"""
11. remove_adjacent

Dada uma lista de números, retorne uma lista onde todos elementos
adjacentes iguais são reduzidos a um único elemento.

Exemplo: [1, 2, 2, 3]
Irá retornar: [1, 2, 3]
"""


def remove_adjacent_a(nums):
    a = nums[:1]
    for item in nums[1:]:
        if item != a[-1]:
            a.append(item)
    return a


def remove_adjacent(nums):
    return [a for a, b in zip(nums, nums[1:]+[False]) if a != b]


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
    test(remove_adjacent, [1, 2, 2, 3], [1, 2, 3])
    test(remove_adjacent, [2, 2, 3, 3, 3], [2, 3])
    test(remove_adjacent, [], [])
    test(remove_adjacent, [2, 2, 3, 3, 3, 2, 2], [2, 3, 2])
    test(remove_adjacent_a, [1, 2, 2, 3], [1, 2, 3])
    test(remove_adjacent_a, [2, 2, 3, 3, 3], [2, 3])
    test(remove_adjacent_a, [], [])
    test(remove_adjacent_a, [2, 2, 3, 3, 3, 2, 2], [2, 3, 2])
