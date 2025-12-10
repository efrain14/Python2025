"""PRUEBELO USTED MISMO  6-5 
HAS UN DICCIONARIO QUE CONTENGA 3 RIOS PRINCIPALES Y EL PAIS POR EL QUE PASA CADA RIO, UN PAR CLAVE-VALOR, UTILICE UN BUCLE PARA IMPRIMIR UNA ORACION SOBRE CADA RIO, UTILICE UN BUCLE PRA IMPRIMIR EL NOMBRE DE CADA PAIS EN EL DICCIONARIO"""

rios_largos = {"orinoco" : "venezuela", 
                "amazonas" : "brazil",
                "nilo" : "egipto"}
for rio , pais in rios_largos.items():
    print(f"el rio {rio} es uno de los mas largos del mundo")
print("\n")
for rio in rios_largos:
    print(rio)
print("\n")
for rio, pais in rios_largos.items():
    print(pais)