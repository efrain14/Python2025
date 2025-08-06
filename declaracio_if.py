"""autos.py"""
carros = ["audi", "palio", "elantra", "ecosport", "bmw"]
for carro in carros:
    if carro == "bmw":
        print(carro.upper())
    else:
        print(carro.title())
