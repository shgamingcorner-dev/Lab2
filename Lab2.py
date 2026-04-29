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


def display_main_menu():
    print("Enter numbers seperated with commas eg. '3, 4, 5.2, 6' ")



def get_user_input():
    stats = input()
    sheets = stats.split(", ")
    listing = [sheets]
    return listing



def calc_average(list):
    noinfo = len(list)
    for i in range(noinfo):
        total = total + list[noinfo]
    
    average = total / len(list)
    return average


def find_min_max(list)
    list.sort(key=myFunc)
    minmaxlist = [list[0], list[-1]]
    return minmaxlist


def sort_temperature()
    print("Sorting the temperature")


def calc_median_temperature()
    print("calc the temp")







