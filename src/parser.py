from src import global_variables


def parse_grammar(grammar_name):
    separator = ' '
    global_variables.grammar = ''

    if grammar_name is None or len(grammar_name) == 0:
        grammar_name = 'dumas'

    # Open file ../global_variables.grammar/dumas.txt
    with open(f'./grammars/{grammar_name}.txt', 'r') as f:
        global_variables.grammar = f.read()

    global_variables.grammar = global_variables.grammar.replace(
        '\n', ' ').split(separator)
    global_variables.grammar = [
        x for x in global_variables.grammar if x != ' ' and x != '']

    if len(global_variables.grammar[0]) == 0:
        global_variables.grammar = global_variables.grammar[1:]

    if len(global_variables.grammar[-1]) == 0:
        global_variables.grammar = global_variables.grammar[:-1]


def parse_program(path):
    separator = ' '
    global_variables.program = ''

    # Open file at path
    with open(f'./{path}', 'r') as f:
        global_variables.program = f.read()

    # Pour pouvoir écrire sur plusieurs lignes
    global_variables.program = global_variables.program.replace('\n', ' ')

    # Pour regrouper les strings avec des espaces ex: "salut comment ça va"
    temp_program = global_variables.program.split('"').copy()
    global_variables.program = []

    for i in range(len(temp_program)):
        if i % 2 == 0:
            global_variables.program.extend(temp_program[i].split(separator))
        else:
            global_variables.program.append('"' + temp_program[i] + '"')

    temp_program = []

    # Pour virer des espaces en trop
    global_variables.program = [
        x for x in global_variables.program if x != ' ' and x != '']

    if len(global_variables.program[0]) == 0:
        global_variables.program = global_variables.program[1:]

    if len(global_variables.program[-1]) == 0:
        global_variables.program = global_variables.program[:-1]
