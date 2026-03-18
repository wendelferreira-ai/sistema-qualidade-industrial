# Sistema de Controle de Qualidade Industrial

Protótipo em Python para inspeção e controle de peças em linha de montagem industrial.

---

## Funcionalidades

| Opção | Descrição |
|-------|-----------|
| 1 | Cadastrar nova peça |
| 2 | Listar peças aprovadas/reprovadas |
| 3 | Remover peça cadastrada |
| 4 | Listar caixas fechadas |
| 5 | Gerar relatório final |
| 0 | Sair |

---

## Critérios de Qualidade

| Atributo    | Condição de Aprovação       |
|-------------|-----------------------------|
| Peso        | Entre **95g** e **105g**    |
| Cor         | **azul** ou **verde**       |
| Comprimento | Entre **10cm** e **20cm**   |

---

## Lógica de Caixas

- Peças **aprovadas** são inseridas automaticamente na caixa em aberto.
- Cada caixa comporta no máximo **10 peças**.
- Ao atingir a capacidade, a caixa é **fechada** e uma nova é iniciada.
- Peças **reprovadas** não entram em caixas.

---

## Como Rodar

### Pré-requisitos

- Python 3.8 ou superior instalado.

### Passo a Passo

```bash
# 1. Clone o repositório
git clone <URL_DO_REPOSITORIO>
cd <PASTA>

# 2. Execute
python sistema_qualidade.py
```

> **Windows:** se `python` não funcionar, tente `py sistema_qualidade.py`

---

## Exemplos de Entrada e Saída

### Peça Aprovada

```
Peso (g): 100
Cor: azul
Comprimento (cm): 15

Peca 1 APROVADA e adicionada na caixa atual (1/10)
```

### Peça Reprovada

```
Peso (g): 80
Cor: vermelho
Comprimento (cm): 25

Peca 2 REPROVADA:
  - Peso fora do intervalo (95g a 105g)
  - Cor invalida (aceitas: azul ou verde)
  - Comprimento fora do intervalo (10cm a 20cm)
```

### Fechamento Automático de Caixa

```
Peca 10 APROVADA e adicionada na caixa atual (10/10)
Caixa 1 fechada!
```

### Relatório Final

```
--- RELATORIO FINAL ---
Total de pecas: 12
Aprovadas: 10
Reprovadas: 2
Caixas utilizadas: 1

Motivos de reprovacao:
  ID 2: Peso fora do intervalo (95g a 105g), Cor invalida (aceitas: azul ou verde)
  ID 5: Comprimento fora do intervalo (10cm a 20cm)
```

---

## Estrutura do Projeto

```
.
├── sistema_qualidade.py   # código-fonte principal
└── README.md              # documentação
```

---

## Observações

- Sem dependências externas — usa apenas Python padrão.
- Dados ficam em memória durante a execução.
- IDs são gerados automaticamente.

---

## Autor

Trabalho de Faculdade — Automação Digital
Unifecaf — 2026
