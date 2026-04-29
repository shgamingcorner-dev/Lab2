def calculate_bmi(height,weight):
    BMI = weight / (height * height)
    print("Height=" + str(height))
    print("Weight=" + str(weight))
    print("BMI=" + str(BMI))

    if BMI <18.5: 
        print("Underweight")
    elif BMI >= 18.5 and BMI  <= 25.0:
        print("Normal Weight")
    else:
        print("Overweight")



calculate_bmi(weight=57,height=1.73)