# Explicação — Desafio 03 — Sistema de Multas

**Aluno:** _(Leonardo Tupinambá)_
**Data:** _(20/05/2026)_

---

## O que meu programa faz

_(Recebe a velocidade do veículo e responde com uma mensagem "Boa viagem! Dirija com segurança" se a velocidade estiver abaixo do permitido, ou se estiver acima do permitido, responde com a seguinte mensagem: "Multado! Você excedeu o limite de 80km/h. Excesso: 20.0 km/h | Valor da multa: R$ 140.00". Ou seja, declara que foi multado e já indica o valor da multa. )_

---

## Resposta à Pergunta Obrigatória

> Por que usamos `elif` e não múltiplos `if` separados? Dê um exemplo concreto onde a diferença causaria um resultado errado.

\_(Quando usamos elif, as condições são mutuamente exclusivas : assim que uma delas é verdadeira, as demais são ignoradas . Com múltiplos if separados, todas as condições são avaliadas independentemente , uma por uma. Deve-se usar elif sempre que as condições forem alternativas (só uma deve valer por vez). Use if separados quando as condições forem independentes (mais de uma pode ser verdadeira ao mesmo tempo.))

Exemplo errado:
velocidade = 95

if velocidade > 80:
print("Multado!")

if velocidade > 60:
print("Boa viagem! Dirija com segurança") # ← executa também!

No caso acima, executaria os 2 if, ao usar elif, quando o if é true, ele pula o elif.

---

## Dificuldades encontradas

_(A compreensão do if e elif e suas diferenças. Bem como sua aplicação no código.)_
