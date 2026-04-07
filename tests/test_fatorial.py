import pytest
from operacoes.calculadora import fatorial

def test_fatorial_valido():
    assert fatorial(5) == 120

def test_fatorial_zero():
    assert fatorial(0) == 1

def test_fatorial_negativo():
    with pytest.raises(ValueError):
        fatorial(-1)