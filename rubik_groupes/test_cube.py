"""Contrôles algébriques, exemples indépendants et tests HTTP locaux."""
from collections import deque
import json
import random
import threading
from types import SimpleNamespace
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import cube as c
from cours import EXERCISES, LESSONS, PRESETS
from rubik_groupes import execute, make_server


class Mathematics(unittest.TestCase):
    def test_turns_are_bijections_and_centers_fixed(self):
        for token, permutation in c.MOVES.items():
            self.assertEqual(sorted(permutation), list(c.IDENTITY), token)
            self.assertTrue(all(permutation[9*f+4] == 9*f+4 for f in range(6)))

    def test_clockwise_face_grid_and_order(self):
        expected = [2,5,8,1,4,7,0,3,6]
        for f,face in enumerate(c.FACES):
            self.assertEqual([c.MOVES[face][9*f+i]-9*f for i in range(9)], expected)
            self.assertEqual(c.order(c.MOVES[face]), 4)
            self.assertEqual(c.apply(c.IDENTITY,[face]*4), c.IDENTITY)

    def test_reference_cubie_coordinates(self):
        # Référence indépendante : https://kociemba.org/math/CubeDefs.htm
        references = {
            "U": ([3,0,1,2,4,5,6,7], [0]*8, [3,0,1,2,4,5,6,7,8,9,10,11], [0]*12),
            "R": ([4,1,2,0,7,5,6,3], [2,0,0,1,1,0,0,2], [8,1,2,3,11,5,6,7,4,9,10,0], [0]*12),
            "F": ([1,5,2,3,0,4,6,7], [1,2,0,0,2,1,0,0], [0,9,2,3,4,8,6,7,1,5,10,11], [0,1,0,0,0,1,0,0,1,1,0,0])}
        for face, expected in references.items():
            self.assertEqual(c.cubies(c.apply(c.IDENTITY,[face])), expected)

    def test_random_states_roundtrip_and_invariants(self):
        for seed in range(160):
            word = c.scramble(50,seed)
            state = c.apply(c.IDENTITY,word)
            self.assertEqual(c.validate_colors(c.facelets(state)), state)
            self.assertEqual(c.validate_state(list(state)),state)
            cp,co,ep,eo = c.cubies(state)
            self.assertEqual(sum(co)%3,0)
            self.assertEqual(sum(eo)%2,0)
            self.assertEqual(c.parity(cp),c.parity(ep))
            self.assertEqual(c.apply(state,c.invert(word)),c.IDENTITY)
            self.assertEqual(c.apply(c.IDENTITY,c.simplify(word)),state)

    def test_composition_convention(self):
        a,b = c.MOVES['R'],c.MOVES['U']
        self.assertEqual(c.compose(a,b), c.permutation(['R','U']))
        self.assertNotEqual(c.compose(a,b),c.compose(b,a))
        self.assertEqual(c.compose(c.MOVES['R'],c.MOVES['L']),c.compose(c.MOVES['L'],c.MOVES['R']))

    def test_known_orders(self):
        for word, expected in [("",1),("R",4),("R2",2),("R U",105),("R U R' U'",6),("R U R' D R U' R' D'",3)]:
            self.assertEqual(c.order(c.permutation(c.parse(word))),expected,word)

    def test_targeted_commutator_and_conjugate(self):
        a,b = c.parse("R U R'"),c.parse("D")
        commutator=a+b+c.invert(a)+c.invert(b)
        base=c.info(c.apply(c.IDENTITY,commutator))
        self.assertEqual((base['corners_changed'],base['edges_changed'],base['order']),(3,0,3))
        for setup in ['F','B2','U R']:
            s=c.parse(setup)
            transported=c.info(c.apply(c.IDENTITY,s+commutator+c.invert(s)))
            self.assertEqual((transported['corners_changed'],transported['edges_changed'],transported['order']),(3,0,3))
        self.assertEqual(c.apply(c.IDENTITY,commutator*3),c.IDENTITY)

    def test_intermediate_subgroup(self):
        for seed in range(30):
            rng=random.Random(seed)
            word=[rng.choice(['U',"U'",'U2','D',"D'",'D2','R2','L2','F2','B2']) for _ in range(30)]
            self.assertTrue(c.info(c.apply(c.IDENTITY,word))['in_h'])
        self.assertFalse(c.info(c.apply(c.IDENTITY,c.parse("F R2 F'")))['in_h'])

    def test_three_impossible_states(self):
        for kind, keyword in [('twist','modulo 3'),('flip','modulo 2'),('parity','parités')]:
            result=execute({'action':'impossible','kind':kind})
            self.assertFalse(result['legal'])
            self.assertIn(keyword,result['reason'])
            with self.assertRaises(ValueError): c.validate_colors(result['preview']['facelets'])

    def test_invalid_pieces_centers_and_mirror(self):
        state=list(c.IDENTITY)
        a,b=c.CORNER_SLOTS[0][1:]
        state[a],state[b]=state[b],state[a]
        with self.assertRaisesRegex(ValueError,'miroir'): c.validate_colors(c.facelets(state))
        bad=list(c.facelets(c.IDENTITY));bad[4],bad[13]=bad[13],bad[4]
        with self.assertRaisesRegex(ValueError,'centres'): c.validate_colors(''.join(bad))
        bad=list(c.IDENTITY);bad[0],bad[1]=bad[1],bad[0]
        with self.assertRaises(ValueError):c.validate_state(bad)

    def test_parser_and_reduction(self):
        self.assertEqual(c.parse("r u’F2"), ['R',"U'",'F2'])
        for word in ['R22',"R''",'M','x','(R U)3','__import__',17]:
            with self.assertRaises(ValueError):c.parse(word)
        self.assertEqual(c.simplify(c.parse("R R U U' R' R2")),["R'"])

    def test_cardinality(self):
        self.assertEqual(c.GROUP_SIZE,43252003274489856000)

    def test_documented_external_fixture(self):
        # Exemple publié par le module kociemba, contrôle indépendant des repères.
        facelets='DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD'
        solution=c.parse("D2 R' D' F2 B D R2 D2 R' F2 D' F2 U' B2 L2 U2 D R2 U")
        self.assertEqual(c.apply(c.validate_colors(facelets),solution),c.IDENTITY)

    def test_optional_solver_adapter_checks_result(self):
        state=c.apply(c.IDENTITY,['R'])
        with patch.dict('sys.modules',{'kociemba':SimpleNamespace(solve=lambda _:"R'")}):
            self.assertEqual(c.solve_complete(state),["R'"])
        with patch.dict('sys.modules',{'kociemba':SimpleNamespace(solve=lambda _:"U")}):
            with self.assertRaisesRegex(ValueError,'vérification'):c.solve_complete(state)

    def test_lessons_and_presets_are_valid(self):
        for item in LESSONS+EXERCISES:
            c.validate_state(list(c.apply(c.IDENTITY,c.parse(item['demo']))))
        for item in PRESETS:c.parse(item['sequence'])


class Searches(unittest.TestCase):
    def test_minimality_against_unidirectional_bfs(self):
        distance={c.IDENTITY:0}
        queue=deque([c.IDENTITY])
        while queue:
            state=queue.popleft()
            if distance[state] == 3:continue
            for token in c.TOKENS:
                nxt=c.apply_move(state,token)
                if nxt not in distance:
                    distance[nxt]=distance[state]+1
                    queue.append(nxt)
        samples=random.Random(22).sample(list(distance),60)
        for state in samples:
            result=c.solve_short(state,6)
            self.assertEqual(result['depth'],distance[state])
            self.assertEqual(c.apply(state,result['moves']),c.IDENTITY)

    def test_bound_and_timeout_are_different(self):
        with self.assertRaisesRegex(c.SearchLimit,'Aucune solution'):
            c.solve_short(c.apply(c.IDENTITY,c.parse('R U F2')),2)
        with self.assertRaisesRegex(c.SearchLimit,'Temps'):
            c.solve_short(c.apply(c.IDENTITY,['R']),6,seconds=-1)
        self.assertEqual(c.solve_short(c.IDENTITY,0)['depth'],0)

    def test_six_move_solution_without_history(self):
        state=c.apply(c.IDENTITY,c.parse('R U F2 L D B'))
        result=c.solve_short(state,6)
        self.assertEqual(c.apply(state,result['moves']),c.IDENTITY)
        self.assertEqual(result['depth'],6)

    def test_history_validation(self):
        state=c.apply(c.IDENTITY,c.parse('R U F2'))
        result=execute({'action':'solve','mode':'history','state':list(state),'history':'R U F2'})
        self.assertTrue(result['verified'])
        self.assertEqual(c.apply(state,result['moves']),c.IDENTITY)
        with self.assertRaisesRegex(ValueError,'historique'):
            execute({'action':'solve','mode':'history','state':list(state),'history':'U'})


class LocalServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=make_server(0)
        cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True)
        cls.thread.start()
        cls.url=f'http://127.0.0.1:{cls.server.server_port}'

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown();cls.server.server_close();cls.thread.join()

    def request(self,data,token=None,origin=None):
        headers={'Content-Type':'application/json','X-Rubik-Token':token or self.server.api_token}
        if origin:headers['Origin']=origin
        return urlopen(Request(self.url+'/api',data=json.dumps(data).encode(),headers=headers),timeout=10)

    def test_page_and_bootstrap(self):
        with urlopen(self.url) as r:
            self.assertIn('Le cube comme groupe.',r.read().decode())
        with urlopen(self.url+'/api/bootstrap') as r:
            data=json.load(r)
            self.assertEqual(len(data['lessons']),10)
            self.assertEqual(len(data['exercises']),12)
            self.assertTrue(data['identity']['solved'])
        for path in ['/app.js','/style.css','/favicon.svg']:
            with urlopen(self.url+path) as r:self.assertEqual(r.status,200)

    def test_one_server_per_port(self):
        with self.assertRaises(OSError):
            make_server(self.server.server_port)

    def test_scramble_timeline_solve_import(self):
        with self.request({'action':'scramble','length':4}) as r:word=json.load(r)['sequence']
        with self.request({'action':'timeline','sequence':word}) as r:steps=json.load(r)['steps']
        self.assertEqual(len(steps),4)
        state=steps[-1]['info']['state']
        with self.request({'action':'solve','state':state,'mode':'short','depth':4}) as r:result=json.load(r)
        self.assertEqual(c.apply(tuple(state),result['moves']),c.IDENTITY)
        with self.request({'action':'import','facelets':c.facelets(state)}) as r:self.assertEqual(json.load(r)['state'],state)

    def test_invalid_input_and_cross_origin(self):
        for data,token,origin,expected in [({'action':'analyse','sequence':'M'},None,None,400),
                                            ({'action':'analyse','sequence':'R'},'wrong',None,403),
                                            ({'action':'analyse','sequence':'R'},None,'https://example.com',403)]:
            with self.assertRaises(HTTPError) as context:self.request(data,token,origin)
            self.assertEqual(context.exception.code,expected)
        with self.assertRaises(HTTPError) as context:urlopen(self.url+'/cube.py')
        self.assertEqual(context.exception.code,404)


if __name__ == '__main__':
    unittest.main(verbosity=2)
