import numpy as np

# פונקציה לחישוב f(x) = x1 * x2 + sin(x2 * x3)
def f(x):
    x1, x2, x3 = x
    return x1 * x2 + np.sin(x2 * x3)

# חישוב הנגזרת הראשונה של f ביחס ל-x1
def grad_f_x1(x):
    x1, x2, x3 = x
    return x2

# חישוב הנגזרת הראשונה של f ביחס ל-x2
def grad_f_x2(x):
    x1, x2, x3 = x
    return x1 + np.cos(x2 * x3) * x3

# חישוב הנגזרת הראשונה של f ביחס ל-x3
def grad_f_x3(x):
    x1, x2, x3 = x
    return np.cos(x2 * x3) * x2

# בדיקת פונקציה והנגזרות
x = [2.0, 3.0, 4.0]
print("Value of f(x):", f(x))
print("Derivative with respect to x1:", grad_f_x1(x))
print("Derivative with respect to x2:", grad_f_x2(x))
print("Derivative with respect to x3:", grad_f_x3(x))
