from src import global_variables


def exec_code():

    while global_variables.pcode[global_variables.CO] != 'STOP':
        # print(global_variables.CO, global_variables.pcode[global_variables.CO])
        interpret(global_variables.pcode[global_variables.CO])


def interpret(instruction):

    if instruction == 'LDA':
        global_variables.SPX += 1
        global_variables.pilex[global_variables.SPX] = global_variables.pcode[global_variables.CO + 1]
        global_variables.CO += 2

    elif instruction == 'LDV':
        global_variables.SPX += 1
        global_variables.pilex[global_variables.SPX] = global_variables.pilex[global_variables.pcode[global_variables.CO + 1]]
        global_variables.CO += 2

    elif instruction == 'LDC':
        global_variables.SPX += 1
        global_variables.pilex[global_variables.SPX] = global_variables.pcode[global_variables.CO + 1]
        global_variables.CO += 2

    elif instruction == 'AFF':
        global_variables.pilex[global_variables.pilex[global_variables.SPX - 1]
                               ] = global_variables.pilex[global_variables.SPX]
        # global_variables.SPX = global_variables.SPX - 2;
        global_variables.CO += 1

    elif instruction == 'JSR':
        # On empile l'emplacement de l'appel
        global_variables.pile_appels_fonction.append(global_variables.CO)
        # et on va a l'adresse de la fonction
        global_variables.CO = global_variables.pcode[global_variables.CO + 1]

    elif instruction == 'RSR':
        # On depile l'emplacement du dernier appel
        # et on passe a la case suivante
        destination = global_variables.pile_appels_fonction[-1] + 2
        global_variables.pile_appels_fonction = global_variables.pile_appels_fonction[:-1]

        global_variables.CO = destination

    elif instruction == 'JMP':
        global_variables.CO = global_variables.pcode[global_variables.CO + 1]

    elif instruction == 'JIF':
        if global_variables.pilex[global_variables.SPX] == 0:
            global_variables.CO = global_variables.pcode[global_variables.CO + 1]
        else:
            global_variables.CO += 2

        # global_variables.SPX -= 1

    elif instruction == 'ADD':
        global_variables.pilex[global_variables.SPX - 1] = global_variables.pilex[global_variables.SPX -
                                                                                  1] + global_variables.pilex[global_variables.SPX]
        global_variables.SPX -= 1
        global_variables.CO += 1

    elif instruction == 'MOINS':
        global_variables.pilex[global_variables.SPX - 1] = global_variables.pilex[global_variables.SPX -
                                                                                  1] - global_variables.pilex[global_variables.SPX]
        global_variables.SPX -= 1
        global_variables.CO += 1

    elif instruction == 'MULT':
        global_variables.pilex[global_variables.SPX - 1] = global_variables.pilex[global_variables.SPX -
                                                                                  1] * global_variables.pilex[global_variables.SPX]
        global_variables.SPX -= 1
        global_variables.CO += 1

    elif instruction == 'DIV':
        global_variables.pilex[global_variables.SPX - 1] = global_variables.pilex[global_variables.SPX -
                                                                                  1] / global_variables.pilex[global_variables.SPX]
        global_variables.SPX -= 1
        global_variables.CO += 1

    # Les opérateurs de comparaisons
    elif instruction == 'EQ':
        global_variables.pilex[global_variables.SPX + 1] = int(
            global_variables.pilex[global_variables.SPX - 1] == global_variables.pilex[global_variables.SPX])
        global_variables.SPX += 1
        # global_variables.SPX -= 1;
        global_variables.CO += 1

    elif instruction == 'SUP':
        global_variables.pilex[global_variables.SPX + 1] = int(
            global_variables.pilex[global_variables.SPX - 1] > global_variables.pilex[global_variables.SPX])
        global_variables.SPX += 1
        # global_variables.SPX -= 1;
        global_variables.CO += 1

    elif instruction == 'SUPE':
        global_variables.pilex[global_variables.SPX + 1] = int(
            global_variables.pilex[global_variables.SPX - 1] >= global_variables.pilex[global_variables.SPX])
        global_variables.SPX += 1
        # global_variables.SPX -= 1;
        global_variables.CO += 1

    elif instruction == 'INF':
        global_variables.pilex[global_variables.SPX + 1] = int(
            global_variables.pilex[global_variables.SPX - 1] < global_variables.pilex[global_variables.SPX])
        global_variables.SPX += 1
        # global_variables.SPX -= 1;
        global_variables.CO += 1

    elif instruction == 'INFE':
        global_variables.pilex[global_variables.SPX + 1] = int(
            global_variables.pilex[global_variables.SPX - 1] <= global_variables.pilex[global_variables.SPX])
        global_variables.SPX += 1
        # global_variables.SPX -= 1;
        global_variables.CO += 1

    elif instruction == 'DIFF':
        global_variables.pilex[global_variables.SPX + 1] = int(
            global_variables.pilex[global_variables.SPX - 1] != global_variables.pilex[global_variables.SPX])
        global_variables.SPX += 1
        # global_variables.SPX -= 1;
        global_variables.CO += 1

    elif instruction == 'WRT':
        print(global_variables.pilex[global_variables.SPX])  # WRT == print
        global_variables.CO += 1

    elif instruction == 'RD':
        keyboard_input = input()

        # Pour gérer le bon type dans l'input
        if keyboard_input.startswith('"') and keyboard_input.endswith('"'):
            keyboard_input = str(keyboard_input[1:-1])
        else:
            keyboard_input = float(
                keyboard_input) if '.' in keyboard_input else int(keyboard_input)

        # print(f'> {keyboard_input}')

        global_variables.pilex[global_variables.SPX + 1] = keyboard_input
        global_variables.SPX += 1
        global_variables.CO += 1
