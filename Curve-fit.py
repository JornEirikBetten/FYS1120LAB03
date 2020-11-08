import numpy as np
import matplotlib.pyplot as plt


t = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220]
V = [8.963, 7.1, 5.6, 4.4, 3.5, 2.72, 2.17, 1.72, 1.36, 1.07, .85, .67]
natV = np.zeros(len(t))
for i in range(len(V)): 
	natV[i] = np.log(V[i])
	


print(natV)	
lin_approx = np.polyfit(t, natV, 1)
poly = np.poly1d(lin_approx)

print(poly)
print(lin_approx)
print(lin_approx[0])
print(lin_approx[1])

def line(a, b, t): 
	return a*t + b
line_vals = np.zeros(len(t))
for i in range(len(t)): 
	line_vals[i] = line(lin_approx[0],lin_approx[1], t[i])

fig1 = plt.figure(figsize=(8,8))
plt.title("Fitted line of the natural log of voltage as a function of time")
plt.scatter(t, natV)
plt.plot(t, line_vals, 'r')
plt.legend(["Fitted line: y=-0.01179135x+2.19206189", "Values of measurements"])
plt.xlabel("Time in seconds")
plt.ylabel("The natural log of the voltage")
plt.show()

I = [17.039, 12.346, 8.678, 7.270, 5.847]
U = [373.4, 269.82, 189.27, 158.76, 127.64]
current = np.linspace(0,20, 100)
line_fit = np.polyfit(I, U, 1)
voltage_fit = np.zeros(len(current))
for i in range(len(current)): 
	voltage_fit[i] = line(line_fit[0], line_fit[1], current[i])
print(line_fit[0])
print(line_fit[1])
fig2 = plt.figure(figsize=(8,8))
plt.title("Scatterplot and fitted line of the voltage against the current")
plt.scatter(I, U)
plt.plot(current, voltage_fit)
plt.legend(["Fitted line: y=21.959703893401624x - 1.001529052859018 ", "Values of measurement"])
plt.xlabel("Current in mA") 
plt.ylabel("Voltage in mV") 
plt.show()
