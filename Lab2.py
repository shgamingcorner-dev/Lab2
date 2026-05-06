import statistics as stats

def display_main_menu():
    print("Enter numbers seperated with commas eg. '3, 4, 5.2, 6' ")

def get_user_input():
    stats = input("Enter numbers here: ")
    sheets = stats.split(",")
    floatsheets = []
    for i in sheets:
        i = float(i)
        floatsheets.append(i)
    return floatsheets


def calc_average(x):
    nolist = len(x)
    total = 0
    for i in x:
        total += i
    average = total / nolist
    return average


def find_min_max(x):
    list.sort(x)
    minmaxlist = [x[0], x[-1]]
    return minmaxlist


def sort_temperature():
    print("Sorting the temperature")


def calc_median_temperature(x):
      return stats.median(x)



def main():
    print("ET0735 LAB2")
    display_main_menu()
    list = get_user_input()
    average = calc_average(list)
    minmax = find_min_max(list)
    median = calc_median_temperature(list)
    print("the list =" + str(list))
    print("Average =" + str(average))
    print("Minimum, Maximum" + str(minmax))
    print("median =" + str(median))

if __name__ == "__main__":
    main()





