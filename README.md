# oops-in-python
This repository contains **basic to advanced examples** of Object-Oriented Programming (OOP) concepts implemented in Python. Each concept is explained with beginner-friendly Python code and clear comments.

oops-in-python/
├── 01_constructor_examples/
│ No. | Program Description |
|-----|---------------------|
| 1.  | Create student class and display name & roll number |
| 2.  | Calculate area of a triangle |
| 3.  | Check if a number is even or odd |
| 4.  | Constructor with default argument |
| 5.  | Sum of two numbers |
| 6.  | Find square of a number |
| 7.  | Store and print employee data |
| 8.  | Convert Celsius to Fahrenheit |
| 9.  | Accept 3 subject marks and calculate total |
| 10. | Check voting eligibility using age |

├── 02_inheritance_examples



├── 03_encapsulation_examples
### 1. 🌡️ Temperature Sensor
- Class: `TemperatureSensor`
- Private: `__celsius`
- Allow values only between `-50` and `150`
- Getter: returns Celsius & Fahrenheit using `F = C × 9/5 + 32`
- ❗ Bonus: Add temperature range error

---

### 2. 📧 Email Validator
- Class: `Employee`
- Private: `__email`
- Conditions:
  - Must contain `@`
  - Must end with `.com`
- Invalid emails are replaced with `"invalid@invalid.com"`
- ❗ Bonus: No regex used — only string methods

---

### 3. 🧮 Quiz Score Tracker
- Class: `Quiz`
- Private: `__scores` (list)
- Only allow scores from 0 to 10
- Getter: show all scores
- Method: `average()` returns average of scores
- ❗ Bonus: Encapsulation on mutable lists

---

### 4. 🚗 Vehicle Speed Control
- Class: `Vehicle`
- Private: `__speed`
- Speed range: `0–180`
- If speed > 120 → print “Overspeeding!”
- Method: `increase_speed(value)`
- ❗ Bonus: Use setter logic from method

---

### 5. 🛒 Shopping Cart Quantity
- Class: `CartItem`
- Private:
  - `__product_name` → Must be alphabetic
  - `__quantity` → Must be between 1–10
- Invalid product name or quantity → set default and print error
- ❗ Bonus: Mixed validation — strings & numbers

---## 🧠 Concepts Practiced

- Private attributes (`__var`)
- Data hiding
- Setter validation logic
- Read-only & computed properties (like Fahrenheit)
- Class-level error handling
- No regex used — pure Python string & number logic

│   
│ 
├── 04_polymorphism_examples
│   
├── README.md   ← main project README
# 🧠 OOPs in Python – Explained with Code


---


## 👩‍💻 Author
      parul pal

**Parul Pal**  
Python Learner | Exploring OOPs, GitHub, and Projects  
🌐 [LinkedIn](https://www.parul-pal-145ba1306/) (Add your link)

---

## ⭐ Like this?

If you're learning Python, star this repo ⭐ and follow for upcoming OOP examples like inheritance, encapsulation, and more!

