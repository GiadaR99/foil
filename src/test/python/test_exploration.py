from unittest import TestCase

from assertpy import assert_that

from foil.exploration import get_assignments
from foil.exploration import get_closure
from foil.exploration import get_masks
from foil.exploration import get_signature
from foil.exploration import get_variables
from foil.exploration import sort
from foil.models import Example
from foil.models import Literal
from foil.models import Mask


class ExplorationTest(TestCase):

    def test__get_assignments(self):
        for i, entry in enumerate([
            ([Example(a) for a in [
                {'X': 0, 'Y': 1},
                {'X': 0, 'Y': 2},
                {'X': 0, 'Y': 3},
                {'X': 0, 'Y': 4},
                {'X': 0, 'Y': 5},
                {'X': 0, 'Y': 6},
                {'X': 0, 'Y': 8},
                {'X': 1, 'Y': 2},
                {'X': 3, 'Y': 2},
                {'X': 3, 'Y': 4},
                {'X': 3, 'Y': 5},
                {'X': 3, 'Y': 6},
                {'X': 3, 'Y': 8},
                {'X': 4, 'Y': 5},
                {'X': 4, 'Y': 6},
                {'X': 4, 'Y': 8},
                {'X': 6, 'Y': 8},
                {'X': 7, 'Y': 6},
                {'X': 7, 'Y': 8},
            ]], ([
                     {'X': 0, 'Y': 1},
                     {'X': 0, 'Y': 2},
                     {'X': 0, 'Y': 3},
                     {'X': 0, 'Y': 4},
                     {'X': 0, 'Y': 5},
                     {'X': 0, 'Y': 6},
                     {'X': 0, 'Y': 8},
                     {'X': 1, 'Y': 2},
                     {'X': 3, 'Y': 2},
                     {'X': 3, 'Y': 4},
                     {'X': 3, 'Y': 5},
                     {'X': 3, 'Y': 6},
                     {'X': 3, 'Y': 8},
                     {'X': 4, 'Y': 5},
                     {'X': 4, 'Y': 6},
                     {'X': 4, 'Y': 8},
                     {'X': 6, 'Y': 8},
                     {'X': 7, 'Y': 6},
                     {'X': 7, 'Y': 8},
                 ],
                 [],
             )),
        ]):
            examples, expected = entry
            with self.subTest(i=i, value=entry):
                result = get_assignments(examples)

                assert_that(
                    result,
                    'get_assignments(examples: List[Example]) -> Tuple[List[Assignment], List[Assignment]]',
                ).is_equal_to(expected)

    def test__get_closure(self):
        for i, entry in enumerate([
            (
                    [
                        Literal.parse('edge(0,1)'),
                        Literal.parse('edge(0,3)'),
                        Literal.parse('edge(1,2)'),
                        Literal.parse('edge(3,2)'),
                        Literal.parse('edge(3,4)'),
                        Literal.parse('edge(4,5)'),
                        Literal.parse('edge(4,6)'),
                        Literal.parse('edge(6,8)'),
                        Literal.parse('edge(7,6)'),
                        Literal.parse('edge(7,8)'),
                    ],
                    [c for c in range(9)],
                    Literal.parse('path(X,Y)'),
                    [
                        {'X': 0, 'Y': 1},
                        {'X': 0, 'Y': 2},
                        {'X': 0, 'Y': 3},
                        {'X': 0, 'Y': 4},
                        {'X': 0, 'Y': 5},
                        {'X': 0, 'Y': 6},
                        {'X': 0, 'Y': 8},
                        {'X': 1, 'Y': 2},
                        {'X': 3, 'Y': 2},
                        {'X': 3, 'Y': 4},
                        {'X': 3, 'Y': 5},
                        {'X': 3, 'Y': 6},
                        {'X': 3, 'Y': 8},
                        {'X': 4, 'Y': 5},
                        {'X': 4, 'Y': 6},
                        {'X': 4, 'Y': 8},
                        {'X': 6, 'Y': 8},
                        {'X': 7, 'Y': 6},
                        {'X': 7, 'Y': 8},
                    ],
                    [],
                    (
                            [
                                {'X': 0, 'Y': 1},
                                {'X': 0, 'Y': 2},
                                {'X': 0, 'Y': 3},
                                {'X': 0, 'Y': 4},
                                {'X': 0, 'Y': 5},
                                {'X': 0, 'Y': 6},
                                {'X': 0, 'Y': 8},
                                {'X': 1, 'Y': 2},
                                {'X': 3, 'Y': 2},
                                {'X': 3, 'Y': 4},
                                {'X': 3, 'Y': 5},
                                {'X': 3, 'Y': 6},
                                {'X': 3, 'Y': 8},
                                {'X': 4, 'Y': 5},
                                {'X': 4, 'Y': 6},
                                {'X': 4, 'Y': 8},
                                {'X': 6, 'Y': 8},
                                {'X': 7, 'Y': 6},
                                {'X': 7, 'Y': 8},
                            ],
                            [
                                {'X': 0, 'Y': 0},
                                {'X': 0, 'Y': 7},
                                {'X': 1, 'Y': 0},
                                {'X': 1, 'Y': 1},
                                {'X': 1, 'Y': 3},
                                {'X': 1, 'Y': 4},
                                {'X': 1, 'Y': 5},
                                {'X': 1, 'Y': 6},
                                {'X': 1, 'Y': 7},
                                {'X': 1, 'Y': 8},
                                {'X': 2, 'Y': 0},
                                {'X': 2, 'Y': 1},
                                {'X': 2, 'Y': 2},
                                {'X': 2, 'Y': 3},
                                {'X': 2, 'Y': 4},
                                {'X': 2, 'Y': 5},
                                {'X': 2, 'Y': 6},
                                {'X': 2, 'Y': 7},
                                {'X': 2, 'Y': 8},
                                {'X': 3, 'Y': 0},
                                {'X': 3, 'Y': 1},
                                {'X': 3, 'Y': 3},
                                {'X': 3, 'Y': 7},
                                {'X': 4, 'Y': 0},
                                {'X': 4, 'Y': 1},
                                {'X': 4, 'Y': 2},
                                {'X': 4, 'Y': 3},
                                {'X': 4, 'Y': 4},
                                {'X': 4, 'Y': 7},
                                {'X': 5, 'Y': 0},
                                {'X': 5, 'Y': 1},
                                {'X': 5, 'Y': 2},
                                {'X': 5, 'Y': 3},
                                {'X': 5, 'Y': 4},
                                {'X': 5, 'Y': 5},
                                {'X': 5, 'Y': 6},
                                {'X': 5, 'Y': 7},
                                {'X': 5, 'Y': 8},
                                {'X': 6, 'Y': 0},
                                {'X': 6, 'Y': 1},
                                {'X': 6, 'Y': 2},
                                {'X': 6, 'Y': 3},
                                {'X': 6, 'Y': 4},
                                {'X': 6, 'Y': 5},
                                {'X': 6, 'Y': 6},
                                {'X': 6, 'Y': 7},
                                {'X': 7, 'Y': 0},
                                {'X': 7, 'Y': 1},
                                {'X': 7, 'Y': 2},
                                {'X': 7, 'Y': 3},
                                {'X': 7, 'Y': 4},
                                {'X': 7, 'Y': 5},
                                {'X': 7, 'Y': 7},
                                {'X': 8, 'Y': 0},
                                {'X': 8, 'Y': 1},
                                {'X': 8, 'Y': 2},
                                {'X': 8, 'Y': 3},
                                {'X': 8, 'Y': 4},
                                {'X': 8, 'Y': 5},
                                {'X': 8, 'Y': 6},
                                {'X': 8, 'Y': 7},
                                {'X': 8, 'Y': 8},
                            ],
                    )
            ),
        ]):
            world, constants, target, pos, neg, expected = entry
            with self.subTest(i=i, value=entry):
                result = get_closure(world, constants, target, pos, neg)

                assert_that(
                    result,
                    'get_closure(world: List[Literal], constants: List[Value], target: Literal, '
                    'pos: List[Assignment], neg: List[Assignment]) -> Tuple[List[Assignment], List[Assignment]]',
                ).is_equal_to(expected)

    def test__get_masks(self):
        for i, entry in enumerate([
            (
                    [
                        Literal.parse('edge(0,1)'),
                        Literal.parse('edge(0,3)'),
                        Literal.parse('edge(1,2)'),
                        Literal.parse('edge(3,2)'),
                        Literal.parse('edge(3,4)'),
                        Literal.parse('edge(4,5)'),
                        Literal.parse('edge(4,6)'),
                        Literal.parse('edge(6,8)'),
                        Literal.parse('edge(7,6)'),
                        Literal.parse('edge(7,8)'),
                        Literal.parse('path(X,Y)'),
                    ],
                    [Mask(False, 'edge', 2), Mask(False, 'path', 2)],
            ),
        ]):
            literals, expected = entry
            with self.subTest(i=i, value=entry):
                result = get_masks(literals)

                assert_that(
                    result,
                    'get_masks(background: List[Clause], target: Literal) -> List[Mask]',
                ).is_equal_to(expected)

    def test__get_signature(self):
        for i, entry in enumerate([
            (['X', 'Y'], (0, 0), ['X', 'X']),
            (['X', 'Y'], (0, 1), ['X', 'Y']),
            (['X', 'Y'], (0, 2), ['X', 'V0']),
            (['X', 'Y'], (1, 0), ['Y', 'X']),
            (['X', 'Y'], (1, 1), ['Y', 'Y']),
            (['X', 'Y'], (1, 2), ['Y', 'V0']),
            (['X', 'Y'], (2, 0), ['V0', 'X']),
            (['X', 'Y'], (2, 1), ['V0', 'Y']),
            (['X', 'Y'], (2, 2), ['V0', 'V0']),
            (['X', 'Y'], (0, 3), ['X', 'V0']),
            (['X', 'Y'], (1, 3), ['Y', 'V0']),
            (['X', 'Y'], (3, 0), ['V0', 'X']),
            (['X', 'Y'], (3, 1), ['V0', 'Y']),
            (['X', 'Y'], (3, 3), ['V0', 'V0']),
            (['X', 'Y'], (0, 0, 0), ['X', 'X', 'X']),
            (['X', 'Y'], (0, 0, 1), ['X', 'X', 'Y']),
            (['X', 'Y'], (0, 1, 0), ['X', 'Y', 'X']),
            (['X', 'Y'], (0, 1, 1), ['X', 'Y', 'Y']),
            (['X', 'Y'], (1, 0, 0), ['Y', 'X', 'X']),
            (['X', 'Y'], (1, 0, 1), ['Y', 'X', 'Y']),
            (['X', 'Y'], (1, 1, 0), ['Y', 'Y', 'X']),
            (['X', 'Y'], (1, 1, 1), ['Y', 'Y', 'Y']),
        ]):
            variables, combination, expected = entry
            with self.subTest(i=i, value=entry):
                result = get_signature(variables, combination)

                assert_that(
                    result,
                    'get_signature(variables: List[Variable], combination: Tuple[int, ...]) -> List[Variable]'
                ).is_equal_to(expected)

    def test__get_variables(self):
        for i, entry in enumerate([
            ([Literal.parse('path(X,Y)')], ['X', 'Y']),
            ([Literal.parse('path(Y,Z)')], ['Y', 'Z']),
            ([Literal.parse('path(X,Y,Z,X,Y,Y)')], ['X', 'Y', 'Z']),
            ([Literal.parse('path(X,Y)'), Literal.parse('edge(X,V0)'), Literal.parse('path(V0,Y)')], ['X', 'Y', 'V0']),
        ]):
            literals, expected = entry
            with self.subTest(i=i, value=entry):
                result = get_variables(literals)

                assert_that(
                    result,
                    'get_variables(literals: List[Literal]) -> List[Variable]',
                ).is_equal_to(expected)

    def test__sort(self):
        for i, entry in enumerate([
            (
                    [{'X': 10, 'Y': 0}, {'X': 5, 'Y': 5}, {'X': 0, 'Y': 10}],
                    [{'X': 0, 'Y': 10}, {'X': 5, 'Y': 5}, {'X': 10, 'Y': 0}],
            ),
        ]):
            assignments, expected = entry
            with self.subTest(i=i, value=entry):
                result = sort(assignments)

                assert_that(
                    result,
                    'sort(assignments: List[Assignment]) -> List[Assignment]',
                ).is_equal_to(expected)