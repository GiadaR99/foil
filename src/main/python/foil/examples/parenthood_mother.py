from src.main.python.foil.learning import get_constants, get_closure, get_masks, foil
from src.main.python.foil.models import Program
from src.main.python.foil.models import Clause
from src.main.python.foil.models import Example
from src.main.python.foil.models import Literal
from src.main.python.foil.models import Label

if __name__ == '__main__':
    background = [
        Clause.parse('parent(a,b).'), Clause.parse('parent(a,c).'), Clause.parse('parent(d,b).'),
        Clause.parse('male(a).'), Clause.parse('female(c).'), Clause.parse('female(d).')
    ]
    print('Background:')
    print()
    print(background)
    print()

    target_name = 'mother'

    target = Literal.parse(target_name + '(X,Y)')
    examples = [
        Example({'X': 'd', 'Y': 'b'}, Label.POSITIVE),
        Example({'X': 'a', 'Y': 'b'}, Label.NEGATIVE),
        Example({'X': 'a', 'Y': 'c'}, Label.NEGATIVE),
        Example({'X': 'a', 'Y': 'd'}, Label.NEGATIVE),
        Example({'X': 'b', 'Y': 'a'}, Label.NEGATIVE),
        Example({'X': 'b', 'Y': 'c'}, Label.NEGATIVE),
        Example({'X': 'b', 'Y': 'd'}, Label.NEGATIVE),
        Example({'X': 'c', 'Y': 'a'}, Label.NEGATIVE),
        Example({'X': 'c', 'Y': 'b'}, Label.NEGATIVE),
        Example({'X': 'c', 'Y': 'd'}, Label.NEGATIVE),
        Example({'X': 'd', 'Y': 'a'}, Label.NEGATIVE),
        Example({'X': 'd', 'Y': 'c'}, Label.NEGATIVE)
    ]

    print('Esempi:')
    print()

    for example in examples:
        if example.label is Label.POSITIVE:
            print('+ : '+target_name+'('+example.assignment.get('X')+','+example.assignment.get('Y')+')')
        else:
            print('- : '+target_name+'('+example.assignment.get('X')+','+example.assignment.get('Y')+')')

    constants = get_constants([target, *{l for c in background for l in c.literals}])
    world = Program(background).ground()
    positives, negatives = get_closure(target, constants, world, examples)
    masks = get_masks([*{l for c in background for l in c.literals}])

    for clause in foil(target, background, masks, constants, positives, negatives):
        print()
        print('Risultato:')
        print()
        print(clause)

    print()

    print('Done.')
