from src import global_variables


class Node:
    def __init__(self, node_type):
        self.left = None
        self.right = None
        self.value = None
        self.COD = None
        self.aType = None
        self.ACT = None
        self.node_type = node_type


def gen_conc(node1, node2):
    new_node = Node("Conc")

    new_node.left = node1
    new_node.right = node2

    return new_node


def gen_union(node1, node2):
    new_node = Node("Union")

    new_node.left = node1
    new_node.right = node2

    return new_node


def gen_star(node):
    new_node = Node("Star")

    new_node.value = node
    return new_node


def gen_un(node):
    new_node = Node("UN")

    new_node.value = node
    return new_node


def gen_atom(code, act, aType):
    new_node = Node("Atom")

    new_node.COD = code
    new_node.ACT = act
    new_node.aType = aType

    return new_node


def gen_foret():
    global_variables.A.append(gen_conc(
        gen_star(
            gen_conc(
                gen_conc(
                    gen_conc(
                        gen_atom("N", 0, "NonTerminal"),
                        gen_atom("->", 0, "Terminal")
                    ),
                    gen_atom("E", 0, "NonTerminal")),
                gen_atom(",", 1, "Terminal"))),
        gen_atom(";", 0, "Terminal")
    ))

    global_variables.A.append(gen_atom("IDNTER", 2, "Terminal"))

    global_variables.A.append(gen_conc(
        gen_atom("T", 0, "NonTerminal"),
        gen_star(
            gen_conc(
                gen_atom("+", 0, "Terminal"),
                gen_atom("T", 3, "NonTerminal")
            )
        )
    ))

    global_variables.A.append(gen_conc(
        gen_atom("F", 0, "NonTerminal"),
        gen_star(
            gen_conc(
                gen_atom(".", 0, "Terminal"),
                gen_atom("F", 4, "NonTerminal")
            )
        )
    ))

    global_variables.A.append(gen_union(
        gen_union(
            gen_union(
                gen_conc(
                    gen_conc(
                        gen_atom("(", 0, "Terminal"),
                        gen_atom("E", 0, "NonTerminal")
                    ),
                    gen_atom(")", 0, "Terminal")
                ),
                gen_conc(
                    gen_conc(
                        gen_atom("[", 0, "Terminal"),
                        gen_atom("E", 0, "NonTerminal")
                    ),
                    gen_atom("]", 6, "Terminal")
                )
            ),
            gen_conc(
                gen_conc(
                    gen_atom("(/", 0, "Terminal"),
                    gen_atom("E", 0, "NonTerminal")
                ),
                gen_atom("/)", 7, "Terminal")
            )
        ),
        gen_union(
            gen_atom("IDNTER", 5, "Terminal"),
            gen_atom("ELTER", 5, "Terminal")
        )
    ))
