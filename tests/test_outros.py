from operacoes.calculadora import multiplicacao, subtracao, potencia

def test_multiplicacao():
    assert multiplicacao(2, 3) == 6

def test_subtracao():
    assert subtracao(5, 3) == 2

def test_potencia():
    assert potencia(2, 3) == 8
    assert potencia(2, 0) == 1