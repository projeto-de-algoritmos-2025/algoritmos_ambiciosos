# 💰 Simulador de Troco — Algoritmo Coin Change

*Projeto de Algoritmos Ambiciosos — Simulação interativa de troco com Pygame*

## 👥 Alunos
| Matrícula    | Nome                      |
|--------------|---------------------------|
| 22/2006641   | Davi de Aguiar Vieira     |
| 22/2006801   | Henrique Carvalho Neves   |

## 📝 Entregas
| Algoritmos Ambiciosos |
|-----------------------|
| [Apresentação]()      |

---

## Sobre o projeto

Este é um simulador interativo de troco utilizando o **algoritmo Coin Change**. O usuário pode informar o valor da compra, o valor recebido e ajustar o estoque de cédulas e moedas disponíveis. O sistema calcula automaticamente o troco ideal, considerando o estoque, e exibe o resultado na tela.

A interface gráfica foi desenvolvida em Python com as bibliotecas **Pygame** e **pygame_gui**.

## Requisitos

- Python 3.7 ou superior
- pygame
- pygame_gui

### Instalando as dependências

```bash
pip install pygame pygame_gui
```

> Recomenda-se utilizar um ambiente virtual (`venv`) para isolar as dependências.

## Como executar

O projeto está localizado na pasta `coin_change_simulator`. Para executar, utilize o arquivo `main.py`:

```bash
cd coin_change_simulator
python main.py
```

## Como usar

A interface permite:

- **Informar o valor da compra** e o **valor recebido** nos campos superiores.
- **Ajustar o estoque de cédulas e moedas** disponíveis nos campos ao lado dos valores de cada moeda.
- **Clicar em "Calcular Troco"** para obter o troco ideal, considerando o estoque atual.
- O resultado do troco é exibido na tela, detalhando a quantidade de cada cédula/moeda utilizada.
- O estoque é atualizado automaticamente após cada operação de troco.

### Comandos

- **Clique nos campos de texto** para digitar valores.
- **Clique no botão "Calcular Troco"** para realizar o cálculo.
- **Ajuste o estoque** digitando nos campos ao lado de cada valor de cédula/moeda.

## Observações

- O algoritmo utilizado é o Coin Change, sempre tentando usar as cédulas/moedas de maior valor disponíveis.
- Caso não seja possível fornecer o troco com o estoque atual, uma mensagem de erro será exibida.
- Os valores são informados em reais (R$), com suporte a centavos.
- O estoque de cada denominação pode ser alterado manualmente a qualquer momento.
