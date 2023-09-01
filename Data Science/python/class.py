month = input("Enter month: ").lower().replace(' ', '')[:3]

match month:
    case "feb":
        print("29 days for leap years and 28 for every other year")
    case "sep":
        print("30 days")
    case "jun":
        print("30 days")
    case "apr":
        print("30 days")
    case "nov":
        print("30 days")
    case other:
        print("31 days")