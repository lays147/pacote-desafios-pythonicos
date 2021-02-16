"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""
import math
def front_back(a, b):
    # +++ SUA SOLUÇÃO +++
    len_a = len(a)
    len_b = len(b)
    # Qual é a mais elegante? 
    # Concatenação na mão ou uso do zip?
    
    # split_a = (a[:math.ceil(len_a/2)], a[math.ceil(len_a/2):])
    # split_b = (b[:math.ceil(len_b/2)], b[math.ceil(len_b/2):])
    # return split_a[0]+split_b[0]+split_a[1]+split_b[1]
    
    # split_a = [a[:math.ceil(len_a/2)], a[math.ceil(len_a/2):]]
    # split_b = [b[:math.ceil(len_b/2)], b[math.ceil(len_b/2):]]
    # result = ''
    # for a,b in zip(split_a, split_b):
    #     result+= a + b
    # return result

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
