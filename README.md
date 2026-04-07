Calculadora com Testes Unitários


*Sobre:

Esse projeto foi desenvolvido para praticar testes unitários utilizando Python e a biblioteca pytest.

A ideia foi implementar uma calculadora simples com algumas operações básicas e, em seguida, criar testes para verificar se essas funções estão funcionando corretamente.

---------------------------------

*Funcionalidades:

A calculadora possui as seguintes operações:

soma
subtração
multiplicação
divisão (com tratamento para divisão por zero)
fatorial (com validação para número negativo)
potência

------------------

*Regras de Negócio Testadas:

As regras de negócio definidas para a calculadora são as seguintes, com correspondência direta aos testes implementados:

- **Soma**: Deve somar dois números (inteiros ou flutuantes), funcionando corretamente com valores positivos, negativos e zero.
- **Subtração**: Deve subtrair o segundo número do primeiro, sem restrições adicionais além dos tipos numéricos.
- **Multiplicação**: Deve multiplicar dois números, retornando o produto correto.
- **Divisão**: Deve dividir o primeiro número pelo segundo, retornando um resultado decimal se necessário. Deve lançar um erro `ZeroDivisionError` caso o divisor seja zero, com a mensagem "divisao por zero".
- **Fatorial**: Deve calcular o fatorial de um número inteiro não-negativo (n >= 0), onde 0! = 1. Deve lançar um erro `ValueError` para números negativos, com a mensagem "numero negativo".
- **Potência**: Deve calcular a^b (base elevada ao expoente), incluindo casos como a^0 = 1.

Essas regras são validadas pelos testes unitários, que cobrem cenários válidos, inválidos e de limite para garantir o comportamento esperado.

---------------------

*Testes:
Print da ferramenta de cobertura de testes;
<img width="582" height="364" alt="Captura de tela 2026-04-07 195425" src="https://github.com/user-attachments/assets/424885b5-c6b6-4873-be77-a19acf4f4739" />


Os testes foram feitos utilizando pytest.

Foram criados testes para:

casos normais (valores positivos)
casos com números negativos
casos de erro (como divisão por zero e fatorial de número negativo)
alguns casos limite (como zero)

O objetivo foi garantir que as funções se comportem corretamente em diferentes situações.

---------------------------

*Estrutura:

operacoes/calculadora.py → funções da calculadora  
tests/ → arquivos de testes  
fixtures/ → dados auxiliares (se usado)  
requirements.txt → dependências  

--Como executar:

Instalar o pytest:

pip install -r requirements.txt

Rodar os testes:

python -m pytest

-------------------

*Observação:

Os testes foram pensados para cobrir diferentes cenários de uso, incluindo situações válidas e inválidas, seguindo o que foi visto em aula sobre testes unitários.

