def main():
    time = input("What time is it? ")
    hours = convert(time)

    if 7.0 <= hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= hours <= 13.0:
        print("lunch time")
    elif 18.0 <= hours <= 19.0:
        print("dinner time")

# Version 1
# def convert(time):
#     hours, minutes = time.split(":")
#     return float(hours) + float(minutes) / 60

#Version 2 (Challenge)  
def convert(time):
    time = time.lower()

    if "a.m." in time:
        time = time.replace("a.m.", "").strip()
        period = "a.m."
    elif "p.m." in time:
        time = time.replace("p.m.", "").strip()
        period = "p.m."
    else:
        period = None

    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    if period == "a.m.":
        if hours == 12:
            hours = 0
    elif period == "p.m.":
        if hours != 12:
            hours += 12

    return hours + minutes / 60
    
if __name__ == "__main__":
    main()