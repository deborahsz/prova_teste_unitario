from operacoes.calculadora import soma

def test_soma_valores_validos():
    assert soma(2, 3) == 5

def test_soma_negativos():
    assert soma(-1, 1) == 0

def test_soma_zero():
    assert soma(0, 0) == 0