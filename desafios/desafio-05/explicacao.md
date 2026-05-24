# Explicação — Desafio 05 — Gerenciador de Compras

**Aluno:** _(Leonardo Tupinambá)_
**Data:** _(24/05/2026)_

---

## O que meu programa faz

Pede pra digitar o nome do produto e vai adicionando na lista até digitar "fim", e quando isso acontece, ele mostra a lista dos produtos digitados.

---

## Resposta à Pergunta Obrigatória

> Por que usamos uma **lista** e não uma **tupla** para essa lista de compras? O que mudaria no comportamento do programa se tentássemos usar tupla?

Diferença prática entre lista e tupla
Lista (list): é mutável, ou seja, podemos adicionar, remover ou alterar elementos depois de criada.

Tupla (tuple): é imutável, não permite mudanças após a criação.

No caso da lista de compras:
Usamos lista porque queremos adicionar produtos dinamicamente conforme o usuário digita.

O método .append() só funciona em listas, já que elas aceitam modificações.

---

## Dificuldades encontradas

Desenvolver o código, entender a diferença entre lista e tupla e qual usar.
