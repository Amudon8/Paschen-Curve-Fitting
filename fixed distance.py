import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def func(x, b, c):
    return x*b/(c + np.log(x))


# experimental data
pres = [9.7e-2, 1.2e-1, 1.4e-1, 1.6e-1, 1.8e-1, 2.0e-1, 2.2e-1, 2.4e-1, 2.8e-1, 3.5e-1, 4.1e-1]
dist = 10
pd = np.multiply(dist, pres)
volt = [428, 354.5, 356.75, 327.75, 336.5, 339.25, 341.25, 334.25, 357, 393.75, 425.5]

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
plt.title('Paschen Curve of fixed distance')
plt.xlabel('pd (mbar.cm)')
plt.ylabel('Breakdown Voltage(volts)')
plt.legend(['Obtimised parameter','Graph parameter', 'Data'])
plt.show()