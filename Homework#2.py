#1. Include a section line with your name:

# Name: Alison Jing Huang -- jing01ucsb@gmail.com
# ID: X111012
# Python for Data Analysis and Scientific Computing HW #2

import numpy as np
from numpy import matrix, array, random, min, max

#2. Create a matrix A with size (3,5) containing random numbers
# A= np.random.random(15)

A = random.random(15)
A = A.reshape(3,5)
A = matrix(A)

#3.  Find the size and length of matrix A.
A.size
len(A)

#4. Resize(crop/slice) matrix A to size (3,4)
A = A[0:3,0:4]

#5.  Find the transpose of matrix A and assign it to B
B = A.transpose()

#6.  Find the minimum value in column 1 of matrix B(check the properties of a matrix -'B.min()')
B[:,1].min()

#7. Find the minimum and maximum values for the entire matrix A

A.min()
A.max()

# Create Vector X(an array) with 4 random numbers
X = array([random.random(4)])


#8. Create a function and pass vector X and matrix A in it
# In the new function multiply vector X and matrix A and assign the result
# to D.(note: you may get an error! - think why and fix it. Recall manipulation in class!)

def function_XA(a,b):
    return a*b.T

D = function_XA(X,A)

#9. Create a complex number Z with absolute and real parts !=0

Z = 200 + 60j

#10, 11, 12.  Show its real and imaginary parts as well as its absolute value

print(Z.real)
print(Z.imag)
print(np.absolute(Z))

#13.  Multiply result D with the absolute value of Z and record it to C

C = D * np.abs(Z)

#14.  Convert matrix B from a matrix to a string and overwrite B

B = str(B)

#15. Display a text on the screen: 'Your Name is done with HW2'

name = "Alison Jing Huang"
print(name + " is done with HW2")

#16. Organize your code: use each line from this assignment as a comment line before each step
#17. Save all steps as a script in a .py file
#18. Email your Github link to me including your .py file + screenshots of your running code no later than midnight on Saturday Jun.09.



