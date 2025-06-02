# 💰 Simulador de Troco — Algoritmo Guloso

*Projeto de Algoritmos Ambiciosos — Simulação interativa de troco com Pygame*

## 👥 Alunos
| Matrícula    | Nome                      |
|--------------|---------------------------|
| 22/2006641   | Davi de Aguiar Vieira     |
| 22/2006801   | Henrique Carvalho Neves   |

## 📝 Entregas
| Alogoritmos Ambiciosos |
|----------|
| [Apresentação]() 
---

## Sobre o projeto

Este é um simulador interativo de troco utilizando o **algoritmo guloso**. O usuário pode informar o valor da compra, o valor recebido e ajustar o estoque de moedas disponíveis. O sistema calcula automaticamente o troco ideal, considerando o estoque, e exibe o resultado na tela.

A interface gráfica foi desenvolvida em Python com a biblioteca **Pygame**.

## Requisitos

- Python 3.7 ou superior
- Pygame

### Instalando o Pygame

```bash
pip install pygame
```

> Recomenda-se utilizar um ambiente virtual (`venv`) para isolar as dependências.

## Como executar

Salve o arquivo [`trocador.py`](trocador.py) e execute:

```bash
python trocador.py
```

Certifique-se de estar na pasta onde o arquivo está localizado.

## Como usar

A interface permite:

- **Informar o valor da compra** e o **valor recebido** nos campos superiores.
- **Ajustar o estoque de moedas** disponíveis nos campos ao lado dos valores de cada moeda.
- **Clicar em "Calcular Troco"** para obter o troco ideal, considerando o estoque atual.
- O resultado do troco é exibido na tela, detalhando a quantidade de cada moeda utilizada.
- O estoque de moedas é atualizado automaticamente após cada operação de troco.

### Comandos

- **Clique nos campos de texto** para digitar valores.
- **Clique no botão verde "Calcular Troco"** para realizar o cálculo.
- **Ajuste o estoque de moedas** digitando nos campos ao lado de cada valor de moeda.

## Observações

- O algoritmo utilizado é guloso, sempre tentando usar as moedas de maior valor disponíveis.
- Caso não seja possível fornecer o troco com o estoque atual, uma mensagem de erro será exibida.