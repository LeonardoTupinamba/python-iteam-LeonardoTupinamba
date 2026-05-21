# Explicação — Desafio 02 — Calculadora de IMC

**Aluno:** _(Leonardo Tupinambá)_
**Data:** _(19/05/2026)_

---

## O que meu programa faz

_(O meu programa calcula o IMC -Índice de Massa Corporal, ele solicita o nome da pessoa, o peso e a altura. E e seguida mostra o resultado do IMC)_

---

## Resposta à Pergunta Obrigatória

> Por que é necessário usar `float()` ao capturar peso e altura com `input()`? O que aconteceria se usássemos `int()` para a altura `1.75`?

_(A função `input()` sempre retorna uma "string" — texto puro, sem tipo numérico. Para fazer cálculos, é preciso converter esse texto para um número.)_

`int()` não sabe interpretar o ponto decimal — ele espera apenas dígitos (`0`–`9`). Como `"1.75"` contém um ponto, a conversão falha antes mesmo de o cálculo acontecer.

Peso e altura são grandezas "contínuas" (raramente valores redondos exatos), por isso `float()` é a escolha correta: ele aceita tanto `"86"` quanto `"86.5"` e `"1.75"` sem erros.

---

## Dificuldades encontradas

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_
