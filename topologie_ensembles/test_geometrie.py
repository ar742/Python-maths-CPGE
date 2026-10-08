"""Vérifications indépendantes des décisions exactes et des scènes géométriques."""
import json
import math
import unittest
import numpy as np
from catalogue_geometrie import LABS
from modeles_geometrie import (calculate, MODELS, lp_norm, ball_boundary,
    classify_shape, reciprocal_distance, project_disk, disk_union_distance,
    segment_min_norm, segment_disk_interval, intervals_cover_unit,
    convex_hull, polygon_signed_area, halfplane_margins, project_polygon,
    boundary_point)


class NormesTests(unittest.TestCase):
    def test_normes_et_marge(self):
        self.assertEqual(lp_norm([3, -4], 1), 7)
        self.assertEqual(lp_norm([3, -4], 2), 5)
        self.assertEqual(lp_norm([3, -4], math.inf), 4)
        self.assertAlmostEqual(lp_norm([1, 1], 3), 2 ** (1 / 3))
        out = calculate('boules_normes', dict(norm='1', radius=1, x=.7, y=.7))
        self.assertFalse(out['scene']['membership'])
        self.assertAlmostEqual(out['scene']['margin'], -.4)

    def test_frontiere_ouverte_fermee(self):
        for mode, expected in [('open', False), ('closed', True)]:
            out = calculate('boules_normes', dict(norm='2', radius=1, x=1, y=0, closed=mode))
            self.assertEqual(out['scene']['membership'], expected)
            self.assertEqual(out['scene']['margin'], 0)

    def test_points_du_bord_satisfont_formule(self):
        for p in [1, 2, 3.25, 8, math.inf]:
            for x in ball_boundary(p, .75)[::15]:
                self.assertAlmostEqual(lp_norm(x, p), .75, places=13)

    def test_equivalence_des_normes(self):
        rng = np.random.default_rng(71)
        for x in rng.normal(size=(100, 2)):
            a, b, c = lp_norm(x, 1), lp_norm(x, 2), lp_norm(x, math.inf)
            self.assertLessEqual(c, b + 1e-14)
            self.assertLessEqual(b, a + 1e-14)
            self.assertLessEqual(a, math.sqrt(2) * b + 1e-14)


class EnsemblesTests(unittest.TestCase):
    def test_disques_meme_adherence_frontiere(self):
        for shape in ['open', 'closed']:
            c = classify_shape(shape, [1, 0], 1)
            self.assertTrue(c['adherent'])
            self.assertTrue(c['boundary'])
            self.assertFalse(c['interior'])
            self.assertEqual(c['belongs'], shape == 'closed')

    def test_trou_point_adherent_sans_appartenance(self):
        c = classify_shape('punctured', [0, 0], 1)
        self.assertFalse(c['belongs'])
        self.assertFalse(c['interior'])
        self.assertTrue(c['adherent'])
        self.assertTrue(c['boundary'])
        self.assertEqual(c['boundary_distance'], 0)

    def test_anneau_bords_et_interieur(self):
        for rho in [.5, 1]:
            c = classify_shape('annulus', [rho, 0], 1)
            self.assertTrue(c['belongs'])
            self.assertTrue(c['boundary'])
            self.assertFalse(c['interior'])
        self.assertTrue(classify_shape('annulus', [.75, 0], 1)['interior'])
        self.assertFalse(classify_shape('annulus', [.3, 0], 1)['adherent'])

    def test_distance_zero_infimum_non_atteint(self):
        for x in [0, -.17]:
            d = reciprocal_distance(x, False)
            self.assertEqual(d['distance'], -x)
            self.assertFalse(d['attained'])
            self.assertFalse(d['belongs'])
        d = reciprocal_distance(0, True)
        self.assertTrue(d['attained'])
        self.assertTrue(d['belongs'])

    def test_distance_reciproques_compare_enumeration(self):
        values = 1 / np.arange(1, 20001)
        for x in [.0015, .013, .09, .26, .7, 1, 1.2]:
            self.assertAlmostEqual(reciprocal_distance(x)['distance'], float(abs(values - x).min()), places=14)
        for k in [1, 2, 3, 7, 49, 200]:
            self.assertTrue(reciprocal_distance(1 / k)['belongs'])

    def test_N_ne_change_pas_distance_infinie(self):
        small = calculate('adherence_suite', dict(N=8, x=.004))
        large = calculate('adherence_suite', dict(N=200, x=.004))
        self.assertEqual(small['scene']['distance'], large['scene']['distance'])
        self.assertEqual(small['scene']['distance']['distance'], 0)
        for eps in [.2, .1, .025, .005]:
            w = calculate('adherence_suite', dict(epsilon=eps))['scene']['witness']
            self.assertGreater(w['value'], 0)
            self.assertLess(w['value'], eps)

    def test_interieur_relatif_au_bord(self):
        out = calculate('topologie_relative', dict(x=0, b=.65, epsilon=.2))['scene']
        self.assertTrue(out['relative_interior'])
        self.assertFalse(out['ambient_interior'])
        self.assertTrue(out['neighborhood_inside'])
        out = calculate('topologie_relative', dict(x=.5, b=.5, epsilon=.1))['scene']
        self.assertFalse(out['relative_interior'])
        self.assertFalse(out['neighborhood_inside'])
        out = calculate('topologie_relative', dict(x=1, b=1.2, epsilon=.6))['scene']
        self.assertTrue(out['relative_interior'])
        self.assertFalse(out['ambient_interior'])
        self.assertTrue(out['neighborhood_inside'])

    def test_voisinage_ouvert_peut_toucher_b_exclu(self):
        s = calculate('topologie_relative', dict(x=.25, b=.5, epsilon=.25))['scene']
        self.assertTrue(s['neighborhood_inside'])
        s = calculate('topologie_relative', dict(x=.25, b=.5, epsilon=.3))['scene']
        self.assertFalse(s['neighborhood_inside'])

    def test_intersection_infinie_et_union_infinie(self):
        s = calculate('operations_ouverts', dict(operation='intersection', N=10, x=.05))['scene']
        self.assertTrue(s['finite_membership'])
        self.assertFalse(s['infinite_membership'])
        s = calculate('operations_ouverts', dict(operation='union', N=10, x=.05))['scene']
        self.assertFalse(s['finite_membership'])
        self.assertTrue(s['infinite_membership'])
        s = calculate('operations_ouverts', dict(operation='union', N=100, x=0))['scene']
        self.assertFalse(s['finite_membership'])
        self.assertFalse(s['infinite_membership'])


class ConvexiteTests(unittest.TestCase):
    def test_projection_sur_disque(self):
        np.testing.assert_allclose(project_disk([3, 4], [0, 0], 2), [1.2, 1.6], atol=1e-14)
        np.testing.assert_array_equal(project_disk([.2, .4], [0, 0], 2), [.2, .4])

    def test_union_deux_projections_et_distance(self):
        d, qs, _ = disk_union_distance([0, .8], 3, .7)
        self.assertEqual(len(qs), 2)
        self.assertAlmostEqual(d, 1.7 - .7)
        for q in qs:
            self.assertAlmostEqual(float(np.linalg.norm(q - [0, .8])), d)
        d, qs, _ = disk_union_distance([-1, .2], 2, .8)
        self.assertEqual(d, 0)
        self.assertEqual(len(qs), 1)

    def test_distance_un_contexte_non_convexe_reste_lipschitz(self):
        rng = np.random.default_rng(37)
        for _ in range(80):
            x, y = rng.uniform(-3, 3, (2, 2))
            dx = disk_union_distance(x, 3, .7)[0]
            dy = disk_union_distance(y, 3, .7)[0]
            self.assertLessEqual(abs(dx - dy), np.linalg.norm(x - y) + 1e-13)

    def test_segment_annulus_contre_exemple_exact(self):
        norm, t = segment_min_norm([.8, 0], [-.8, 0])
        self.assertEqual(norm, 0)
        self.assertEqual(t, .5)
        s = calculate('convexite', dict(shape='annulus', a=0, b=180, rho=.8))['scene']
        self.assertFalse(s['segment_contained'])
        self.assertFalse(s['global_convex'])
        s = calculate('convexite', dict(shape='annulus', a=0, b=20, rho=.8))['scene']
        self.assertTrue(s['segment_contained'])
        self.assertFalse(s['global_convex'])

    def test_intervalles_segment_calcules_par_racines(self):
        q = segment_disk_interval([-2, 0], [2, 0], [0, 0], 1)
        self.assertAlmostEqual(q[0], .25)
        self.assertAlmostEqual(q[1], .75)
        self.assertFalse(intervals_cover_unit([q]))
        self.assertTrue(intervals_cover_unit([(0, .5), (.5, 1)]))
        self.assertFalse(intervals_cover_unit([(0, .49), (.51, 1)]))
        self.assertIsNone(segment_disk_interval([-2, 2], [2, 2], [0, 0], 1))

    def test_union_temoin_nonconvexite_meme_si_connexe(self):
        for separation in [.1, .8, 2]:
            s = calculate('convexite', dict(shape='union', separation=separation))['scene']
            a, b = map(np.array, s['witness_endpoints'])
            mid = np.array(s['witness_midpoint'])
            self.assertLessEqual(disk_union_distance(a, separation, .65)[0], 1e-14)
            self.assertLessEqual(disk_union_distance(b, separation, .65)[0], 1e-14)
            self.assertGreater(disk_union_distance(mid, separation, .65)[0], 0)

    def test_enveloppe_carre_points_internes_doublons(self):
        points = [[-1, -1], [1, -1], [1, 1], [-1, 1], [0, 0], [1, -1], [.4, 1]]
        hull = convex_hull(points)
        self.assertEqual(len(hull), 4)
        self.assertEqual(polygon_signed_area(hull), 4)
        for point in points:
            self.assertGreaterEqual(float(halfplane_margins(hull, point).min()), 0)

    def test_barycentre_marges_et_sommet_poids1(self):
        for alpha in [0, .4, 1]:
            s = calculate('enveloppe_convexe', dict(alpha=alpha))['scene']
            weights = np.array(s['weights'])
            self.assertAlmostEqual(float(weights.sum()), 1)
            self.assertGreaterEqual(weights.min(), 0)
            self.assertGreaterEqual(min(s['margins']), -1e-13)
            np.testing.assert_allclose(np.array(s['weights']) @ np.array(s['cloud']), s['barycenter'], atol=1e-14)
            if alpha == 1:
                np.testing.assert_array_equal(s['barycenter'], s['cloud'][0])

    def test_projection_rectangle_egale_clamp(self):
        v = np.array([[-1, -.65], [1, -.65], [1, .65], [-1, .65]])
        rng = np.random.default_rng(13)
        for x in rng.uniform(-2.5, 2.5, (80, 2)):
            np.testing.assert_allclose(project_polygon(x, v), np.clip(x, [-1, -.65], [1, .65]), atol=2e-14)

    def test_projection_triangle_variation_pythagore_et_lipschitz(self):
        v = np.array([[-1, -.75], [1, -.75], [.1, 1.1]])
        rng = np.random.default_rng(11)
        for x, y in rng.uniform(-2.5, 2.5, (60, 2, 2)):
            q, r = project_polygon(x, v), project_polygon(y, v)
            self.assertGreaterEqual(float(halfplane_margins(v, q).min()), -1e-13)
            self.assertLessEqual(float(((v - q) @ (x - q)).max()), 1e-13)
            self.assertLessEqual(float(np.linalg.norm(q - r)), float(np.linalg.norm(x - y)) + 1e-13)
            for z in v:
                self.assertGreaterEqual(float(np.sum((x - z) ** 2) - np.sum((x - q) ** 2) - np.sum((z - q) ** 2)), -1e-12)

    def test_projection_sommet_et_point_interieur(self):
        v = np.array([[-1, -.75], [1, -.75], [.1, 1.1]])
        np.testing.assert_allclose(project_polygon([.1, 2.3], v), [.1, 1.1], atol=1e-14)
        np.testing.assert_array_equal(project_polygon([0, 0], v), [0, 0])
        np.testing.assert_allclose(boundary_point(v, 0), boundary_point(v, 1), atol=1e-14)


class ConnexiteTests(unittest.TestCase):
    def test_plan_epointe_chemin_et_deux_segments_evitent_zero(self):
        s = calculate('connexite_chemins', dict(space='punctured', angle=180))['scene']
        self.assertTrue(s['path_exists'])
        self.assertEqual(s['components'], 1)
        self.assertGreater(s['path_minimum_radius'], 0)
        self.assertGreater(s['two_segments']['minimum_radius'], 0)
        paths = [q for q in s['paths'] if q['label'] == 'Chemin radial et angulaire']
        norms = np.linalg.norm(np.array(paths[0]['points']), axis=1)
        self.assertGreaterEqual(norms.min(), .8 - 1e-13)
        self.assertLessEqual(norms.max(), 1.2 + 1e-13)

    def test_anneau_chemin_reste_entre_bords(self):
        for angle in [-180, -45, 0, 95, 180]:
            s = calculate('connexite_chemins', dict(space='annulus', angle=angle, r1=.55, r2=1.4))['scene']
            route = next(q for q in s['paths'] if q['label'] == 'Chemin radial et angulaire')
            norms = np.linalg.norm(np.array(route['points']), axis=1)
            self.assertGreaterEqual(float(norms.min()), .5)
            self.assertLessEqual(float(norms.max()), 1.5)

    def test_separations_et_tvi(self):
        for space in ['axis', 'disks']:
            s = calculate('connexite_chemins', dict(space=space))['scene']
            self.assertFalse(s['path_exists'])
            self.assertEqual(s['components'], 2)


class ContratTests(unittest.TestCase):
    def test_dix_catalogues_et_moteurs(self):
        self.assertEqual(len(LABS), 10)
        self.assertEqual({a['id'] for a in LABS}, set(MODELS))

    def test_presets_bornes_et_selects_json_fini(self):
        for lab in LABS:
            params = {c['key']: c['value'] for c in lab['controls']}
            variants = [params] + [dict(params, **q['values']) for q in lab['presets']]
            for control in lab['controls']:
                choices = [control['min'], control['max']] if control['type'] == 'range' else [q['value'] for q in control['options']]
                variants.extend(dict(params, **{control['key']: choice}) for choice in choices)
            for values in variants:
                with self.subTest(lab=lab['id'], values=values):
                    out = calculate(lab['id'], values)
                    json.dumps(out, allow_nan=False)
                    self.assertTrue(out['metrics'])
                    self.assertTrue(out['charts'])
                    self.assertTrue(out['steps'])
                    for chart in out['charts']:
                        for line in chart['series']:
                            self.assertEqual(len(line['x']), len(line['y']))
                            self.assertLessEqual(len(line['x']), 650)

    def test_inconnu_refuse(self):
        with self.assertRaises(ValueError):
            calculate('inconnu', {})


if __name__ == '__main__':
    unittest.main()
