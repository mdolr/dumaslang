import re
from src import global_variables


def scan_g0(parsed_grammar):
    # Tant qu'il reste des elements dans l'array
    if len(parsed_grammar) > 0:

        # On recupere l'element actuel
        current_char = parsed_grammar[0]

        # On definit les variables par defaut
        action = 0
        code = 'IDNTER'
        char_type = 'NonTerminal'
        chaine = current_char

        # chaine = re.sub(r"""[0-9]""", "", current_char) # dans la chaine je retire tous les chiffres pour l'action

        # Si on detecte une action on recupere tous les chiffres
        if '#' in parsed_grammar[0]:
            action = re.sub(r"""\D""", "", current_char.split('#')[1])
            chaine = chaine.split('#')[:-1]
            chaine = ''.join(chaine)

            # print(chaine)

            if parsed_grammar[0].endswith("'"):
                chaine += "'"

        # On part du principe que si l'element est entoure de guillemet c'est un element terminal
        if chaine.startswith("'") and chaine.endswith("'"):
            code = 'ELTER'
            char_type = 'Terminal'
            chaine = chaine[1:-1].replace('#', '')
            global_variables.dico_t.append(chaine)
        else:
            chaine = chaine.replace('#', '')
            global_variables.dico_nt.append(chaine)

        # On shift l'array pour aller a l'element suivant
        parsed_grammar = parsed_grammar[1:]

        # On renvoit l'element et la liste d'elements updatee
        return {
            'code': code,
            'chaine': chaine,
            'action': int(str(action)),
            'type': char_type
        }, parsed_grammar

    # Si on est arrive au bout on renvoi None + liste vide
    else:
        return None, []

# Cette fonction va venir scanner une array de string


def scan_gpl(parsed_program):
    # Tant qu'il reste des elements dans l'array
    if len(parsed_program) > 0:

        # On recupere l'element actuel
        current_char = parsed_program[0]

        # On definit les variables par defaut
        action = 0
        code = 'ELTER'
        char_type = 'Terminal'
        chaine = current_char

        # On shift l'array pour aller a l'element suivant
        parsed_program = parsed_program[1:]

        # On renvoit l'element et la liste d'elements updatee
        return {
            'code': code,
            'chaine': chaine.replace('#', ""),
            'action': int(str(action)),
            'type': char_type
        }, parsed_program

    # Si on est arrive au bout on renvoi None + liste vide
    else:
        return None, []
