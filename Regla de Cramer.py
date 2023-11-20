'''Dado un problema de 3 ecuaciones con 3 incógnitas tendremos una matriz A asociada al sistema de la forma:

a1 a2 a3 | y1

b1 b2 b3 | y2

c1 c2 c3 | y3

la regla de cramer dice lo siguiente:

reemplazamos a1 b1 c1 por y1 y2 y3 y esta será la matriz Ax1 x1=Det(Ax1)/Det(A)
y así con x2 y x3

entonces Det(A)=a1b2c3 + a3b1c2 + a2b3c1 - a1b3c2 - a2b1c3 - a3b2c1

Det(Ax1)=y1b2c3 + a3y2c2 + a2b3y3 - y1b3c2 - a2y2c3 - a3b2y3'''

a1 = 0.3
a2 = 0.52
a3 = 1
b1 = 0.5
b2 = 1
b3 = 1.9
c1 = 0.1
c2 = 0.3
c3 = 0.5
y1 = -0.01
y2 = 0.67
y3 = -0.44

x1 = ((y1 * b2 * c3) + (a3 * y2 * c2) + (a2 * b3 * y3) - (y1 * b3 * c2) - (a2 * y2 * c3) - (a3 * b2 * y3)) / ((a1 * b2 * c3) + (a3 * b1 * c2) + (a2 * b3 * c1) - (a1 * b3 * c2) - (a2 * b1 * c3) - (a3 * b2 * c1))
x2 = ((a1 * y2 * c3) + (a3 * b1 * y3) + (y1 * b3 * c1) - (a1 * b3 * y3) - (y1 * b1 * c3) - (a3 * y2 * c1)) / ((a1 * b2 * c3) + (a3 * b1 * c2) + (a2 * b3 * c1) - (a1 * b3 * c2) - (a2 * b1 * c3) - (a3 * b2 * c1))
x3 = ((a1 * b2 * y3) + (y1 * b1 * c2) + (a2 * y2 * c1) - (a1 * y2 * c2) - (a2 * b1 * y3) - (y1 * b2 * c1)) / ((a1 * b2 * c3) + (a3 * b1 * c2) + (a2 * b3 * c1) - (a1 * b3 * c2) - (a2 * b1 * c3) - (a3 * b2 * c1))
print("x1 es igual a", x1)
print("x2 es igual a", x2)
print("x3 es igual a", x3)

print("verificando si es correcto \n . \n . \n .")
print(a1 * x1 + a2 * x2 + a3 * x3, "=", y1)
print(b1 * x1 + b2 * x2 + b3 * x3, "=", y2)
print(c1 * x1 + c2 * x2 + c3 * x3, "=", y3)
