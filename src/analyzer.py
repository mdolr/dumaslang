from src import global_variables
from src.synthesizer import action_g0, action_gpl
from src.scanner import scan_g0, scan_gpl


def analyze_g0(node):
    # print(f'Analyzing node : ')
    # print(f'node_type={node.node_type}, aType={node.aType}, COD={node.COD}')
    # Si le noeud est une concatenation
    if node.node_type == 'Conc':
        # On retourne le resultat la l'analyse a droite si celle a gauche deja faite
        # et valide sinon false si gauche invalide
        # print(f'Node right: node_type={node.right.node_type} COD={node.right.COD} ')
        return analyze_g0(node.right) if analyze_g0(node.left) else False

    # Si le noeud est une union
    elif node.node_type == 'Union':
        # On retourne vrai si l'analyse de g0 est valide sinon
        # on retourne l'analyse de g0 a droite
        # revient a valider les differents pans de l'arbre de gauche a droite
        return True if analyze_g0(node.left) else analyze_g0(node.right)

    # Si le noeud est une Star
    elif node.node_type == 'Star':
        # On analyse pour chaque sous noeud
        while analyze_g0(node.value):
            continue

        return True

    # Si le noeud est un UN (0 ou 1)
    elif node.node_type == 'UN':
        # Si analyze_g0 est valide on renvoi True
        if analyze_g0(node.value):
            return True

    # Si le noeud est un atom
    elif node.node_type == 'Atom':
        # On check si c'est un atom terminal
        if node.aType == 'Terminal':
            # On verifie que notre scan nous confirme bien que le caractere
            # present a ce moment est bien celui qu'on est en train de lire
            # print(global_variables.scanned)
            # print(f'node.COD={node.COD} node.aType={node.aType}')
            if global_variables.scanned and (node.COD == global_variables.scanned['code'] or node.COD == global_variables.scanned['chaine']):
                # S'il y a une action on retourne l'analyse de l'action
                if node.ACT != None and node.ACT != 0:
                    action_g0(node.ACT)

                global_variables.scanned, global_variables.grammar = scan_g0(
                    global_variables.grammar)

                return True

            else:
                return False

        # Si c'est un atom non terminal
        elif node.aType == 'NonTerminal':
            # On retourne l'analyse de la case du COD dans l'arbre
            if analyze_g0(global_variables.A[global_variables.Sym.index(node.COD)]):
                # S'il y a une action on retourne l'analyse de l'action
                if node.ACT != None and node.ACT != 0:
                    action_g0(node.ACT)

                # Sinon on retourne false
                return True
            else:
                return False


# Fonction d'analyse de la GPL
# Prend en parametre un noeud (origine de la GPL)

def analyze_gpl(node):
    global A

    # print(f'Analyzing node : ')
    # print(f'node_type={node.node_type}, aType={node.aType}, COD={node.COD}')
    # Si le noeud est une concatenation
    if node.node_type == 'Conc':
        # On retourne le resultat la l'analyse a droite si celle a gauche deja faite
        # et valide sinon false si gauche invalide
        # print(
        #     f'Node right: node_type={node.right.node_type} COD={node.right.COD} ')
        return analyze_gpl(node.right) if analyze_gpl(node.left) else False

    # Si le noeud est une union
    elif node.node_type == 'Union':
        # On retourne vrai si l'analyse de g0 est valide sinon
        # on retourne l'analyse de g0 a droite
        # revient a valider les differents pans de l'arbre de gauche a droite
        # print(f'Avant union', global_variables.program,
        #       'global_variables.scanned:', global_variables.scanned)
        stored_program = global_variables.program
        stored_scanned = global_variables.scanned

        left = analyze_gpl(node.left)

        if left:
            return True

        else:
            # print('Avant reset', global_variables.program,
            #       'global_variables.scanned: ', global_variables.scanned)
            global_variables.program = stored_program
            global_variables.scanned = stored_scanned
            # print('Après reset', global_variables.program,
            #       'global_variables.scanned:', global_variables.scanned)
            right = analyze_gpl(node.right)
            return right

        # return True if analyze_gpl(node.left) else analyze_gpl(node.right)

    # Si le noeud est une Star
    elif node.node_type == 'Star':
        # On analyse pour chaque sous noeud
        while analyze_gpl(node.value):
            continue

        # Puis on renvoi True
        return True

    # Si le noeud est un UN (0 ou 1)
    elif node.node_type == 'UN':
        # Si analyze_gpl est valide on renvoi True
        stored_program = global_variables.program
        stored_scanned = global_variables.scanned

        result = analyze_gpl(node.value)

        if not result:
            # print('Avant reset', global_variables.program,
            #       'global_variables.scanned: ', global_variables.scanned)
            global_variables.program = stored_program
            global_variables.scanned = stored_scanned
            # print('Après reset', global_variables.program,
            #       'global_variables.scanned:', global_variables.scanned)

        return True

    # Si le noeud est un atom
    elif node.node_type == 'Atom':
        # On check si c'est un atom terminal
        if node.aType == 'Terminal':
            # On verifie que notre scan nous confirme bien que le caractere
            # present a ce moment est bien celui qu'on est en train de lire
            # print(global_variables.scanned)
            # print(f'node.COD={node.COD} node.aType={node.aType}')
            if global_variables.scanned and (node.COD == global_variables.scanned['code'] or node.COD == global_variables.scanned['chaine']):
                # print('Egalite verifiee')
                # S'il y a une action on retourne l'analyse de l'action
                if node.ACT != None and node.ACT != 0:
                    action_gpl(node.ACT)

                global_variables.scanned, global_variables.program = scan_gpl(
                    global_variables.program)

                return True

            else:
                # print('Je retourne false')
                return False

        # Si c'est un atom non terminal
        elif node.aType == 'NonTerminal':
            # On retourne l'analyse de la case du COD dans l'arbre
            if analyze_gpl(global_variables.A[global_variables.Sym.index(node.COD)]):
                # S'il y a une action on retourne l'analyse de l'action
                if node.ACT != None and node.ACT != 0:
                    action_gpl(node.ACT)

                # Sinon on retourne false
                return True
            else:
                return False
