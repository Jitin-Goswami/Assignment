# Body Mass Index (BMI) Calculator

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Get user input
try:
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    if weight <= 0 or height <= 0:
        print("Weight and height must be positive numbers.")
    else:
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is: {bmi:.2f}")

        # Categorize BMI
        if bmi < 18.5:
            print("Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            print("Category: Normal weight")
        elif 25 <= bmi < 29.9:
            print("Category: Overweight")
        else:
            print("Category: Obese")
except ValueError:
    print("Invalid input! Please enter numeric values.")
