import numpy as np
m = int(input("satır"))
n = int(input("sütun"))
a = m * n 

mata =np.arange(1,a+1).reshape(m,n)
matb =np.arange(1,a+1).reshape(m,n)
matc = np.zeros((m,n)).reshape(m,n)


for i in range(m):
    for j in range(n):
        matc[i,j] = mata[i,j]+matb[i,j]
        
print(matc[m,n])    