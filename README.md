# 🧮 Calculadora em Python

Este projeto é uma **calculadora simples** desenvolvida em Python, utilizando uma classe para implementar as principais operações matemáticas.

## 🚀 Funcionalidades

A calculadora possui métodos para:
- ➕ Adição
- ➖ Subtração
- ✖️ Multiplicação
- ➗ Divisão (com tratamento para divisão por zero)
- 📊 Porcentagem
- 🔢 Potenciação

## 📂 Estrutura do Projeto

calculadora-python/
│── calculadora.py # Código principal da calculadora
│── README.md # Documentação do projeto

## ▶️ Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/Julliely/calculadora-python.git
   
2. Acesse a pasta do projeto:
      ```bash
      cd calculadora-python
      
3. Execute o arquivo principal:
      ```bash
      python calculadora.py
      
from calculadora import Calculadora

calc = Calculadora()

print(calc.somar(10, 5))       # 15
print(calc.subtrair(10, 5))    # 5
print(calc.multiplicar(10, 5)) # 50
print(calc.dividir(10, 5))     # 2.0
print(calc.porcentagem(50, 10))# 5.0
print(calc.potencia(2, 3))     # 8

Tecnologias Utilizadas

Python 3.x

✨ Autor

Projeto desenvolvido por Julliely
