from app.calculadora import(
    soma,
    subtrair,
    calcular_desconto

)

def test_somar():
    resultado = soma(2,3)
    assert resultado == 5

def test_subtrair():
    resultado = subtrair(10,4)
    assert resultado == 6

def test_calcular_desconto():
    resultado = calcular_desconto
    return resultado == 90


