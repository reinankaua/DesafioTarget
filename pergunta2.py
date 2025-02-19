"""2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""

NUMERO_INFORMADO = 2

ultimo = 1
penultimo = 0
termo = 0

while True:
  termo = ultimo + penultimo
  penultimo = ultimo
  ultimo = termo

  if termo > NUMERO_INFORMADO:
    print("Não pertence a sequência")
    break
  elif termo == NUMERO_INFORMADO:
    print("Pertence a sequência")
    break