#My CS50 week 1st problem set 1st, 5th problem, meal time.
#Accepted the challenge for 12 hour time input format.
def main():
    time_input = input("What time is it? ").strip()
    if " " in time_input:
        time, end = time_input.split(" ")
        converted_time = convert(time,end)
    else:
        converted_time = convert(time_input)

    if 7.00 <= converted_time <=8.00:
        print("breakfast time")
    if 12.00 <= converted_time <=13.00:
        print("lunch time")
    if 18.00 <= converted_time <=19.00:
        print("dinner time")


def convert(time,end=None):
    hours, mins = time.split(":")
    hours=float(hours)
    mins=(f"{float(int(mins)/60):.2f}")
    mins=float(mins)
    if end:
        end = end.lower()
        if end == ("p.m.") and hours!=12:
            hours+=12
        elif end == ("a.m.") and hours==12:
            hours=0
    return float(hours+mins)

if __name__ == "__main__":
    main()
