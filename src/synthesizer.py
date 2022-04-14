from src import global_variables
from src.structures import gen_atom, gen_union, gen_conc, gen_star, gen_un


def action_g0(act):
    if act == 1:
        t1 = global_variables.action_pile[-1]
        t2 = global_variables.action_pile[-2]
        global_variables.action_pile = global_variables.action_pile[:-2]

        if t2.COD in global_variables.Sym:
            global_variables.A[global_variables.Sym.index(t2.COD)] = t1
        else:
            global_variables.A.append(t1)
            global_variables.Sym.append(t2.COD)

    elif act == 2:
        global_variables.action_pile.append(
            gen_atom(global_variables.scanned['chaine'], global_variables.scanned['action'], global_variables.scanned['type']))

    elif act == 3:
        t1 = global_variables.action_pile[-1]
        t2 = global_variables.action_pile[-2]
        global_variables.action_pile = global_variables.action_pile[:-2]
        global_variables.action_pile.append(gen_union(t2, t1))

    elif act == 4:
        t1 = global_variables.action_pile[-1]
        t2 = global_variables.action_pile[-2]
        global_variables.action_pile = global_variables.action_pile[:-2]
        global_variables.action_pile.append(gen_conc(t2, t1))

    elif act == 5:
        if global_variables.scanned['type'] == 'Terminal':
            global_variables.action_pile.append(
                gen_atom(global_variables.scanned['chaine'], global_variables.scanned['action'], 'Terminal'))
        else:
            global_variables.action_pile.append(
                gen_atom(global_variables.scanned['chaine'], global_variables.scanned['action'], 'NonTerminal'))

    elif act == 6:
        t1 = global_variables.action_pile[-1]
        global_variables.action_pile = global_variables.action_pile[:-1]
        global_variables.action_pile.append(gen_star(t1))

    elif act == 7:
        t1 = global_variables.action_pile[-1]
        global_variables.action_pile = global_variables.action_pile[:-1]
        global_variables.action_pile.append(gen_un(t1))


# Une fonction pour recuperer une variable / string / nombre dans le bon type
# en se basant sur les declarations de variables passees etc


def get_token():
    if global_variables.scanned['chaine'].startswith('"') and global_variables.scanned['chaine'].endswith('"'):
        return ['LDC', str(global_variables.scanned['chaine'][1:-1])]
    else:
        if global_variables.scanned['chaine'] in global_variables.table_memoire:
            return ['LDV', global_variables.table_memoire[global_variables.scanned['chaine']]]
        elif str(global_variables.scanned['chaine']) in ['Bon', 'Mauvais', 'Vide']:
            if str(global_variables.scanned['chaine']) in ['Bon', 'Mauvais']:
                return ['LDC', 1 if str(global_variables.scanned['chaine']) == 'Bon' else 0]
            else:
                return ['LDC', None]
        else:
            return ['LDC', float(global_variables.scanned['chaine']) if '.' in global_variables.scanned['chaine'] else int(global_variables.scanned['chaine'])]


def action_gpl(act):
    # global fonction
    # global global_variables.pcode_global_variables.fonctions
    # global global_variables.pcode_storage

    # Chargement avec creation prealable si necessaire
    if act == 1:
        if not global_variables.scanned['chaine'] in global_variables.table_memoire:
            global_variables.table_memoire[global_variables.scanned['chaine']] = len(
                list(global_variables.table_memoire.keys()))

        global_variables.pcode.append('LDA')
        global_variables.pcode.append(
            global_variables.table_memoire[global_variables.scanned['chaine']])

    elif act == 2:
        # Chargement d'une valeur / variable avec le bon type
        global_variables.pcode.extend(get_token())

    elif act == 3:
        # Lors de comparaison chargement 2nde variable
        # pour mettre en place le calcul d'un booleen
        # l'operateur est placé dans global_variables.pcode[-1]

        # on insere le chargement de ntore variable
        # avant l'operateur mais après le chargement de la 1ere variable
        token = get_token()
        token.append(global_variables.pcode[-1])

        global_variables.pcode = global_variables.pcode[:-1]
        global_variables.pcode.extend(token)

    elif act == 4:
        # Affectation dans le valeur = variable
        global_variables.pcode.extend(get_token())
        global_variables.pcode.append('AFF')

    elif act == 5:
        global_variables.pcode.append('AFF')

    elif act == 6:
        global_variables.pcode.append('ADD')

    elif act == 7:
        global_variables.pcode.append('MOINS')

    elif act == 8:
        global_variables.pcode.append('MULT')

    elif act == 9:
        global_variables.pcode.append('DIV')

    elif act == 10:
        # Creation de l'espace memoire d'une variable sans
        # affectation directe
        if not global_variables.scanned['chaine'] in global_variables.table_memoire:
            global_variables.table_memoire[global_variables.scanned['chaine']] = len(
                list(global_variables.table_memoire.keys()))

    elif act == 12:
        # On charge en mémoire avant de demander l'écriture
        global_variables.pcode.extend(get_token())
        global_variables.pcode.append('WRT')

    elif act == 13:
        global_variables.pcode.append('WRTLN')

    elif act == 14:
        global_variables.pcode.append('STOP')

    elif act == 15:
        global_variables.pcode.append('RD')
        global_variables.pcode.append('AFF')

    elif act == 16:
        global_variables.pcode.append('RDLN')

    elif act == 19:
        global_variables.pcode.append('OR')

    elif act == 21:
        global_variables.pcode.append('AND')

    elif act == 22:
        global_variables.pcode.append('NOT')

    elif act == 23:
        global_variables.pcode.append('EQ')

    elif act == 24:
        global_variables.pcode.append('INF')

    elif act == 25:
        global_variables.pcode.append('INFE')

    elif act == 26:
        global_variables.pcode.append('SUP')

    elif act == 27:
        global_variables.pcode.append('SUPE')

    elif act == 28:
        global_variables.pcode.append('DIFF')

    elif act == 29:
        global_variables.pcode.append('JIF')
        global_variables.pcode.append(-1)

    elif act == 30:
        # Pour fermer un JIF dans un if simple
        # en prenant le dernier -1 enregistré
        global_variables.pcode[len(global_variables.pcode) - list(
            reversed(global_variables.pcode)).index(-1) - 1] = len(global_variables.pcode)

    elif act == 31:
        # Pour gérer le cas du if else
        jif_index = len(global_variables.pcode) - \
            list(reversed(global_variables.pcode)).index(-1) - 1
        global_variables.pcode.append('JMP')
        global_variables.pcode.append(-1)
        global_variables.pcode[jif_index] = len(
            global_variables.pcode)  # on commence par fermer le if

    elif act == 32:
        # Pour gérer la fermeture boucle while
        jif_index = len(global_variables.pcode) - \
            list(reversed(global_variables.pcode)).index(-1) - 1
        global_variables.pcode.append('JMP')
        global_variables.pcode.append(jif_index - 6)
        global_variables.pcode[jif_index] = len(global_variables.pcode)

    elif act == 33:
        # Pour ne pas executer le code la fonction au moment de sa lecture
        global_variables.pcode.append('JMP')
        global_variables.pcode.append(-1)

        global_variables.fonctions[global_variables.scanned['chaine']] = len(
            global_variables.pcode)
        """
        # On considere la fonction comme uen variable a part entiere
        if not global_variables.scanned['chaine'] in global_variables.table_memoire:
            global_variables.table_memoire[global_variables.scanned['chaine']] = len(list(global_variables.table_memoire.keys()))
        
        # On stocke dans la valeur de la fonction le CO de son debut
        global_variables.pcode.append('LDA')
        global_variables.pcode.append(global_variables.table_memoire[global_variables.scanned['chaine']])
        global_variables.pcode.append('LDC')
        global_variables.pcode.append(len(global_variables.pcode) + 2)
        global_variables.pcode.append('AFF')
        """
    elif act == 34:
        # Pour signifier le retour d'une fonction
        global_variables.pcode.append('RSR')
        # On ferme le jump
        global_variables.pcode[len(global_variables.pcode) - list(
            reversed(global_variables.pcode)).index(-1) - 1] = len(global_variables.pcode)

    elif act == 35:
        # Pour sauter vers une fonction
        # On charge directement l'adresse de saut depuis la memoire du programme
        global_variables.pcode.append('JSR')
        global_variables.pcode.append(
            global_variables.fonctions[global_variables.scanned['chaine']])
