weight = 77
height = 180
bmi = (weight / (height**2)) * 10000
print("Computing…")
print("Your bmi is {}\n".format(bmi))
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 24.99:
    print("Perfect ! Normal weight")
elif 25.00 <= bmi <= 30.00:
    print("Overweight")
elif bmi > 30.00:
    print("Obese")