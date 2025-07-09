# Ask user for height and weight, then calculate BMI
# BMI = weight / (height * height)

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))
bmi = weight / (height ** 2)
print(f"Your BMI is {bmi:.2f}")
