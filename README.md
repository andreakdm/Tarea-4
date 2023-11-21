# Tarea-4
El código comienza importando las bibliotecas necesarias. Luego, genera los datos para la gráfica utilizando la función linspace de numpy para generar un conjunto de valores de x, y luego calcula los correspondientes valores de y.

A continuación, se crea la gráfica y se traza la curva con los datos generados. Se establecen los límites y las marcas de los ejes x e y.

Después, se añade una línea horizontal en y=40 utilizando la función axhline. Para encontrar el punto de intersección de esta línea con la curva, se define una función que representa la ecuación de la curva menos 40, y se utiliza la función fsolve de scipy para encontrar la raíz de esta función, que es el valor de x en el punto de intersección.

Finalmente, se añade una línea vertical en el punto de intersección utilizando la función axvline, y se marca el punto de intersección en la gráfica. Se añade una leyenda a la gráfica que incluye el valor del coeficiente de resistencia en el punto de intersección.

Para el segundo ejercicio de Regla de Cramer el programa toma como entrada los coeficientes y los términos independientes de las ecuaciones. Luego, calcula los determinantes de la matriz principal y las matrices obtenidas al reemplazar una columna por los términos independientes. Finalmente, divide estos determinantes para obtener las soluciones del sistema.
