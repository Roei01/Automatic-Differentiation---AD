import numpy as np

#הגדרת פונקציה פשוטה
def f(x):
    return 1 / x

# חישוב נגזרת באמצעות הפרשים סופיים
def finite_difference(f, x, h=1e-5): #לא יעבוד נכון כי זה לחלק למספר ממש נמוך וייצור בעיה בדיוק 
    # חישוב הגדרת הנגזרת
    return (f(x + h) - f(x - h)) / (2 * h)

# השמת ערך לx לדוגמא
x = 2.0

# חישוב נגזרת לפי הפרשים סופיים
derivative_x = finite_difference(f, x)
print("Derivative of f(x) = 1/x using finite differences:", derivative_x)
