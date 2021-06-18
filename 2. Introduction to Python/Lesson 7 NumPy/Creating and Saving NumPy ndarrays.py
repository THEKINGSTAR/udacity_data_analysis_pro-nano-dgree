import numpy as np

x =np.array([1,2,3,4,5])
print(x)
print(type(x))

print(x.dtype)
print(x.shape)



print("#"*10)



y = np.array([[1, 2, 3, 4], [6, 7, 8, 9], [6, 7, 8, 9], [6, 7, 8, 9]])

print(y)
print(y.shape)
print(y.size)


print("#"*10)



s=np.array(["hello","world"])
print(s)
print(s.dtype)

print("#"*10)

si = np.array(["hello", "world",1,3,"phton"])
print(si)
print(si.dtype)

print("#"*10)

x = np.array([1.5,3,5,3.4])
print(x)
print('dtype',x.dtype)

print("#"*10)

x = np.array([1.5,3,5,3.4],dtype=np.int64)
print(x)
print('dtype',x.dtype)

print("#"*10)



x =np.array([1,2,4,5,6,7])
np.save("numpy_array",x)
print("#"*10)

y = np.load("numpy_array.npy")
print("Loaded array : ",y)
