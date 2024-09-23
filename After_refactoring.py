import numpy as np

# פונקציה כללית לחישוב הנגזרת לפי-Forward Mode AD
def forward_mode_ad(f, x, var_idx):
    n = len(x)
    
    # יצירת משתנה הנגזרות
    dot_x = np.zeros(n)
    dot_x[var_idx] = 1  # מגדירים את הנגזרת של המשתנה המבוקש ל-1
    
    # חישוב ערך הפונקציה
    y = f(x)
    
    # חישוב הערך הביניים והנגזרת בהתאם למשתנה הנבחר
    x1, x2, x3 = x
    if var_idx == 0:
        dot_y = dot_x[0] * x2
    elif var_idx == 1:
        dot_y = dot_x[1] * x1 + np.cos(x2 * x3) * dot_x[1] * x3
    elif var_idx == 2:
        dot_y = np.cos(x2 * x3) * x2 * dot_x[2]
    
    return y, dot_y

# פונקציה לדוגמה: f(x) = x1 * x2 + sin(x2 * x3)
def f(x):
    x1, x2, x3 = x
    return x1 * x2 + np.sin(x2 * x3)

# פונקציה כללית לחישוב הנגזרות לכל משתנה
def compute_derivatives(f, x):
    n = len(x)
    derivatives = {}
    
    # חישוב הנגזרת עבור כל משתנה
    for var_idx in range(n):
        _, derivative = forward_mode_ad(f, x, var_idx)
        derivatives[f"x{var_idx+1}"] = derivative
    
    return derivatives

# ערכים לדוגמה
x = [2.0, 3.0, 4.0]

# חישוב הנגזרות
derivatives = compute_derivatives(f, x)
print("Value of f(x):", f(x))
print("Derivatives:", derivatives)
