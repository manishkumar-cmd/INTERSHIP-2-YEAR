# BMI Calculator
# Underweight = <18.5
# Normal weight = 18.5â€“24.9
# Overweight = 25â€“29.9
# Obesity = BMI of 30 or greater
while True:
    height = float(input('Enter your height cm: \n'))
    height = height / 100
    weight = float(input('Enter your weight kg: \n'))

    BMI = round(weight / (height * height), 2)
    print(f'Your body mass index (BMI) is {BMI}')
    if(BMI<=18.5):
        print('You are underweight')
    elif(BMI<=24.9):
        print('You are healthy')
    elif(BMI<=29.9):
        print('You are overweight')
    else:
        print('You are obese')
    userWantsToContinue = input('Do you want to continue? (yes/no): \n')
    if (userWantsToContinue == 'no'):
        print('Over')
        break