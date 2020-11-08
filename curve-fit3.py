import numpy as np
import matplotlib.pyplot as plt

U = [2.25, 3.43, 5.72, 9.10, 21.76]
R = [1, 1.5, 2.5, 4, 10]
I = np.zeros(len(R))
for i in range(len(R)): 
	I[i] = U[i]/R[i]
print(I)
plt.scatter(I, U)
plt.title("Data from experiment")
plt.xlabel("Current in mA")
plt.ylabel("Voltage in mV")

plt.show()

fit = np.polyfit([2.25, 2.28666667],[2.25, 3.43], 1)
print(fit[0])
print(fit[1])
def line(a, b, t): 
	return a*t+b
current = np.linspace(0, 25, 100)
line_fit = np.zeros(len(current))
for i in range(len(line_fit)): 
	line_fit[i] = line(fit[0],fit[1],current[i])

fig = plt.figure(figsize=(8,8))
plt.title("Fitted line and usable data.")
plt.scatter([2.25, 2.2866667], [2.25, 3.43])
plt.plot(current, line_fit)
plt.legend(["Fitted line: y=32.18x-70.16", "Scatterplot of points that made sense (two points)"])
plt.xlabel("Current in mA")
plt.ylabel("Voltage in mV")
plt.show()
