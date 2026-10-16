import re

def tokeniser(expr):
    """'2 * (3 + 4)' -> ['2', '*', '(', '3', '+', '4', ')']"""
    return re.findall(r"\d+(?:\.\d+)?|[()+\-*/]", expr)


def chercher(tokens, operateurs, i, niveau=0):
    """Indice de l'opérateur le plus à droite hors parenthèses, ou -1 (récursif)."""
    if i < 0:
        return -1
    t = tokens[i]
    if t == ")":
        return chercher(tokens, operateurs, i - 1, niveau + 1)
    if t == "(":
        return chercher(tokens, operateurs, i - 1, niveau - 1)
    if niveau == 0 and t in operateurs:
        return i
    return chercher(tokens, operateurs, i - 1, niveau)


def prefixe(tokens):
    """Convertit une liste de tokens infixes en chaîne préfixée (récursif)."""
    # D'abord + et - (les moins prioritaires), sinon * et /
    i = chercher(tokens, "+-", len(tokens) - 1)
    if i == -1:
        i = chercher(tokens, "*/", len(tokens) - 1)

    if i != -1:
        return f"{tokens[i]} {prefixe(tokens[:i])} {prefixe(tokens[i + 1:])}"

    # Aucun opérateur hors parenthèses : soit (expression), soit un nombre
    if tokens[0] == "(":
        return prefixe(tokens[1:-1])
    return tokens[0]


def infixe_vers_prefixe(expr):
    return prefixe(tokeniser(expr))


print(infixe_vers_prefixe("2 * ( 3 + 4 )"))      # * 2 + 3 4
print(infixe_vers_prefixe("(1 + 2) * (3 - 4)"))  # * + 1 2 - 3 4
print(infixe_vers_prefixe("1 - 2 - 3"))          # - - 1 2 3
print(infixe_vers_prefixe("2 + 3 * 4"))          # + 2 * 3 4