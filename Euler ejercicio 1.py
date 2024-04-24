# Importo librerias
import math
# Creo las variables necesarias
x0 = 1
y0 = 1
h = float(input("Ingrese de cuanto es el salto: "))
limite = 1
k = 1/(math.exp((1**2)/10))
i = 1+h
# Se escribe el desarrollo de la serie de euler
print(f'''
EDO dada: y'=0.2xy
      
Aproximacion con salto de {h}
      
Se usa la serie de euler:
      
y0+1 = y0 + {h}*(0.2*x0*y0)
      ''')

while limite <= 1.5:  # Aca establezco el limite de hasta que valor de x quiero llegar
    y = y0 + h*(0.2*x0*y0)
    x0 = x0+h
    y0 = y
    limite = limite + h
    # Determinacion del valor real
    valor_real = math.exp((i**2)/10)*k
    i += h
error_absoluto = abs(valor_real-y)
error_relativo = error_absoluto/valor_real
error_porcentual = error_relativo*100

print(f'''
Resolviendo la EDO tengo: y=e^((x^2)/10)) * 0.9                         
                 
Mis valores evaluados en el x = 1.5 son:                                          
La aproximacion en 1.5 es: {y}                                   
El valor real en 1.5 es: {valor_real}                            


CALCULO DEL ERROR                                                   
    
El error absoluto es: {error_absoluto}                          
El error relativo es: {error_relativo}                          
El error porcentual es: {error_porcentual} 
      ''')
