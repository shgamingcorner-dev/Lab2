def calculate_bmi(height,weight):
    BMI = weight / (height * height)
    print("Height=" + str(height))
    print("Weight=" + str(weight))
    print("BMI=" + str(BMI))

    if BMI <18.5: 
        print("Underweight")
        return -1
    elif BMI >= 18.5 and BMI  <= 25.0:
        print("Normal Weight")
        return 0
    else:
        print("Overweight")
        return 1

def calculator(a,b,operation):
    if operation == '+':
        answer = a + b
    elif operation == '-':
        answer = a - b

    elif operation == '*':
        answer = a * b
    elif operation == '/':    
        answer = a / b
    else:
        answer = 'wrong'

    return answer

def Clean_text(text):
    UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cleantext = ''

    for i in text:
        if i.isalnum():
            cleantext+=i
    print(cleantext.lower())