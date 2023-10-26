import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def func(x, b, c):
    return x*b/(c + np.log(x))

# experimental data
pres = 1.6e-1
dist = [9, 8, 7, 6, 5, 4, 3]
pd = np.multiply(dist, pres)
volt = [294.5, 283.75, 275, 275.5, 281.25, 316.75, 435]

# finding optimised B and C
popt, poct = curve_fit(func, pd, volt)

# plotting the curve fitting
b_opt, c_opt = popt
pd_model = np.linspace(min(pd), max(pd), 100)
volt_model = func(pd_model, b_opt, c_opt)

# finding pd_min and v_min from the optimised function graph
v_min = min(volt_model)
volt_model_l = volt_model.tolist()
index = volt_model_l.index(v_min)

pd_min = pd_model[index]

# the constant b given by v_min/pd_min
b = v_min/(pd_min)
c = 1 - np.log(pd_min)
volt_graph = func(pd_model, b, c)

u_argon = 15.77
print('The ionization energy of argon is ', u_argon, ' eV')
print('The value of B is\f', b_opt)

a_opt = b_opt/u_argon
print('The value of A is', a_opt)

gamma_opt = 1/(np.exp(a_opt/np.exp(c_opt))-1)
print('The value of gamma is ', gamma_opt)

plt.plot(pd_model, volt_model, color='r')
plt.plot(pd_model, volt_graph, color='green')
plt.scatter(pd, volt, s=5)
plt.title('Paschen Curve of fixed pressure')
plt.xlabel('pd (mbar.cm)')
plt.ylabel('Breakdown Voltage(volts)')
plt.legend(['Obtimised parameter','Graph parameter', 'Data'])
plt.show()