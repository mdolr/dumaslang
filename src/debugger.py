from src import global_variables

canvas = None


def imprim_canvas(canvas):
    res = ''

    for i in range(len(canvas)):
        for j in range(len(canvas[i])):
            res += canvas[i][j]
        res += '\n'

    return res


def arbre_canvas(node, coords=(0, 0)):
    global canvas

    if not canvas:
        canvas = [['-']]

    if node:
        x, y = coords[0], coords[1]

        if node.node_type == 'Conc' or node.node_type == 'Union':

            canvas[x].append('-')
            canvas[x].append('-')
            canvas[x].append(' ')
            canvas[x].append('.' if node.node_type == 'Conc' else '+')
            canvas[x].append(' ')
            canvas[x].append('-')
            canvas[x].append('-')
            canvas[x].append('|')

            y = len(canvas[x]) - 1

            filler = [' ' for k in range(y)]
            filler.append('|')

            canvas.insert(x + 1, filler.copy())
            canvas.insert(x + 1, filler.copy())
            canvas.insert(x, filler.copy())
            canvas.insert(x, filler.copy())

            x += 2

            # On commence par la droite
            # car sinon on va prepend dans notre array canvas
            # ce qui va faire bouger le x et tout foutre en l'air
            # quand on passe finalement a droite

            arbre_canvas(node.left, (x + 2, y))
            arbre_canvas(node.right, (x - 2, y))

        elif node.node_type == 'Star' or node.node_type == 'UN':
            canvas[x].append('-')
            canvas[x].append('-')
            canvas[x].append(' ')
            canvas[x].append('*' if node.node_type == 'Star' else '?')
            canvas[x].append(' ')

            y = len(canvas[x]) - 1

            arbre_canvas(node.value, (x, y))

        elif node.node_type == 'Atom':
            canvas[x].append('-')
            canvas[x].append('-')
            canvas[x].append(' ')

            if node.aType == 'Terminal':
                canvas[x].append('"')
                canvas[x].extend(list(node.COD))
                canvas[x].append('"')

            else:
                canvas[x].extend(list(node.COD))

    return canvas


def imprim_arbre(node):
    res_canvas = arbre_canvas(node)
    # print(res_canvas)
    print(imprim_canvas(canvas))
