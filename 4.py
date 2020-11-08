import numpy as np
import matplotlib.pyplot as plt

I = [0.5, 1.0, 1.5]
U2C = [0.65, 1.30, 1.98]
U4C = [0.01, 0.03, 0.04]
U2A = [1.12, 2.19, 3.25]
U4A = [0.025, 0.05, 0.08]

U2C_fit = np.polyfit(I, U2C, 1)
U4C_fit = np.polyfit(I, U4C, 1)
U2A_fit = np.polyfit(I, U2A, 1)
U4A_fit = np.polyfit(I, U4A, 1)
R2C = np.zeros(3)
R4C = np.zeros(3)
R2A = np.zeros(3)
R4A = np.zeros(3)

for i in range(len(R2C)): 
	R2C[i] = U2C[i]/I[i]
	R4C[i] = U4C[i]/I[i]
	R2A[i] = U2A[i]/I[i]
	R4A[i] = U4A[i]/I[i]
res_2C = 0
res_4C = 0
res_2A = 0
res_4A = 0

for i in range(len(R2C)): 
	res_2C += R2C[i]
	res_4C += R4C[i]
	res_2A += R2A[i]
	res_4A += R4A[i]
res_2C = res_2C/3
res_4C = res_4C/3
res_2A = res_2A/3
res_4A = res_4A/3
print(R2C)
print(R4C)
print(R2A)
print(R4A)
print(res_2C)
print(res_4C)
print(res_2A)
print(res_4A)


