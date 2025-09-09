def calcular_imc(peso,altura):
    return peso/altura**2
def categoria_imc(imc):
    if imc > 18.5:
        return"abaixo do peso"
    