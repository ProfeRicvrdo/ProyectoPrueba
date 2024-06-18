try:
    numerador =int(input('Ingresa un numero hola '));
    denominador =int(input('ingresa otro numero'));
    resultado = numerador / denominador
except ZeroDivisionError as e:
    print(f"Error: No se puede dividir por cero.")
else:
    print ('el resultado es : ', resultado)
