def is_leap(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            return False
        return True
    return False

def get_year():
    year = input("Enter a year: ")
    if (not year.isdigit()):
        return getYear()
    return year

def main():
    year = getYear()

    if isLeap(int(year)):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")

if __name__ == '__main__':
    main()
