day = 5

day = 67

day_2 = 5

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")

match day_2:
    case 1 | 2 | 3 | 4 | 5:
        print("It's a weekday")
    case 6 | 7:
        print("It's the weekend")
    case _:
        print("Invalid day")

month = 5
day_3= 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")