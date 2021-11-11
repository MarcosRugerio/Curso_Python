#Funcion estatica que solo suma los valores definidos
def suma():
  num1 = 5
  num2 = 7
  print(num1+num2)

suma()

#Función que recibe parametros, para que en este caso sea sumado.
def suma_con_argumentos(num3,num4):
  resultado = num3+num4
  return resultado

print(suma_con_argumentos(10,43)) 
print(suma_con_argumentos(11232340,3))
print(suma_con_argumentos(10,1))

almacena_resultado=suma_con_argumentos(1984,1981)
print('El resultado almacenado es: ', almacena_resultado)