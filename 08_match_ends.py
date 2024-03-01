"""
08. match_ends

Dada uma lista de strings, retorne a contagem do número de
strings onde o comprimento da cadeia é 2 ou mais e o primeiro
e o último caracteres da cadeia são os mesmos.

PS: Python não possui o operador ++, porém += funciona.
"""

def match_ends(words):
    # +++ SUA SOLUÇÃO +++
    """
    SOLUÇÃO 2 - List comprehensions - Consiste em criar uma nova lista e adicionar os elementos que obedecem aquela regra
    accepted_words = []

    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            accepted_words.append(word)

    return len(accepted_words)
    """

    """count = 0

    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1

    return count"""
    """
    SOLUÇÃO 3 - Generator expressions
    """

    new_words = []

    def accepted_words(list_words):
        for word in list_words:
            if len(word) >= 2 and word[0] == word[-1]:
                yield word

    for word in accepted_words(words):
        new_words.append(word)

    return len(new_words)
# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(match_ends, ['aba', 'xyz', 'aa', 'x', 'bbb'], 3)
    test(match_ends, ['', 'x', 'xy', 'xyx', 'xx'], 2)
    test(match_ends, ['aaa', 'be', 'abc', 'hello'], 1)
