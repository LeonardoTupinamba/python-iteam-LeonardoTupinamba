# Explicação — Desafio 08 — Banco Digital

**Aluno:** _(Leonardo Tupinambá)_
**Data:** _(28/05/2026)_

---

## O que meu programa faz

_(Descreva em suas palavras o que cada parte do código faz.)_

---

## Resposta à Pergunta Obrigatória

> Por que `saldo` deve ser um **atributo da instância** (`self.saldo`) e não uma variável comum dentro do método? O que mudaria no comportamento do programa?

## Por que `saldo` deve ser um atributo da instância (`self.saldo`)?

Se `saldo` fosse apenas uma variável comum dentro de um método, ele existiria (somente durante a execução daquele método) e seria descartado ao final. Isso significaria que cada chamada a `depositar` ou `sacar` começaria "do zero", sem lembrar o histórico anterior.

Ao usar `self.saldo`, o valor fica armazenado (na instância do objeto) e persiste entre chamadas de métodos. Assim, cada operação altera o mesmo estado interno da conta, permitindo que o programa acompanhe corretamente o saldo ao longo do tempo.

Resumindo:

- `saldo` como variável local → não guarda estado, sempre reinicia.
- `self.saldo` como atributo da instância → mantém o saldo atualizado e consistente entre operações.

---

## Dificuldades encontradas

Infelizmente, muita dificuldade, ainda não consigo construir o código sozinho, estou usando ajuda de IA, mas estou tentando entender o que está sendo feito e aprendendo a ler o código.
