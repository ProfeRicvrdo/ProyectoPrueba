try:
    numerador =int(input('Ingresa un numero'));
    denominador =0;
    resultado = numerador / denominador
except ZeroDivisionError as e:
    print(f"Error: No se puede dividir por cero.")

else:
    print (resultado)