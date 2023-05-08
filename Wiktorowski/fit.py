import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from scipy.interpolate import CubicSpline

# wykres danych surowych
cars = [126, 134, 156, 124, 161, 129, 154, 150, 151, 153,
         123, 125, 116, 115, 139, 106, 98, 107, 108, 114, 104, 93, 119, 82]
x = [i + 1 for i in range(len(cars))]

# plt.scatter(x, cars)
# plt.show()


#wykres średniej ruchomej MA(5)
def ma(X, n):
    s = [np.mean(X[i:(i + n)]) for i in range(len(X) - n + 1)]
    return s

y2 = ma(cars, 5)
x2 = [i + 1 for i in range(len(y2))]


#interpolacja punktów

x_new = np.linspace(min(x2), max(x2), 1000)

f2 = make_interp_spline(x2, y2, k = 3, bc_type = 'natural') #cubic_spline


def fit(x_new, deg):
    a = np.polyfit(x2, y2, deg = deg)
    p = sum([a[i]*x_new**(deg - i) for i in range(len(a))])
    return p

# plt.plot(x_new, f2(x_new))
# plt.plot(x_new, fit(x_new, 3))
# plt.plot(x_new, fit(x_new, 4))
plt.plot(x_new, fit(x_new, 5))
# plt.plot(x_new, fit(x_new, 6))
# plt.plot(x_new, fit(x_new, 7))
plt.title('Cubic spline')
plt.scatter(x2, y2, color = 'red')
plt.show()