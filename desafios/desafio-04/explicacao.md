# Explicação — Desafio 04 — Tabuada Personalizada

**Aluno:** _(Leonardo Tupinambá)_
**Data:** _(21/05/2026)_

---

## O que meu programa faz

_(O programa é um gerador de tabuada, que recebe um número do usuário e entrega a tabuada referente a aquele número.)_

---

## Resposta à Pergunta Obrigatória

> Para esse exercício, por que `for` com `range()` é preferível ao `while`? Em que cenário o `while` seria a escolha certa?

`for` com `range()` vs `while` — qual usar e quando?

Por que `for` é preferível para a tabuada?

A tabuada vai sempre de 1 a 10: quantidade de repetições conhecida de antemão.
O `for` com `range()` foi feito exatamente para isso — ele expressa a intenção de forma direta:

## O equivalente com `while` (mais verboso, mais frágil)

```python
i = 1                        # ← precisa criar manualmente
while i <= 10:
    print(f"{numero} x {i} = {numero * i}")
    i += 1                   # ← precisa incrementar manualmente
                             # esquecer isso = loop infinito
```

Três linhas de "infraestrutura" para fazer o que o `for` faz em uma.
Se o `i += 1` for esquecido, o programa trava para sempre.

Quando o `while` é a escolha certa?

Use `while` quando **não sabe quantas repetições serão necessárias** — o loop depende de uma condição que muda durante a execução.

Exemplo onde `while` é superior:

1. Repetir até o usuário digitar 0\*\* (usado neste próprio exercício):

```python
while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break

Não há como saber quantas tabuadas o usuário vai querer — o `for` não serve aqui.


## Dificuldades encontradas

_(Esse desafio é bem mais complexo, tive muita dificuldade e pedi ajuda para IA, mas antes de postar, procurei entender todo o código e o sistema.)_
```
