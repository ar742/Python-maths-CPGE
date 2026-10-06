"""Certificats indépendants des cinq ateliers de réduction."""
import json
import unittest

import sympy as sp

import reductions as r


def independent_minimal(A):
    """Premier lien linéaire entre les matrices I,A,... (sans Smith)."""
    columns = []
    for k in range(A.rows+1):
        current = A**k
        flattened = sp.Matrix([current[i, j] for i in range(A.rows) for j in range(A.cols)])
        if columns:
            B = sp.Matrix.hstack(*columns)
            if B.row_join(flattened).rank() == B.cols:
                coefficients = B.gauss_jordan_solve(-flattened)[0]
                return sp.Poly(r.X**k+sum(coefficients[j]*r.X**j for j in range(k)), r.X, domain=sp.QQ)
        columns.append(flattened)
    raise AssertionError("Cayley–Hamilton absent")


def matrix_from_strings(entries):
    return sp.Matrix([[sp.sympify(value) for value in row] for row in entries])


class InvariantsAndSpectrumTests(unittest.TestCase):
    def test_smith_minimal_matches_first_matrix_dependency(self):
        matrices = [sp.zeros(3), 2*sp.eye(3), sp.diag(1, 1, 2),
                    sp.Matrix([[0, -1], [1, 0]]),
                    sp.Matrix([[1, 1, 0], [0, 1, 1], [0, 0, 1]]),
                    sp.Matrix([[1, sp.Rational(1, 2), 0], [0, -2, 1], [0, 0, -2]]),
                    sp.Matrix([[0, 0, 1], [1, 0, 1], [0, 1, 0]])]
        for A in matrices:
            with self.subTest(A=A):
                chi, mu, factors = r.exact_invariants(A)
                self.assertEqual(mu, independent_minimal(A))
                self.assertEqual(chi.as_expr(), (r.X*sp.eye(A.rows)-A).det().expand())
                self.assertEqual(sum(p.degree() for p in factors), A.rows)

    def test_real_rotation_depends_on_the_field(self):
        for field, expected in [("Q", False), ("R", False), ("C", True)]:
            result = r.spectre(dict(famille="rotation", corps=field))
            self.assertEqual(result["theory"]["diagonalizable"], expected)
            self.assertEqual(result["theory"]["split"], expected)

    def test_symmetric_matrix_can_require_an_extension_of_Q(self):
        self.assertFalse(r.spectre(dict(famille="symetrique", corps="Q"))["theory"]["diagonalizable"])
        self.assertTrue(r.spectre(dict(famille="symetrique", corps="R"))["theory"]["diagonalizable"])

    def test_repeated_eigenvalue_is_not_a_defect_by_itself(self):
        result = r.spectre(dict(famille="double"))
        self.assertTrue(result["theory"]["diagonalizable"])
        self.assertIn(["1", 2, 2, "1, 1"], result["table"]["rows"])

    def test_kernel_dimensions_match_direct_rank_calculations(self):
        A = sp.diag(r.jordan_block(3, 2), sp.Matrix([[2]]))
        _, _, _, blocks, *_ = r.spectral_structure(A)
        self.assertEqual(len(blocks), 1)
        self.assertEqual(blocks[0]["sizes"], [3, 1])
        self.assertEqual(blocks[0]["kernels"], [0, 2, 3, 4, 4])
        for k in range(5):
            self.assertEqual(blocks[0]["kernels"][k], 4-((A-2*sp.eye(4))**k).rank())

    def test_generic_irreducible_cubic_keeps_exact_roots(self):
        A = sp.Matrix([[0, 0, 1], [1, 0, 1], [0, 1, 0]])
        result = r.spectre(dict(matrix=[[str(v) for v in row] for row in A.tolist()], corps="C"))
        self.assertTrue(result["theory"]["diagonalizable"])
        self.assertEqual(result["theory"]["minimal"], "X^3 - X - 1")
        self.assertEqual(len(result["table"]["rows"]), 3)
        json.dumps(result, allow_nan=False)

    def test_zero_and_scalar_one_dimensional(self):
        for entry in [0, -3, "1/7"]:
            result = r.spectre(dict(matrix=[[entry]], corps="Q"))
            self.assertTrue(result["theory"]["diagonalizable"])
            self.assertEqual(result["table"]["rows"][0][1:3], [1, 1])


class DunfordTests(unittest.TestCase):
    def test_recueil_matrix_and_base(self):
        A, P, J = r._tp_matrix()
        expected = sp.Matrix([[sp.Rational(5, 3), -sp.Rational(1, 3), sp.Rational(4, 3)],
                              [sp.Rational(4, 3), sp.Rational(1, 3), -sp.Rational(1, 3)], [0, 0, 1]])
        self.assertEqual(A, expected)
        self.assertEqual(A*P, P*J)
        result = r.dunford_newton(A)
        self.assertEqual(result["D"], sp.eye(3))
        self.assertEqual(result["N"]**3, sp.zeros(3))
        self.assertNotEqual(result["N"]**2, sp.zeros(3))
        self.assertEqual(result["nilpotence_index"], 3)
        self.assertEqual(len(result["history"])-1, 1)

    def test_multiple_eigenvalues_recover_D_by_known_similarity(self):
        J = sp.diag(r.jordan_block(3, -2), sp.Matrix([[3]]))
        P = sp.Matrix([[1, 1, 0, 2], [0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]])
        A = P*J*P.inv()
        result = r.dunford_newton(A)
        self.assertEqual(result["D"], P*sp.diag(-2, -2, -2, 3)*P.inv())
        self.assertEqual(result["N"], P*(J-sp.diag(-2, -2, -2, 3))*P.inv())
        self.assertEqual(result["nilpotence_index"], 3)

    def test_newton_terminates_at_most_logarithmically(self):
        A, _, _ = r.DUNFORD_FAMILIES["deux_blocs"]()
        result = r.dunford_newton(A)
        self.assertLessEqual(len(result["history"])-1, 2)
        self.assertTrue(result["history"][-1]["residual"].is_zero)
        for state in result["history"]:
            self.assertLess(state["polynomial"].degree(), result["minimal"].degree())

    def test_irreducible_quadratic_repeated_exactly(self):
        A, _, _ = r._rotation_jordan()
        R = sp.Matrix([[0, -1], [1, 0]])
        result = r.dunford_newton(A)
        self.assertEqual(result["D"], sp.diag(R, R))
        self.assertEqual(result["N"], sp.zeros(2).row_join(sp.eye(2)).col_join(sp.zeros(2, 4)))
        self.assertEqual(result["nilpotence_index"], 2)
        self.assertEqual(result["D"]**2, -sp.eye(4))
        self.assertFalse(r.dunford(dict(famille="rotation_jordan", corps="R"))["theory"]["diagonalizable_over_field"])
        self.assertTrue(r.dunford(dict(famille="rotation_jordan", corps="C"))["theory"]["diagonalizable_over_field"])

    def test_semisimple_needs_no_correction(self):
        A = sp.Matrix([[2, 1], [1, 2]])
        result = r.dunford_newton(A)
        self.assertEqual(result["D"], A)
        self.assertEqual(result["N"], sp.zeros(2))
        self.assertEqual(result["nilpotence_index"], 1)
        self.assertEqual(len(result["history"]), 1)

    def test_nilpotent_D_is_zero(self):
        result = r.dunford_newton(r.jordan_block(4))
        self.assertEqual(result["D"], sp.zeros(4))
        self.assertEqual(result["N"], r.jordan_block(4))
        self.assertEqual(result["nilpotence_index"], 4)


class CyclicTests(unittest.TestCase):
    def test_companion_characteristic_and_Krylov_orientation(self):
        p = (r.X-1)*(r.X-2)*(r.X-3)
        A = r.companion(p)
        self.assertEqual(A, sp.Matrix([[0, 0, 6], [1, 0, -11], [0, 1, 6]]))
        self.assertEqual(A.charpoly(r.X).as_expr(), sp.expand(p))
        self.assertEqual(r.krylov(A, sp.Matrix([1, 0, 0])), sp.eye(3))

    def test_exists_not_for_every_nonzero_vector(self):
        chosen = r.cyclique(dict(famille="diagonale", vecteur="cyclique"))
        eigen = r.cyclique(dict(famille="diagonale", vecteur="propre"))
        self.assertTrue(chosen["theory"]["cyclic_matrix"])
        self.assertTrue(eigen["theory"]["cyclic_matrix"])
        self.assertTrue(chosen["theory"]["cyclic_vector"])
        self.assertFalse(eigen["theory"]["cyclic_vector"])
        self.assertEqual(eigen["theory"]["rank"], 1)

    def test_scalar_matrix_commutant_has_dimension_n_squared(self):
        result = r.cyclique(dict(famille="scalaire"))
        self.assertFalse(result["theory"]["cyclic_matrix"])
        self.assertEqual(result["theory"]["commutant_dimension"], 9)
        self.assertEqual(result["theory"]["polynomial_algebra_dimension"], 1)

    def test_cyclic_commutant_is_polynomial_algebra(self):
        for family in ["compagnon", "jordan", "diagonale"]:
            result = r.cyclique(dict(famille=family))
            self.assertEqual(result["theory"]["commutant_dimension"], 3)
            self.assertEqual(result["theory"]["polynomial_algebra_dimension"], 3)

    def test_vector_annulator_differs_from_matrix_minimal(self):
        A = sp.diag(1, 2, 3)
        p = r.vector_minimal(A, sp.Matrix([1, 1, 0]))
        self.assertEqual(p.as_expr(), (r.X**2-3*r.X+2))
        result = r.cyclique(dict(famille="diagonale", vecteur="manuel", v="1 1 0"))
        self.assertEqual(result["theory"]["rank"], 2)
        self.assertFalse(result["theory"]["cyclic_vector"])

    def test_zero_vector_and_irreducible_no_rational_eigenvector(self):
        result = r.cyclique(dict(famille="compagnon", vecteur="manuel", v=[0, 0, 0]))
        self.assertEqual(result["theory"]["rank"], 0)
        self.assertEqual(result["theory"]["vector_minimal"], "1")
        with self.assertRaises(ValueError):
            r.cyclique(dict(matrix=[[0, -1], [1, 0]], vecteur="propre"))

    def test_search_general_rational_similarity(self):
        P = sp.Matrix([[1, 2, 1, 0], [0, 1, 1, 2], [0, 0, 1, -1], [0, 0, 0, 1]])
        A = P*sp.diag(1, 2, 3, 4)*P.inv()
        v = r.cyclic_vector(A)
        K = r.krylov(A, v)
        self.assertNotEqual(K.det(), 0)
        self.assertEqual(A*K, K*r.companion((r.X-1)*(r.X-2)*(r.X-3)*(r.X-4)))


class FrobeniusTests(unittest.TestCase):
    def test_families_and_independent_minimal(self):
        expected = {
            "irreductible": [r.X**2+1, r.X**2+1],
            "deux_facteurs": [r.X**2-1, sp.expand((r.X**2-1)*(r.X-2)**2)],
            "puissances": [r.X-1, sp.expand((r.X-1)**3)],
            "cyclique": [sp.expand((r.X**2+1)**2)],
        }
        for family, polynomials in expected.items():
            for shear in [0, 1, 3]:
                with self.subTest(family=family, shear=shear):
                    A, P, F, _ = r.frobenius_family(family, shear)
                    chi, mu, factors = r.exact_invariants(A)
                    self.assertEqual([p.as_expr() for p in factors], polynomials)
                    self.assertEqual(mu, independent_minimal(A))
                    self.assertEqual(A*P, P*F)
                    self.assertEqual(P.det(), 1)
                    self.assertEqual(chi.as_expr(), sp.expand(sp.prod(polynomials)))

    def test_irreducible_and_repeated_irreducible_jordan_difference(self):
        A, *_ = r.frobenius_family("irreductible")
        B, *_ = r.frobenius_family("cyclique")
        self.assertEqual(A.charpoly(r.X), B.charpoly(r.X))
        self.assertEqual(independent_minimal(A).as_expr(), r.X**2+1)
        self.assertEqual(independent_minimal(B).as_expr(), r.X**4+2*r.X**2+1)
        self.assertTrue(A.is_diagonalizable())
        self.assertFalse(B.is_diagonalizable())


class CayleyTests(unittest.TestCase):
    def test_recueil_vandermonde_trace_and_determinant(self):
        A, *_ = r.CAYLEY_FAMILIES["tp"]()
        self.assertEqual(A, sp.Matrix([[1, 1, 1, 1], [1, 2, 3, 5], [1, 4, 9, 25], [1, 8, 27, 125]]))
        self.assertEqual(A.det(), 48)
        self.assertEqual(sp.trace(A), 137)
        self.assertEqual(A.charpoly(r.X).as_expr(), r.X**4-137*r.X**3+799*r.X**2-646*r.X+48)

    def test_newton_and_Faddeev_against_determinant_random_rational(self):
        matrices = [sp.Matrix([[1, 2], [3, 4]]),
                    sp.Matrix([[0, 1, 3], [2, -1, 0], [1, 2, 2]]),
                    sp.Matrix([[1, sp.Rational(1, 2), 0, 3], [0, -2, 1, 0], [2, 0, 3, 1], [1, 0, 0, 0]])]
        for A in matrices:
            expected = sp.Poly((r.X*sp.eye(A.rows)-A).det().expand(), r.X, domain=sp.QQ)
            newton, _, _ = r.newton_coefficients(A)
            faddeev, states = r.faddeev_leverrier(A)
            self.assertEqual(newton, expected)
            self.assertEqual(faddeev, expected)
            self.assertEqual(states[-1]["matrix"], sp.zeros(A.rows))

    def test_trace_formula_determinant_dimensions_two_and_three(self):
        A = sp.Matrix([[1, 2], [3, 5]])
        B = sp.Matrix([[1, 0, 2], [3, 2, 1], [0, -1, 4]])
        self.assertEqual(A.det(), (sp.trace(A)**2-sp.trace(A**2))/2)
        self.assertEqual(B.det(), (sp.trace(B)**3-3*sp.trace(B)*sp.trace(B**2)+2*sp.trace(B**3))/6)

    def test_euclidean_power_and_inverse_for_every_family(self):
        for family in r.CAYLEY_FAMILIES:
            for power in [0, 1, 2, 12, 40]:
                result = r.cayley(dict(famille=family, power=power))
                A, *_ = r.CAYLEY_FAMILIES[family]()
                self.assertEqual(matrix_from_strings(result["theory"]["power_matrix"]), A**power)
                inverse_polynomial = result["theory"]["inverse_polynomial"]
                if A.det():
                    # Vérifier l'inverse fourni contre l'algorithme de Gauss.
                    inverse = next(b for b in result["matrices"] if b["label"].startswith("A⁻¹"))
                    self.assertEqual(matrix_from_strings(inverse["entries"]), A.inv())
                    self.assertIsNotNone(inverse_polynomial)
                else:
                    self.assertIsNone(inverse_polynomial)

    def test_rotation_power_period_and_singular_zero_dimension(self):
        result = r.cayley(dict(famille="rotation", power=40))
        self.assertEqual(result["theory"]["power_remainder"], "1")
        self.assertEqual(matrix_from_strings(result["theory"]["power_matrix"]), sp.eye(2))
        zero = r.cayley(dict(matrix=[[0]], power=0))
        self.assertEqual(matrix_from_strings(zero["theory"]["power_matrix"]), sp.eye(1))
        self.assertIsNone(zero["theory"]["inverse_polynomial"])


class ContractTests(unittest.TestCase):
    def test_all_presets_are_strict_JSON(self):
        families = dict(spectre=r.SPECTRE_FAMILIES, dunford=r.DUNFORD_FAMILIES,
                        cyclique=r.CYCLIQUE_FAMILIES, frobenius=dict.fromkeys(["irreductible", "deux_facteurs", "puissances", "cyclique", "meme_chi_a", "meme_chi_b"]),
                        cayley=r.CAYLEY_FAMILIES)
        for lab, options in families.items():
            for family in options:
                with self.subTest(lab=lab, family=family):
                    result = r.calculate_lab(dict(lab=lab, famille=family))
                    json.dumps(result, allow_nan=False)
                    self.assertTrue(result["metrics"])
                    self.assertTrue(result["notes"])
                    for chart in result["charts"]:
                        for series in chart["series"]:
                            self.assertEqual(len(series["x"]), len(series["y"]))

    def test_limits_and_unknown_values(self):
        for data in [dict(lab="unknown"), dict(lab="spectre", corps="Z"),
                     dict(lab="cayley", power=-1), dict(lab="cayley", power=41),
                     dict(lab="cayley", power=1.2), dict(lab="frobenius", shear=4),
                     dict(lab="cayley", power=10**500),
                     dict(lab="spectre", matrix=[[1, 2]]),
                     dict(lab="dunford", matrix=[["sin(1)"]]),
                     dict(lab="cyclique", vecteur="manuel", v=[1, 2])]:
            with self.subTest(data=data), self.assertRaises(ValueError):
                r.calculate_lab(data)

    def test_UI_semicolon_inputs(self):
        result = r.cyclique(dict(famille="compagnon", vecteur="manuel", v="1;1;1"))
        self.assertEqual(result["theory"]["vector"], [["1"], ["1"], ["1"]])
        result = r.cayley(dict(matrix="1 0;0 1"))
        self.assertEqual(result["theory"]["minimal"], "X - 1")


class DenseEnrichmentTests(unittest.TestCase):
    def test_controlled_dense_change_of_basis_is_exactly_orthogonal(self):
        P = r.dense_basis()
        self.assertEqual(P.T*P, sp.eye(6))
        self.assertEqual(P.det(), -1)
        for family in ["jordan42", "jordan321", "symetrique6"]:
            A, Q, J = r.SPECTRE_FAMILIES[family]()
            self.assertEqual(A*Q, Q*J)
            self.assertGreaterEqual(sum(value != 0 for value in A), 30)

    def test_same_characteristic_different_Jordan_from_direct_kernels(self):
        expected = {"jordan42": [0, 2, 4, 5, 6, 6, 6], "jordan321": [0, 3, 5, 6, 6, 6, 6]}
        characteristics = []
        for family, dimensions in expected.items():
            A, *_ = r.SPECTRE_FAMILIES[family]()
            characteristics.append(A.charpoly(r.X).as_expr())
            self.assertEqual([6-((A-sp.eye(6))**k).rank() for k in range(7)], dimensions)
            result = r.spectre(dict(famille=family))
            self.assertEqual(result["theory"]["jordan_blocks"][0]["kernels"], dimensions)
        self.assertEqual(characteristics[0], characteristics[1])
        self.assertEqual(characteristics[0], sp.expand((r.X-1)**6))

    def test_dense_Dunford_against_known_generalized_eigenspaces(self):
        A, P, J = r.DUNFORD_FAMILIES["dense6"]()
        result = r.dunford_newton(A)
        expected_D = P*sp.diag(1, 1, 1, -2, -2, 3)*P.T
        self.assertEqual(result["D"], expected_D)
        self.assertEqual(result["N"], P*(J-sp.diag(1, 1, 1, -2, -2, 3))*P.T)
        self.assertEqual(result["N"]**3, sp.zeros(6))
        self.assertNotEqual(result["N"]**2, sp.zeros(6))
        self.assertEqual(result["D"]*result["N"], result["N"]*result["D"])

    def test_dense_nilpotent42_has_D_zero_and_exact_index_four(self):
        A, *_ = r.DUNFORD_FAMILIES["nilpotent42"]()
        result = r.dunford_newton(A)
        self.assertEqual(result["D"], sp.zeros(6))
        self.assertEqual(result["N"], A)
        self.assertEqual(A**4, sp.zeros(6))
        self.assertNotEqual(A**3, sp.zeros(6))
        self.assertEqual([6-(A**k).rank() for k in range(5)], [0, 2, 4, 5, 6])

    def test_dense_recurrence_matches_direct_companion_dynamics(self):
        A, P, C = r.CYCLIQUE_FAMILIES["recurrence6"]()
        result = r.cyclique(dict(terms=24))
        sequence = [sp.Rational(s) for s in result["theory"]["sequence"]]
        current = sp.eye(6)[:, 0]
        expected = []
        for k in range(24):
            expected.append(current[-1])
            current = C*current
        self.assertEqual(sequence, expected)
        coefficients = sp.Poly(r.RECURRENCE6, r.X).all_coeffs()[::-1]
        for k in range(18):
            self.assertEqual(sum(coefficients[j]*sequence[k+j] for j in range(7)), 0)
        self.assertEqual(sequence[:6], [0, 0, 0, 0, 0, 1])
        self.assertEqual(matrix_from_strings(result["theory"]["vector"]), P[:, 0])
        self.assertEqual(result["theory"]["commutant_dimension"], 6)

    def test_noncyclic_six_dimensional_commutant_has_extra_directions(self):
        result = r.cyclique(dict(famille="deux_chaines6"))
        A, *_ = r.CYCLIQUE_FAMILIES["deux_chaines6"]()
        self.assertFalse(result["theory"]["cyclic_matrix"])
        self.assertEqual(result["theory"]["rank"], 4)
        self.assertEqual(result["theory"]["commutant_dimension"], 10)
        self.assertEqual(r.commutant_dimension(A), 10)
        J = sp.diag(r.jordan_block(4, 1), r.jordan_block(2, 1))
        operator = sp.kronecker_product(sp.eye(6), J)-sp.kronecker_product(J.T, sp.eye(6))
        self.assertEqual(36-operator.rank(), 10)

    def test_six_dimensional_Frobenius_same_chi_but_different_minimal(self):
        A, P, F, factors = r.frobenius_family("meme_chi_a", 2)
        B, Q, G, other = r.frobenius_family("meme_chi_b", 2)
        self.assertEqual(A.charpoly(r.X), B.charpoly(r.X))
        self.assertEqual(A.charpoly(r.X).as_expr(), sp.expand((r.X-1)**4*(r.X+2)**2))
        self.assertEqual(independent_minimal(A).degree(), 4)
        self.assertEqual(independent_minimal(B).degree(), 6)
        self.assertEqual(A*P, P*F)
        self.assertEqual(B*Q, Q*G)
        self.assertEqual(factors[1].rem(factors[0]).as_expr(), 0)
        self.assertEqual(len(other), 1)

    def test_dense_Cayley_traces_are_independent_of_nilpotent_parts(self):
        A, *_ = r.CAYLEY_FAMILIES["dense6"]()
        result = r.cayley(dict(power=15))
        expected = [3+2*(-2)**k+3**k for k in range(1, 7)]
        self.assertEqual([sp.Rational(s) for s in result["theory"]["traces"]], expected)
        self.assertEqual(matrix_from_strings(result["theory"]["power_matrix"]), A**15)
        self.assertEqual(A.det(), 12)
        self.assertEqual(sp.trace(A), 2)

    def test_new_defaults_have_semantic_scenes_and_pedagogy(self):
        for lab in r.REDUCTION_LABS:
            result = r.calculate_lab(dict(lab=lab))
            self.assertTrue(result["scenes"])
            pedagogy = result["pedagogy"]
            for key in ("mission", "objects", "reading", "proof", "questions"):
                self.assertTrue(pedagogy[key])
            for scene in result["scenes"]:
                if scene["kind"] == "graph":
                    ids = {node["id"] for node in scene["nodes"]}
                    for edge in scene["edges"]:
                        self.assertIn(edge["source"], ids)
                        self.assertIn(edge["target"], ids)
            json.dumps(result, allow_nan=False)


if __name__ == "__main__":
    unittest.main()
