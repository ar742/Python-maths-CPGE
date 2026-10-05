"""Comptage exhaustif 1D, invariants et noyau exact 2×2 indépendants."""
import itertools
import json
import math
import unittest
import numpy as np
import ising


def chain_configurations(N):
    states=list(itertools.product([-1,1],repeat=N))
    energies=np.array([-sum(s[i]*s[(i+1)%N] for i in range(N)) for s in states],dtype=float)
    return states,energies


def square_energy_independent(spins):
    L=len(spins)
    return -sum(int(spins[i,j])*(int(spins[(i+1)%L,j])+int(spins[i,(j+1)%L])) for i in range(L) for j in range(L))


def square_states():
    return [np.array([1 if n&(1<<j) else -1 for j in range(4)],dtype=np.int8).reshape(2,2) for n in range(16)]


def sublattice_kernel(theta,color):
    """Toutes les acceptations/rejets possibles d'une couleur du tore 2×2."""
    states=square_states();matrix=np.zeros((16,16));positions=[(i,j) for i in range(2) for j in range(2) if (i+j)%2==color]
    for index,spins in enumerate(states):
        probabilities=[]
        for i,j in positions:
            changed=spins.copy();changed[i,j]*=-1
            delta=square_energy_independent(changed)-square_energy_independent(spins)
            probabilities.append(.5*min(1.,math.exp(-delta/theta)))
        for accepted in itertools.product([False,True],repeat=len(positions)):
            new=spins.copy();probability=1
            for (i,j),take,p in zip(positions,accepted,probabilities):
                probability*=p if take else 1-p
                if take:new[i,j]*=-1
            target=sum((1<<j) for j,s in enumerate(new.ravel()) if s==1)
            matrix[index,target]+=probability
    return matrix


class ChainExact(unittest.TestCase):
    def test_degeneracies_against_exhaustive_configurations(self):
        for N in range(3,10):
            _,energies=chain_configurations(N)
            observed={int(v):int(np.count_nonzero(energies==v)) for v in np.unique(energies)}
            expected={v["energy"]:v["degeneracy"] for v in ising.chain_levels(N)}
            self.assertEqual(observed,expected)

    def test_even_wall_parity_from_periodic_closure(self):
        for spins in itertools.product([-1,1],repeat=7):
            walls=sum(spins[i]!=spins[(i+1)%7] for i in range(7))
            self.assertEqual(walls%2,0)

    def test_total_states_as_exact_large_integer(self):
        for N in [3,4,20,99,100]:
            self.assertEqual(sum(v["degeneracy"] for v in ising.chain_levels(N)),1<<N)
        result=ising.calculate_lab(dict(mode="chaine",N=100,level=4))
        self.assertEqual(result["theory"]["total_states"],str(1<<100))
        self.assertIsInstance(result["theory"]["levels"][4]["degeneracy"],str)

    def test_ground_doublet_and_odd_frustration(self):
        for N in [3,6,99,100]:
            levels=ising.chain_levels(N)
            self.assertEqual(levels[0]["energy"],-N)
            self.assertEqual(levels[0]["degeneracy"],2)
            self.assertEqual(levels[-1]["energy"],N if N%2==0 else N-2)

    def test_canonical_statistics_against_full_enumeration(self):
        for N,theta in [(3,.7),(4,1.3),(7,2),(9,4)]:
            _,energies=chain_configurations(N);weights=np.exp(-energies/theta);p=weights/weights.sum()
            state=ising.chain_statistics(N,theta);mean=float(p@energies)
            self.assertAlmostEqual(state["energy"],mean,places=12)
            self.assertAlmostEqual(state["log_partition"],math.log(float(weights.sum())),places=12)
            self.assertAlmostEqual(state["heat_capacity"],float(p@((energies-mean)**2))/theta**2,places=12)
            self.assertAlmostEqual(state["entropy"],float(-p@np.log(p)),places=12)

    def test_partition_against_transfer_eigenvalues(self):
        for N,theta in [(3,2.2),(8,1.8),(20,.7)]:
            K=1/theta
            exact=(2*math.cosh(K))**N+(2*math.sinh(K))**N
            self.assertAlmostEqual(ising.chain_statistics(N,theta)["log_partition"],math.log(exact),places=12)

    def test_energy_is_beta_derivative(self):
        N=20;beta=.4;h=1e-5
        difference=(ising.chain_statistics(N,1/(beta+h))["log_partition"]-ising.chain_statistics(N,1/(beta-h))["log_partition"])/(2*h)
        self.assertAlmostEqual(difference,-ising.chain_statistics(N,1/beta)["energy"],places=8)

    def test_capacity_is_temperature_derivative(self):
        N=17;theta=1.6;h=1e-5
        derivative=(ising.chain_statistics(N,theta+h)["energy"]-ising.chain_statistics(N,theta-h)["energy"])/(2*h)
        self.assertAlmostEqual(derivative,ising.chain_statistics(N,theta)["heat_capacity"],places=8)

    def test_low_temperature_ground_entropy_remains_ln_two(self):
        state=ising.chain_statistics(100,.05)
        self.assertAlmostEqual(state["energy"],-100,places=12)
        self.assertAlmostEqual(state["entropy"],math.log(2),places=12)
        self.assertLess(state["heat_capacity"],1e-20)

    def test_high_temperature_uniform_microstates(self):
        N=30;state=ising.chain_statistics(N,1e7)
        self.assertAlmostEqual(state["entropy"],N*math.log(2),places=10)
        self.assertLess(abs(state["energy_per_spin"]),2e-7)
        self.assertAlmostEqual(state["log_partition"],N*math.log(2),places=10)

    def test_thermodynamic_energy_limit_and_corrected_stirling(self):
        theta=2;N=100;state=ising.chain_statistics(N,theta)
        self.assertAlmostEqual(state["energy_per_spin"],-math.tanh(1/theta),places=13)
        expected=N/(2*(1+math.exp(2/theta)))
        self.assertAlmostEqual(ising.chain_stirling_pair_mean(N,theta),expected,places=13)
        self.assertAlmostEqual(state["mean_wall_pairs"],expected,places=12)

    def test_canonical_signed_magnetization_zero(self):
        spins,energy=chain_configurations(7);weights=np.exp(-energy/.8)
        means=np.array([np.mean(s) for s in spins])
        self.assertAlmostEqual(float(weights@means/weights.sum()),0,places=14)
        self.assertEqual(ising.chain_statistics(7,.8)["magnetization"],0)


class OnsagerYang(unittest.TestCase):
    def test_critical_temperature_condition(self):
        self.assertAlmostEqual(math.sinh(2/ising.THETA_CRITICAL),1,places=14)
        self.assertAlmostEqual(ising.THETA_CRITICAL,2.269185314213022,places=14)

    def test_exact_formula_below_critical_and_zero_above(self):
        for theta in [.7,1,2]:
            expected=(1-math.sinh(2/theta)**(-4))**.125
            self.assertAlmostEqual(ising.onsager_magnetization(theta),expected,places=14)
        for theta in [ising.THETA_CRITICAL,3,8]:self.assertEqual(ising.onsager_magnetization(theta),0)

    def test_extremes_do_not_overflow(self):
        with np.errstate(over="raise",invalid="raise",divide="raise"):
            values=ising.onsager_magnetization([1e-300,.2,1e300])
        np.testing.assert_allclose(values,[1,1,0],atol=1e-14)

    def test_monotonicity_and_critical_exponent(self):
        theta=np.linspace(.2,ising.THETA_CRITICAL,250);values=ising.onsager_magnetization(theta)
        self.assertTrue(np.all(np.diff(values)<=1e-14))
        a=ising.onsager_magnetization(ising.THETA_CRITICAL*(1-1e-4))
        b=ising.onsager_magnetization(ising.THETA_CRITICAL*(1-1e-5))
        self.assertAlmostEqual(a/b,10**.125,places=3)


class SquareHamiltonian(unittest.TestCase):
    def test_ground_and_checkerboard_energy(self):
        for L in [2,4,8]:
            self.assertEqual(ising.energy_square(np.ones((L,L),dtype=np.int8)),-2*L*L)
            self.assertEqual(ising.energy_square(-np.ones((L,L),dtype=np.int8)),-2*L*L)
            rows,columns=np.indices((L,L));checker=(-1)**(rows+columns)
            self.assertEqual(ising.energy_square(checker),2*L*L)

    def test_local_flip_difference_exhaustive_two_by_two(self):
        for spins in square_states():
            before=square_energy_independent(spins)
            self.assertEqual(ising.energy_square(spins),before)
            for i,j in itertools.product(range(2),repeat=2):
                changed=spins.copy();changed[i,j]*=-1
                self.assertEqual(ising.delta_flip(spins,i,j),square_energy_independent(changed)-before)

    def test_local_flip_difference_random_square(self):
        rng=np.random.default_rng(24)
        for L in [4,8,16]:
            spins=rng.choice([-1,1],size=(L,L));before=square_energy_independent(spins)
            for i,j in [(0,0),(0,L-1),(L-1,0),(L//2,L//2)]:
                after=spins.copy();after[i,j]*=-1
                self.assertEqual(ising.delta_flip(spins,i,j),square_energy_independent(after)-before)

    def test_one_flip_cost_and_parallel_bond_convention(self):
        for L in [2,4]:
            spins=np.ones((L,L),dtype=np.int8)
            self.assertEqual(ising.delta_flip(spins,0,0),8)
            after=spins.copy();after[0,0]=after[0,1]=-1
            self.assertEqual(ising.energy_square(after)-ising.energy_square(spins),8 if L==2 else 12)

    def test_periodic_translation_and_global_flip_symmetries(self):
        rng=np.random.default_rng(8);spins=rng.choice([-1,1],size=(8,8));E=ising.energy_square(spins)
        self.assertEqual(ising.energy_square(-spins),E)
        self.assertEqual(ising.energy_square(np.roll(spins,3,0)),E)
        self.assertEqual(ising.energy_square(np.roll(spins,5,1)),E)


class MetropolisValidation(unittest.TestCase):
    def test_each_color_and_composed_kernel_preserve_boltzmann_distribution(self):
        theta=1.9;states=square_states();energies=np.array([square_energy_independent(s) for s in states])
        p=np.exp(-energies/theta);p/=p.sum()
        A=sublattice_kernel(theta,0);B=sublattice_kernel(theta,1)
        for kernel in [A,B,A@B]:
            np.testing.assert_allclose(kernel.sum(axis=1),1,atol=1e-14)
            np.testing.assert_allclose(p@kernel,p,atol=1e-14)

    def test_metropolis_two_by_two_observations_match_exact_equilibrium(self):
        theta=3.5;states=square_states();energies=np.array([square_energy_independent(s) for s in states])
        weights=np.exp(-energies/theta);weights/=weights.sum()
        expectedE=float(weights@energies)/4;expectedM=float(weights@np.array([abs(np.mean(s)) for s in states]))
        result=ising.metropolis_square(2,theta,burnin=500,sweeps=12000,stride=1,seed=321)
        self.assertLess(abs(result["mean_energy_per_spin"]-expectedE),.04)
        self.assertLess(abs(result["mean_absolute_magnetization"]-expectedM),.03)

    def test_fixed_seed_reproduces_every_measured_value(self):
        a=ising.metropolis_square(8,2.3,50,300,3,742)
        b=ising.metropolis_square(8,2.3,50,300,3,742)
        for key in ["spins","steps","energy_trace","magnetization_trace"]:np.testing.assert_array_equal(a[key],b[key])
        self.assertEqual(a["mean_absolute_magnetization"],b["mean_absolute_magnetization"])

    def test_different_seed_changes_trajectory(self):
        a=ising.metropolis_square(8,2.6,50,300,3,742)
        b=ising.metropolis_square(8,2.6,50,300,3,743)
        self.assertFalse(np.array_equal(a["magnetization_trace"],b["magnetization_trace"]))

    def test_observable_bounds_and_measurement_count(self):
        result=ising.metropolis_square(8,2.3,50,305,20,12)
        self.assertEqual(result["samples"],15)
        self.assertEqual(result["steps"][-1],300)
        self.assertTrue(np.all(abs(result["magnetization_trace"])<=1))
        self.assertTrue(np.all(abs(result["energy_trace"])<=2))
        self.assertGreaterEqual(result["acceptance_rate"],0)
        self.assertLessEqual(result["acceptance_rate"],1)

    def test_frozen_trace_does_not_claim_zero_sampling_error(self):
        result=ising.metropolis_square(8,.2,50,300,5,742,"plus")
        self.assertEqual(result["mean_absolute_magnetization"],1)
        self.assertEqual(result["mean_energy_per_spin"],-2)
        self.assertFalse(result["absolute_diagnostic"]["varying"])
        self.assertIsNone(result["absolute_diagnostic"]["standard_error_blocks"])
        self.assertIsNone(result["absolute_diagnostic"]["effective_samples"])

    def test_checkerboard_updates_signed_integer_arrays_in_place(self):
        spins=np.ones((4,4),dtype=np.int64)
        accepted=ising.checkerboard_sweep(spins,10,np.random.default_rng(4))
        self.assertGreater(accepted,0)
        self.assertTrue(np.any(spins==-1))

    def test_lazy_proposal_escapes_zero_field_band_cycle(self):
        spins=np.repeat(((-1)**np.arange(8))[:,None],8,axis=1).astype(np.int8)
        before=spins.copy();rng=np.random.default_rng(52)
        for _ in range(4):ising.checkerboard_sweep(spins,2.3,rng)
        self.assertFalse(np.array_equal(spins,before))
        self.assertFalse(np.array_equal(spins,-before))
        self.assertNotEqual(ising.energy_square(spins),0)

    def test_acceptance_counts_only_real_flip_proposals(self):
        result=ising.metropolis_square(8,2.4,50,300,5,12)
        self.assertGreater(result["proposed_flips"],0)
        self.assertLessEqual(result["accepted_flips"],result["proposed_flips"])
        self.assertAlmostEqual(result["acceptance_rate"],result["accepted_flips"]/result["proposed_flips"],places=15)
        self.assertAlmostEqual(result["proposed_flips"]/(300*64),.5,places=2)

    def test_autocorrelation_blocks_on_independent_data(self):
        values=np.random.default_rng(18).normal(size=4000)
        result=ising.autocorrelation_diagnostic(values,stride=5)
        self.assertTrue(result["varying"])
        self.assertEqual(result["acf"][0],1)
        self.assertGreater(result["effective_samples"],2000)
        self.assertLess(result["standard_error_blocks"],.035)
        self.assertEqual(result["tau_sweeps"],5*result["tau_measurements"])


class InputAndExports(unittest.TestCase):
    def test_both_modes_return_finite_json(self):
        for data in [dict(mode="chaine",N=100,level=49,theta=.2),dict(mode="carre",theta=8,size=8,burnin=50,sweeps=300),dict(mode="carre",theta=.2,size=8,initial="plus",burnin=50,sweeps=300)]:
            result=ising.calculate_lab(data);json.dumps(result,allow_nan=False)
            for c in result["charts"]:
                for s in c["series"]:self.assertEqual(len(s["x"]),len(s["y"]))

    def test_large_exported_degeneracy_is_not_a_rounded_javascript_integer(self):
        result=ising.calculate_lab(dict(mode="chaine",N=100,level=25))
        self.assertEqual(result["table"]["rows"][25][3],str(2*math.comb(100,50)))

    def test_reject_invalid_modes_temperatures_and_counts(self):
        invalid=[dict(mode="sphere"),dict(theta=0),dict(theta=math.nan),dict(theta=True),dict(N=2),dict(N=3.5),dict(N=5,level=3),dict(mode="carre",size=9),dict(mode="carre",seed=-1),dict(mode="carre",stride=0)]
        for data in invalid:
            with self.subTest(data=data),self.assertRaises(ValueError):ising.calculate_lab(data)

    def test_reject_nonspin_data_and_odd_checkerboard(self):
        for spins in [np.zeros((4,4)),np.ones((3,4)),np.ones(4)]:
            with self.assertRaises(ValueError):ising.energy_square(spins)
        with self.assertRaises(ValueError):ising.metropolis_square(9,2)

    def test_finite_signed_and_infinite_spontaneous_averages_are_distinguished(self):
        result=ising.calculate_lab(dict(mode="carre",theta=1.5,size=8,initial="plus",burnin=50,sweeps=300))
        self.assertEqual(result["theory"]["finite_signed_equilibrium_magnetization"],0)
        self.assertGreater(result["theory"]["infinite_spontaneous_magnetization"],.9)
        self.assertGreater(result["theory"]["mean_magnetization"],.9)


if __name__=="__main__":unittest.main()
