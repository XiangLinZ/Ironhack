#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

print(np.version.version)

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a1 = np.random.randint(0, 100, (2, 3, 5))

a2 = np.random.rand(2, 3, 5)

a3 = np.random.random_sample((2, 3, 5))

#4. Print a.

print (a1)
print (a2)
print (a3)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5, 2, 3))

#6. Print b.

print (b)

#7. Do a and b have the same size? How do you prove that in Python code?

print (a1.size == b.size)

#8. Are you able to add a and b? Why or why not?

# No, porque no tienen la misma forma
print (a1.shape, b.shape)

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = np.transpose(b,(1, 2, 0))

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = a1 + c
# c = np.add(a1, b) Usando numpy
print (d)
# Ahora sí podemos, porque tienen la misma forma.
print (a1.shape,c.shape)

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print (a1)
print (d) 
"""
La diferencia es simplemente que al array a1 le hemos sumado el array c, que está compuesta solo por unos,
así que el array resultante, d, es el mismo que a1 pero con todos los valores aumentados en uno...
(Por favor, no más de este tipo de pregunta que es como preguntar "¿Por qué te da 2 de la suma de 1 más 1?"😥😥😥)
"""


#12. Multiply a and c. Assign the result to e.

e = a1 * c
# e = np.multiply(a1, c) Usando numpy
print (e)

#13. Does e equal to a? Why or why not?

print (e == a1)
"""
Sí, porque aunque estemos multiplicando cada valor de un array con el valor del mismo objeto en la misma posición de otro array
resulta que el array c está solo compuesto por unos, y en una multiplicación por uno, el resultado siempre es sí mismo
porque... bueno... te lo imaginas... 🤡🤡🤡
"""

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)
print (d_max, d_min, d_mean)

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty((2, 3, 5))


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
# No soy fan de los "X", "y", "z", pero en arrays me es más fácil así porque me recuerda a las gráficas e mates
for z in range(d.shape[0]):
        for y in range(d.shape[1]):
                for x in range(d.shape[2]):
                        if (d[z, y, x] > d_min) & (d[z, y, x] < d_mean):
                                f[z, y, x] = 25
                        elif (d[z, y, x] > d_mean) & (d[z, y, x] < d_max):
                                f[z, y, x] = 75
                        elif d[z, y, x] == d_mean:
                                f[z, y, x] = 50
                        elif d[z, y, x] == d_min:
                                f[z, y, x] = 0
                        elif d[z, y, x] == d_max:
                                f[z, y, x] = 100
print (f)



"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
print (d)
print (f)
# Está guay, ha salido como debería

"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""
# Me voy a crear otro array y esas cosas para no solapar la F

g = np.empty((2, 3, 5), dtype = str)

for z in range(d.shape[0]):
        for y in range(d.shape[1]):
                for x in range(d.shape[2]):
                        if (d[z, y, x] > d_min) & (d[z, y, x] < d_mean):
                                g[z, y, x] = "B"
                        elif (d[z, y, x] > d_mean) & (d[z, y, x] < d_max):
                                g[z, y, x] = "D"
                        elif d[z, y, x] == d_mean:
                                g[z, y, x] = "C"
                        elif d[z, y, x] == d_min:
                                g[z, y, x] = "A"
                        elif d[z, y, x] == d_max:
                                g[z, y, x] = "E"

print (g)