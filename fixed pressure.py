import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def func(x, b, a, c):
    return b*x/(np.log(a*x)-np.log(np.log(1 + 1.0/c)))

# experimental data
pres = 1.6e-1
dist = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3]
pd = np.multiply(dist, pres)
volt = [350.5, 334.25, 310.25, 294.5, 283.75, 275, 275.5, 281.25, 316.75, 434]

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
y_error = [1.91, 2.22, 2.63, 3.70, 2.06, 2.94, 0.58, 1.26, 0.5, 3.61]
plt.plot(pd_model, volt_model, color='red')
plt.scatter(pd, volt, s=5)
plt.errorbar(pd, volt, yerr=y_error, fmt='.')
plt.title('Paschen Curve of fixed pressure')
plt.xlabel('pd (mbar.cm)')
plt.ylabel('Breakdown Voltage(volts)')
plt.legend(['Fitted Curve', 'Data'])
plt.show()