months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
# 9/8/1636 or September 8, 1636 -> YYYY-MM-DD

def main():
    while True:
        try:

            date = input("Date: ").strip()
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
            elif "," in date:
                month_and_day, year = date.split(",")
                m, day = month_and_day.split(" ")
                month = months.index(m) + 1
            else:
                continue
            day = int(day)
            year = year.strip()
            
            if(month in range(1,13) and day in range(1,32)):
                break
        except ValueError:
            continue

    print(f"{year}-{month:02}-{day:02}")
if __name__ == "__main__":
    main()