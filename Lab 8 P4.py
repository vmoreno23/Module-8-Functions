def check_leap_year(year):
    if year % 4 == 0:
        print("A leap year")
        return True
    elif (year % 100 == 0) and (year % 400 == 0):
        print("A leap year")
        return True
    else:
        return False
    

print("Year: 2024")
check_leap_year(2024)
check_leap_year(2015)
print("Year: 2000")
check_leap_year(2000)

# Victor Moreno
# 3/7/24

#Function takes a year as parameter and returns True if the year is a leap year, False if it is otherwise. 
