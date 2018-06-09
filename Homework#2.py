
# Name: Alison Jing Huang -- jing01ucsb@gmail.com
# ID: X111012
# Python for Data Analysis and Scientific Computing HW #2
import numpy as np
from numpy import matrix, array, random, min, max

# Create a matrix A with size (3,5) containing random numbers
# A= np.random.random(15)

A = random.random(15)
A = A.reshape(3,5)
A = matrix(A)

# Find the size and length of matrix A.
A.size
len(A)

# Resize(crop/slice) matrix A to size (3,4)
A = A[0:3,0:4]

# Find the transpose of matrix A and assign it to B
B = A.transpose()

# Find the minimum value in column 1 of matrix B(check the properties of a matrix -'B.min()')
B[:,1].min()

# Find the minimum and maximum values for the entire matrix A

A.min()
A.max()

# Create Vector X(an array) with 4 random numbers
X = array([random.random(4)])


# Create a function and pass vector X and matrix A in it
# In the new function multiply vector X and matrix A and assign the result
# to D.(note: you may get an error! - think why and fix it. Recall manipulation in class!)

def function_XA(a,b):
    return a*b.T

D = function_XA(X,A)

# Create a complex number Z with absolute and real parts !=0

Z = 200 + 60j

# Show its real and imaginary parts as well as its absolute value

print(Z.real)
print(Z.imag)
print(np.absolute(Z))

# Multiply result D with the absolute value of Z and record it to C

C = D * np.abs(Z)

# Convert matrix B from a matrix to a string and overwrite B

B = str(B)

# Display a text on the screen: 'Your Name is done with HW2'

name = "Alison Jing Huang"
print(name + " is done with HW2")
