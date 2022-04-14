import re
import sys

from src.structures import gen_foret
from src.parser import parse_grammar, parse_program
from src.scanner import scan_g0, scan_gpl
from src.analyzer import analyze_g0, analyze_gpl
from src.interpreter import exec_code

import src.global_variables as global_variables

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage: dumas <path/to/file.dumas> <optional: grammar_name>")
        sys.exit(1)

    global_variables.init()

    gen_foret()

    parse_grammar(sys.argv[2] if len(sys.argv) == 3 else None)
    global_variables.scanned, global_variables.grammar = scan_g0(
        global_variables.grammar)
    result = analyze_g0(global_variables.A[0])

    if not result:
        print("Grammar is not correct")
        sys.exit(1)

    parse_program(sys.argv[1] if len(sys.argv) >=
                  2 else './examples/variables.dumas')

    global_variables.scanned, global_variables.program = scan_gpl(
        global_variables.program)
    result = analyze_gpl(global_variables.A[5])

    result = result and global_variables.scanned == None and len(
        global_variables.program) == 0

    if not result:
        print("Program is not correct")
        sys.exit(1)

    # print(global_variables.pcode)

    exec_code()

    # print(f'Grammaire correcte? {result}')
