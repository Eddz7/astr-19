import numpy as np #import numpy library

#integers

i = 10 #integer
print("type(i) = ",type(i)) #print out the data type of i

a_i = np.zeros(i,dtype=int) #declare an array of ints
print("type(a_i) = ",type(a_i)) #will return an ndarray
print("type(a_i[0]) = ",type(a_i[0])) #will return int32
print("a_i.shape: ",a_i.shape)

#floats

x = 19.0 #floating point number
print("type(x) = ",type(x)) #print out the data type of x

y = 1.9e2 #float 190 in scientific notation
print("type(y) = ",type(y)) #print out the data type of y

z = np.zeros(i,dtype=float) #declare an array of floats
print("type(z) = ",type(z)) #print out the data type of z
print("type(z[0]) = ",type(z[0])) #print out data type of an element of z
print("z.shape: ",z.shape)