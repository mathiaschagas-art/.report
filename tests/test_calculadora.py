from app.calculadora import(
    soma,
    subtrair,
    multiplicar,
    calcular_desconto

)

def test_somar():
    resultado = soma(2,3)
    assert resultado == 5

def test_subtrair():
    resultado = subtrair(10,4)
    assert resultado == 6

def test_multiplicar():
    resultado = multiplicar(3,4)
    assert resultado == 12

def test_calcular_desconto():
    resultado = calcular_desconto(100, 0.1)
    assert resultado == 90

