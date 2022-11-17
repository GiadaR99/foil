from src.main.python.foil.learning import get_constants, get_closure, get_masks, foil
from src.main.python.foil.models import Program
from src.main.python.foil.models import Clause
from src.main.python.foil.models import Example
from src.main.python.foil.models import Literal
from src.main.python.foil.models import Label

if __name__ == '__main__':
    background = [
        Clause.parse('d_90_99(a).'),
        Clause.parse('d_70_79(b).'),
        Clause.parse('d_60_69(c).'),
        Clause.parse('d_80_89(d).'),
        Clause.parse('d_80_89(e).'),
        Clause.parse('d_70_79(f).'),
        Clause.parse('d_70_79(g).'),
        Clause.parse('d_70_79(h).'),
        Clause.parse('d_90_99(i).'),
        Clause.parse('d_100(j).'),
        Clause.parse('d_70_79(k).'),
        Clause.parse('d_80_89(l).'),
        Clause.parse('d_80_89(m).'),

        Clause.parse('d_over90(a).'),
        Clause.parse('d_over70(b).'),
        Clause.parse('d_over80(d).'),
        Clause.parse('d_over80(e).'),
        Clause.parse('d_over70(f).'),
        Clause.parse('d_over70(g).'),
        Clause.parse('d_over70(h).'),
        Clause.parse('d_over90(i).'),
        Clause.parse('d_over90(j).'),
        Clause.parse('d_over70(k).'),
        Clause.parse('d_over80(l).'),
        Clause.parse('d_over80(m).'),

        Clause.parse('informatica(a).'),
        Clause.parse('liceoScientifico(b).'),
        Clause.parse('altroLiceo(c).'),
        Clause.parse('altroIstitutoTecnico(d).'),
        Clause.parse('altroIstitutoTecnico(e).'),
        Clause.parse('altroLiceo(f).'),
        Clause.parse('liceoScientifico(g).'),
        Clause.parse('informatica(h).'),
        Clause.parse('informatica(i).'),
        Clause.parse('liceoScientifico(j).'),
        Clause.parse('altroIstitutoTecnico(k).'),
        Clause.parse('liceoScientifico(l).'),
        Clause.parse('informatica(m).'),

        Clause.parse('istitutoTecnico(a).'),
        Clause.parse('liceo(b).'),
        Clause.parse('liceo(c).'),
        Clause.parse('istitutoTecnico(d).'),
        Clause.parse('istitutoTecnico(e).'),
        Clause.parse('liceo(f).'),
        Clause.parse('liceo(g).'),
        Clause.parse('istitutoTecnico(h).'),
        Clause.parse('istitutoTecnico(i).'),
        Clause.parse('liceo(j).'),
        Clause.parse('istitutoTecnico(k).'),
        Clause.parse('liceo(l).'),
        Clause.parse('istitutoTecnico(m).'),

        Clause.parse('inSede(a).'),
        Clause.parse('inSede(b).'),
        Clause.parse('fuorisede(c).'),
        Clause.parse('inSede(d).'),
        Clause.parse('inSede(e).'),
        Clause.parse('fuoriSede(f).'),
        Clause.parse('inSede(g).'),
        Clause.parse('inSede(h).'),
        Clause.parse('inSede(i).'),
        Clause.parse('inSede(j).'),
        Clause.parse('fuorisede(k).'),
        Clause.parse('inSede(l).'),
        Clause.parse('fuorisede(m).'),


        Clause.parse('nonLavoratore(a).'),
        Clause.parse('lavoratore(b).'),
        Clause.parse('lavoratore(c).'),
        Clause.parse('nonLavoratore(d).'),
        Clause.parse('nonLavoratore(e).'),
        Clause.parse('nonLavoratore(f).'),
        Clause.parse('lavoratore(g).'),
        Clause.parse('lavoratore(h).'),
        Clause.parse('lavoratore(i).'),
        Clause.parse('nonLavoratore(j).'),
        Clause.parse('lavoratore(k).'),
        Clause.parse('nonLavoratore(l).'),
        Clause.parse('nonLavoratore(m).')
    ]
    print('Background:')
    print()
    print(background)
    print()

    target_name = 'l_110'

    target = Literal.parse(target_name + '(X)')
    examples = [
        Example({'X': 'a'}, Label.POSITIVE),
        Example({'X': 'g'}, Label.POSITIVE),
        Example({'X': 'i'}, Label.POSITIVE),
        Example({'X': 'j'}, Label.POSITIVE),
        Example({'X': 'm'}, Label.POSITIVE),
        Example({'X': 'b'}, Label.NEGATIVE),
        Example({'X': 'c'}, Label.NEGATIVE),
        Example({'X': 'd'}, Label.NEGATIVE),
        Example({'X': 'e'}, Label.NEGATIVE),
        Example({'X': 'f'}, Label.NEGATIVE),
        Example({'X': 'h'}, Label.NEGATIVE),
        Example({'X': 'k'}, Label.NEGATIVE),
        Example({'X': 'l'}, Label.NEGATIVE)
    ]

    print('Esempi:')
    print()

    for example in examples:
        if example.label is Label.POSITIVE:
            print('+ : '+target_name+'('+example.assignment.get('X')+')')
        else:
            print('- : '+target_name+'('+example.assignment.get('X')+')')

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
