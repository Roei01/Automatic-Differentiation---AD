import numpy as np

# פונקציה פשוטה: f(x) = 1/x
def f(x):
    return 1 / x

# חישוב נגזרת באמצעות הפרשים סופיים
def finite_difference(f, x, h=1e-5): #לא יעבוד נכון כי זה לחלק למספר ממש נמוך 
    # חישוב נגזרת עם הפרש קטן קדימה ואחורה
    return (f(x + h) - f(x - h)) / (2 * h)

# ערך לדוגמה
x = 2.0

# חישוב נגזרת באמצעות הפרשים סופיים
derivative_x = finite_difference(f, x)
print("Derivative of f(x) = 1/x using finite differences:", derivative_x)
