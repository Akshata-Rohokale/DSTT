## Name   -  Akshata Rohokale
## Reg No -  22-27-21
import math
import numpy as np
img1 = np.array([[1,2,3], [4,5,6],[1,4,6]])
img2 = np.array([[4,4,2], [5,3,1],[2,2,2,]])
lst1= img1.flatten()
lst2= img2.flatten()
lst1 = lst1.tolist()
lst2 = lst2.tolist()

### Mean Absolute Error ###
SAE=0
for i in range(0,len(lst1)):
    SAE+= abs(lst1[i]-lst2[i])
MAE= SAE/len(lst1)
print("MAE= ",MAE)

### Mean Square Error ###
SSE=0
for i in range(0,len(lst1)):
    SSE+= (lst1[i]-lst2[i])**2
MSE= SSE/len(lst1)
print("SSE= ",MSE)

### Root Mean Square Error ###
RMSE = MSE**0.5
print("RMSE= ", RMSE)

### Signal to Noise Ratio ###
Psignal = 0
for i in range(0,len(lst1)):
    Psignal+= (lst1[i])**2

Pnoise= 0
for i in range(0,len(lst2)):
    Pnoise+= (lst1[i]-lst2[i])**2

SNR= Psignal/Pnoise
print("SNR= ",SNR)

### Signal to Noise Ratio in dB ###
SNRdB = 10*math.log10(SNR)
print("SNR(dB)= ", SNRdB)



    
