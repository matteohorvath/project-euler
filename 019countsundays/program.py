counted_sundays = 0

starting_year = 1999
ending_year = 2020

watched_days = 0
current_day = 1
current_month = 1
current_year = 1900
current_day_of_week = 0
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

days_of_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

run = True

while (run):
    watched_days += 1
    current_day += 1
    current_day_of_week += 1


    # weekdays overload
    if current_day_of_week == 7:
        current_day_of_week = 0

    # day overload
    if current_day == days_of_months[current_month-1]+1:
        current_day = 1
        current_month += 1
    # month overload
    if current_month == 13:
        current_month = 1
        current_year += 1
    # jan 1 february day set
    if current_day == 1 and current_month == 1:

        if current_year % 4 == 0:
            days_of_months[1] = 29
        elif current_year % 100 == 0:
            days_of_months[1] = 28
        elif current_year % 400 == 0:
            days_of_months[1] = 29
        else:
            days_of_months[1] = 28


    if current_day_of_week != 6:
        continue
    elif current_day == 1:
        if current_year >= starting_year:
            #print(f"Current Date is : {current_year}.{current_month}.{current_day}. which is {days_of_week[current_day_of_week]}")
            #print(f"This year February is : {days_of_months[1]}")
            counted_sundays += 1

    if current_year > ending_year:
        print(f"Counted sundays : {counted_sundays} , watched days : {watched_days}")
        run = False
