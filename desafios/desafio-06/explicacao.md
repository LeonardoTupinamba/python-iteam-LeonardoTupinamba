# Explicação — Desafio 06 — Bio-Cadastro

**Aluno:** Leonardo Tupinambá
**Data:** _(25/05/2026)_

---

## O que meu programa faz

Pede para digitar o nome do colaborador(funcionário) e sua função e sair par encerrar, e ao encerrar, entrega a lista de funcionários e suas funções listadas.

---

## Resposta à Pergunta Obrigatória

> Por que usamos um **dicionário** para cada funcionário e não uma lista com dois itens como `["Ricardo", "Dev"]`? Qual é a desvantagem de `funcionario[0]` comparado a `funcionario["nome"]`?

Usamos um 'dicionário' para cada funcionário porque ele permite associar
diretamente uma 'chave semântica' ao valor. Assim, `funcionario["nome"]`
é muito mais legível e intuitivo do que `funcionario[0]`.

Se usássemos uma lista como `["Ricardo", "Dev"]`, precisaríamos lembrar
que o índice `0` corresponde ao nome e o índice `1` ao cargo. Isso torna
o código menos claro e mais propenso a erros, especialmente quando a
estrutura cresce ou novos atributos são adicionados.

Portanto, a desvantagem de `funcionario[0]` é a 'falta de significado':
o índice não diz nada sobre o que representa. Já `funcionario["nome"]`
torna explícito o propósito do dado, melhorando a legibilidade,
manutenção e evitando confusões.

---

## Dificuldades encontradas

_(De entender a diferença e qual usar para cada situação, mas estou praticando e lendo pra tenta entender)_
