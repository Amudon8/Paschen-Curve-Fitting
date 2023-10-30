import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# experimental data
pres = [9.7e-2, 1.2e-1, 1.4e-1, 1.6e-1, 1.8e-1, 2.0e-1, 2.2e-1, 2.4e-1, 2.8e-1, 3.5e-1, 4.1e-1]
dist = 10
pd = np.multiply(dist, pres)
volt = [428, 354.5, 356.75, 327.75, 336.5, 339.25, 341.25, 334.25, 357, 393.75, 425.5]


def func(x, b, a, c):
    return b*x/(np.log(a*x)-np.log(np.log(1 + 1.0/c)))


# finding optimised B and C
popt, poct = curve_fit(func, pd, volt, p0=[300,20,0.02])
print(popt)
# the fitted curve
pd_model = np.linspace(min(pd), max(pd), 100)
volt_model = func(pd_model, popt[0], popt[1], popt[2])

# finding pd_min and v_min from the optimised function graph
v_min = min(volt_model)
volt_model_l = volt_model.tolist()
index = volt_model_l.index(v_min)
pd_min = pd_model[index]

b_graph = v_min/pd_min
print(b_graph)
a_graph = b_graph/15.76
print(a_graph)
gamma = 1/(np.exp(a_graph*pd_min/2.72)-1)
print(gamma)

# standard deviation
y_error =[9.34, 6.45, 7.59, 3.20, 2.38, 0.5, 2.06, 2.63, 3.16, 0.96, 2.64]
plt.plot(pd_model, volt_model, color='red')
plt.scatter(pd, volt, s=5)
plt.errorbar(pd, volt, yerr=y_error, fmt='.')
plt.title('Paschen Curve of fixed Distance')
plt.xlabel('pd (mbar.cm)')
plt.ylabel('Breakdown Voltage(volts)')
plt.legend(['Fitted Curve', 'Data'])
plt.show()
