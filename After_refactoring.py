import autograd.numpy as np
from autograd import grad

#הגדרת פונקציה פשוטה
def f(x):
    return 1 / x

# חישוב הנגזרת לפי AD ......מה שזה עושה זה בעצם גוזר כל משתנה ומשתנה כפי שהראנו במחקר ומוצא לכל משתנה ומשתנה את הנגזרת שלו וככה עוקף את הבעיה שנוצרה בהפרשים הסופיים
grad_f = grad(f)

# השמת ערך לx לדוגמא
x = 2.0

# חישוב הנגזרת לפי AD
derivative_x = grad_f(x)
print("Derivative of f(x) = 1/x using AD:", derivative_x)
