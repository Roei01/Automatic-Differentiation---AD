import autograd.numpy as np
from autograd import grad

# פונקציה פשוטה: f(x) = 1/x
def f(x):
    return 1 / x

# חישוב הנגזרת באמצעות AD
grad_f = grad(f)

# ערך לדוגמה
x = 2.0

# חישוב הנגזרת באמצעות AD
derivative_x = grad_f(x)
print("Derivative of f(x) = 1/x using AD:", derivative_x)
