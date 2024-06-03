try:
    resultado = numerador / denominador
except ZeroDivisionError as e:
    print(f"Error: No se puede dividir por cero.")
    
else:
    print (resultado)

