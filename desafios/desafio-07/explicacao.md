# Explicação — Desafio 07 — Bio-Calculadora

**Aluno:** _(Leonardo Tupinambá)_
**Data:** _(26/05/2026)_

---

## O que meu programa faz

O meu programa é uma CALCULADORA GEOMÉTRICA, que calcula a Área de um círculo, o Volume de uma esfera e a Hipotenusa de um triângulo.

---

## Resposta à Pergunta Obrigatória

> Por que separar as funções em um arquivo diferente do `solucao.py`? O que muda no projeto quando você tem 50 funções em vez de 3?

O problema do arquivo único
Com 3 funções, tudo num só arquivo parece confortável. Mas pense que não acontece quando o projeto cresce.

O que muda com 50 funções

1. Navegação vira pesadelo
   Com tudo em solucao.py, um arquivo de 3 funções tem mais ou menos 30 linhas. Com 50 funções, facilmente passa de 500 linhas. Encontrar hipotenusa()um arquivo assim exige Ctrl+F— em vez de simplesmente abrir funcoes_mat.py.
2. Conflitos em equipe
   Se duas pessoas editam o mesmo arquivo no mesmo tempo, o controle de versão (Git) gera conflito. Separado em módulos, a pessoa A edita funcoes_geometria.pyenquanto a pessoa B edita funcoes_estatistica.py— sem nenhum atrito.
3. Reutilização zero vs. reutilização total
   Python# SEM modularização — a função está presa dentro de solucao.py

# Outro projeto não consegue usá-la sem copiar e colar.

# COM modularização — qualquer projeto importa em uma linha:

from funcoes_mat import area_circulo
Copiar e colar código é a origem de bugs duplicados: você corrige em um lugar e esquece do outro. 4. Testes isolados
Módulos separados permitem testar cada função de forma independente, sem precisar executar o programa inteiro. Com 50 funções num arquivo só, um erro em qualquer pode impedir o carregamento de todos.

---

## Dificuldades encontradas

Todas possiveis, programa muito complexo para o meu nível de conhecimento, apenas com ajuda da IA consegui resolver. Mas foi importante para eu conhecer e perceber a importância da modularização e separação de código. E também serviu para eu entender a dinâmica de importação e edição independente.
