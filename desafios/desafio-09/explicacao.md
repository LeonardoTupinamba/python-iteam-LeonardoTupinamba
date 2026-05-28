# Explicação — Desafio 09 — Sistema de Frota

**Aluno:** _(Leonardo Tupinambá)_
**Data:** _(28/05/2026)_

---

## O que meu programa faz

Ele entrega um controle de frotas, e exibe a Marca do veículo, o ano do veículo, a quilometragem e a capacidade de carga no caso de caminhão e a potência no caso de moto.

---

## Resposta à Pergunta Obrigatória

> Por que `Caminhao` e `Moto` 'herdam de' `Veiculo` e não simplesmente repetem os atributos? O que você ganha e o que arrisca ao usar herança?

Por que `Caminhao` e `Moto` herdam de `Veiculo`?

Se `Caminhao` e `Moto` simplesmente repetissem os atributos de `Veiculo`, haveria "duplicação de código". Isso tornaria o sistema mais difícil de manter: qualquer mudança em como um veículo guarda ou exibe seus dados teria que ser replicada em todas as classes.

Ao usar "herança", os atributos e métodos comuns ficam centralizados na classe `Veiculo`. Assim:

- "Ganho:" reaproveitamento de código, consistência e facilidade de manutenção. Além disso, podemos tratar caminhões e motos como "veículos" em coleções ou funções genéricas.
- "Risco:" acoplamento maior. Se a classe base mudar de forma incompatível, todas as subclasses podem ser afetadas. Também é possível cair em hierarquias complexas e difíceis de entender.

Resumindo:
Herança evita repetição e facilita a extensão, mas deve ser usada com cuidado para não criar dependências rígidas ou hierarquias excessivamente complicadas.

---

## Dificuldades encontradas

Nessa atividade não tive tanta dificuldade, pois já compreendi o conceito de herança e sua importância, assim como, onde utilizar para melhorar o código.
