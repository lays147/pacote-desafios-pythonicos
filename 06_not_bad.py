"""
06. not_bad

Dada uma string, encontre a primeira aparição das
substrings 'not' e 'bad'. Se 'bad' aparecer depois
de 'not', troque todo o trecho entre 'not' e 'bad'
por 'good' e retorne a string resultante.

Exemplo: 'The dinner is not that bad!' retorna 'The dinner is good!'
"""
import re

def find_index(s, word):
    lower = s.lower()
    find  = lower.find(word)
    rfind = lower.rfind(word)
    print(word, find, rfind)
    if find == rfind: 
        return find
    if find != -1 and rfind != -1: 
        return min(find,rfind)

def not_bad(s):
    # +++ SUA SOLUÇÃO +++
    # Usando find e manipulando a string
    # bad_idx = find_index(s, 'bad')
    # not_idx = find_index(s, 'not')
    # if bad_idx > not_idx :
    #     return s.replace(s[not_idx:bad_idx+3], 'good')
    # return s

    # Usango regex
    # reg = re.compile('(not.+bad)', re.IGNORECASE)
    # match = reg.search(s)
    # if match:
    #     return s.replace(s[match.start():match.end()], 'good')
    # return s

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
    test(not_bad, 'This movie is not so bad', 'This movie is good')
    test(not_bad, 'This dinner is not that bad!', 'This dinner is good!')
    test(not_bad, 'This tea is not hot', 'This tea is not hot')
    test(not_bad, "It's bad yet not", "It's bad yet not")
    test(not_bad, 'Not not bad', 'good')
    # Esse falha no regex, pois teria que pegar o grupo (Not bad) 
    # em vez disso da match entre o primeiro not e o ultimo bad
    test(not_bad, 'Not bad not bad', 'good not bad')
    # Esse falha na lógica comum, pois como trabalhamos com a 
    # primeira aparição da dupla not bad, a lógica segue com o menor
    # index de cada uma. Imagino que precisaria de tratar esse 
    # caso especial
    test(not_bad, 'bad not bad', 'bad good')