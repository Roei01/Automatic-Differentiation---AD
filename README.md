# Automatic-Differentiation---AD


# חישוב נגזרות: השוואה בין שיטות

## מבוא
בפרויקט הזה, השווינו בין שתי שיטות לחישוב נגזרות של פונקציות מתמטיות:
1. **שיטת ההפרשים הסופיים** – שיטה מספרית לחישוב נגזרות על ידי קירוב ערכי הפונקציה בנקודות סמוכות.
2. **שיטת הנגזרות האוטומטיות (Automatic Differentiation - AD)** – שיטה אנליטית לחישוב נגזרות בצורה מדויקת וללא שגיאות עיגול.

## השיטות

### שיטת ההפרשים הסופיים

שיטת ההפרשים הסופיים משתמשת בהפרשים קטנים בין ערכי הפונקציה בנקודות סמוכות כדי לחשב את הנגזרת. השיטה עובדת לפי הנוסחה:

\[
f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}
\]

#### יתרונות:
- קלה ליישום.
- לא דורשת הבנה מעמיקה של מבנה הפונקציה.

#### חסרונות:
- תלות גבוהה בבחירת \( h \) (הפרש קטן).
- שגיאות עיגול משמעותיות כאשר \( h \) קטן מדי.
- עלולה להיות לא יציבה בפונקציות מורכבות.

#### קוד לדוגמה:
```python
import numpy as np

# פונקציה פשוטה: f(x) = 1/x
def f(x):
    return 1 / x

# חישוב נגזרת באמצעות הפרשים סופיים
def finite_difference(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

# ערך לדוגמה
x = 2.0
derivative_x = finite_difference(f, x)
print("Derivative of f(x) = 1/x using finite differences:", derivative_x)
שיטת הנגזרות האוטומטיות (AD)
שיטת הנגזרות האוטומטיות מבצעת חישוב אנליטי מדויק של הנגזרת על ידי פירוק הפונקציה לפעולות בסיסיות ושימוש בכלל השרשרת לחישוב נגזרות של פונקציות מורכבות.

יתרונות:
חישוב מדויק ללא תלות ב-
ℎ
h.
יכולה להתמודד עם פונקציות מורכבות בקלות.
מדויקת ויציבה גם לפונקציות מורכבות.
חסרונות:
דורשת שימוש בספריות חיצוניות כמו autograd.
דורשת הבנה עמוקה יותר של מבנה הפונקציה, אך ניתן לממש אותה בצורה גנרית.
קוד לדוגמה:
python
Copy code
import autograd.numpy as np
from autograd import grad

# פונקציה פשוטה: f(x) = 1/x
def f(x):
    return 1 / x

# חישוב הנגזרת באמצעות AD
grad_f = grad(f)

# ערך לדוגמה
x = 2.0
derivative_x = grad_f(x)
print("Derivative of f(x) = 1/x using AD:", derivative_x)
השוואת תוצאות
לדוגמה, עבור הפונקציה 
𝑓
(
𝑥
)
=
1
/
𝑥
f(x)=1/x בנקודה 
𝑥
=
2
x=2, השיטה המדויקת (AD) תחזיר תוצאה מדויקת של 
−
0.25
−0.25, בעוד שהשיטה המבוססת על הפרשים סופיים עלולה להחזיר ערכים קרובים אך לא מדויקים לחלוטין.

מסקנה
שיטת הנגזרות האוטומטיות (AD) מבטיחה דיוק גבוה וללא תלות בבחירת ערכים קטנים כמו 
ℎ
h, ולכן היא עדיפה במיוחד עבור פונקציות מורכבות או כאשר נדרש דיוק גבוה. מצד שני, שיטת ההפרשים הסופיים פשוטה יותר ליישום אך רגישה לשגיאות עיגול ותלויה בפרמטרים נומריים.

markdown
Copy code

### הסבר:

1. **מבנה `README.md`**: הקובץ מסביר בצורה כללית על שתי השיטות לחישוב נגזרות, ומספק דוגמאות קוד לשימוש בכל שיטה.
2. **יתרונות וחסרונות**: ישנה השוואה בין השיטות, הכוללת את היתרונות והחסרונות של כל שיטה.
3. **קוד לדוגמה**: כל שיטה כוללת דוגמה של קוד פשוט שניתן להריץ כדי לראות את ההבדלים.

### איך להשתמש:

1. תוכל לשים את הקובץ הזה בתיקיית הפרויקט שלך כקובץ `README.md`.
2. בעת פתיחת המאגר ב-GitHub או בתיקייה שלך, תוכל לראות את הקובץ שמסביר על שתי השיטות ועל הקוד שכתבת עבור כל אחת מהן.
3. תוכל להוסיף מידע נוסף או לשנות את הקובץ לפי הצורך.





