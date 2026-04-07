import pytest
from operacoes.calculadora import divisao

def test_divisao_valores_validos():
    assert divisao(10, 2) == 5

def test_divisao_decimal():
    assert divisao(5, 2) == 2.5

def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        divisao(10, 0)