"""
08. match_ends

Dada uma lista de strings, retorne a contagem do número de
strings onde o comprimento da cadeia é 2 ou mais e o primeiro
e o último caracteres da cadeia são os mesmos.

PS: Python não possui o operador ++, porém += funciona.
"""


def match_ends(words):
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
    return count


def match_ends_lc(words):
    return len([word for word in words if len(word) >= 2 and word[0] == word[-1]])


def match_ends_ge(words):
    return len(list((word for word in words if len(word) >= 2 and word[0] == word[-1])))

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

    # list comprehension
    print('list comprehension')
    test(match_ends_lc, ['aba', 'xyz', 'aa', 'x', 'bbb'], 3)
    test(match_ends_lc, ['', 'x', 'xy', 'xyx', 'xx'], 2)
    test(match_ends_lc, ['aaa', 'be', 'abc', 'hello'], 1)

    # generation expressions
    print('generation expressions')
    test(match_ends_ge, ['aba', 'xyz', 'aa', 'x', 'bbb'], 3)
    test(match_ends_ge, ['', 'x', 'xy', 'xyx', 'xx'], 2)
    test(match_ends_ge, ['aaa', 'be', 'abc', 'hello'], 1)