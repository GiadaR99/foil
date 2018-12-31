from unittest import TestCase

from assertpy import assert_that

from foil.foil import build
from foil.foil import choose
from foil.foil import common
from foil.foil import covers
from foil.foil import entropy
from foil.foil import Expand
from foil.foil import gain
from foil.foil import learn
from foil.foil import max_gain


class ExpandTest(TestCase):

    def test___as_terms(self):
        for i, entry in enumerate([
            # TODO
        ]):
            variables, combination, expected = entry
            with self.subTest(i=i, value=entry):
                result = Expand._as_terms(variables, combination)

                assert_that(
                    result,
                    'Expand._as_terms(variables: Tuple[Variable], combination: Tuple[int, ...]) -> Tuple[Variable]:'
                ).is_equal_to(expected)


class FoilTest(TestCase):

    def test__learn(self):
        for i, entry in enumerate([
            # TODO
        ]):
            background, target, masks, positives, negatives, expected = entry
            with self.subTest(i=i, value=entry):
                result = learn(background, target, masks, positives, negatives)

                assert_that(
                    result,
                    'learn(background: List[Clause], '
                    '      target: Literal, masks: List[Mask], '
                    '      positives: List[Example], negatives: List[Example]'
                    ') -> List[Clause]:'
                ).is_equal_to(expected)

    def test__build(self):
        for i, entry in enumerate([
            # TODO
        ]):
            background, hypothesis, target, masks, positives, negatives, expected = entry
            with self.subTest(i=i, value=entry):
                result = build(background, hypothesis, target, masks, positives, negatives)

                assert_that(
                    result,
                    'build(background: List[Clause], hypothesis: List[Clause], '
                    '      target: Literal, masks: List[Mask], '
                    '      positives: List[Example], negatives: List[Example]'
                    ') -> Tuple[Clause, List[Example], List[Example]]:'
                ).is_equal_to(expected)

    def test__choose(self):
        for i, entry in enumerate([
            # TODO
        ]):
            background, hypothesis, target, masks, positives, negatives, expected = entry
            with self.subTest(i=i, value=entry):
                result = choose(background, hypothesis, target, masks, positives, negatives)

                assert_that(
                    result,
                    'choose(background: List[Clause], hypothesis: List[Clause], '
                    '       target: Literal, body: List[Literal], masks: List[Mask], '
                    '       positives: List[Example], negatives: List[Example]'
                    ') -> Optional[Tuple[Literal, List[Example], List[Example]]]:'
                ).is_equal_to(expected)

    def test__covers(self):
        for i, entry in enumerate([
            # TODO
        ]):
            background, hypothesis, target, body, masks, examples, expected = entry
            with self.subTest(i=i, value=entry):
                result = covers(background, hypothesis, target, body, masks, examples)

                assert_that(
                    result,
                    'covers(background: List[Clause], hypothesis: List[Clause],'
                    '       target: Literal, body: List[Literal],'
                    '       examples: List[Example]'
                    ') -> List[Example]:'
                ).is_equal_to(expected)

    def test__gain(self):
        for i, entry in enumerate([
            # TODO
        ]):
            positives, negatives, positives_i, negatives_i, expected = entry
            with self.subTest(i=i, value=entry):
                result = gain(positives, negatives, positives_i, negatives_i)

                assert_that(
                    result,
                    'gain(positives: List[Example], negatives: List[Example],'
                    '     positives_i: List[Example], negatives_i: List[Example]'
                    ') -> float:'
                ).is_equal_to(expected)

    def test__max_gain(self):
        for i, entry in enumerate([
            # TODO
        ]):
            positives, negatives, positives_i, expected = entry
            with self.subTest(i=i, value=entry):
                result = max_gain(positives, negatives, positives_i)

                assert_that(
                    result,
                    'max_gain(positives: List[Example], negatives: List[Example], positives_i: List[Example]) -> float:'
                ).is_equal_to(expected)

    def test__common(self):
        for i, entry in enumerate([
            # TODO
        ]):
            positives, positives_i, expected = entry
            with self.subTest(i=i, value=entry):
                result = common(positives, positives_i)

                assert_that(
                    result,
                    'common(positives: List[Example], positives_i: List[Example]) -> int:'
                ).is_equal_to(expected)

    def test__entropy(self):
        for i, entry in enumerate([
            # TODO
        ]):
            positives, negatives, expected = entry
            with self.subTest(i=i, value=entry):
                result = entropy(positives, negatives)

                assert_that(
                    result,
                    'entropy(positives: List[Example], negatives: List[Example]) -> float:'
                ).is_equal_to(expected)