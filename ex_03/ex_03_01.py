hrs = input("Enter hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)

if h <= 40:
    salary = h * r
else:
    salary = 40 * r + (h - 40) * r * 1.5

print(salary)
