nombre = str(input('cual es su nombre: '))
print ('Bienvenido ' + nombre.capitalize())
peso = int(input(' Por favor ingrese su Peso en Kilogramos: '))
estatura = int(input(' Por favor ingrese su Estatura en Centimetros: '))
imc = float(peso //((estatura/100)**2))

print (nombre.capitalize(), 'su Indice de masa corporal es: '+ str(imc))






