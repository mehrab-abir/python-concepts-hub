def main():
    givenTime = input("What time is it? ")
    time = convert(givenTime)

    if time >=7 and time<=8:
        print("It's breakfast time")
    if time >= 0 and time <= 7:
        print(f"Next meal time is after {7-time} hours.")
    if time > 7 and time < 12:
        print(f"Next meal time is after {12-time} hours.")
    if time >= 12 and time <= 13:
        print("It's lunch time")
    if time > 13 and time < 18:
        print(f"Next meal time is after {18-time} hours")
    if time >= 18 and time <= 19:
        print("It's dinner time")
    if time > 19 and time < 24:
        print("Not a meal time")



def convert(time):
    hours, minutes = time.split(":")

    minuteInNumber = float(minutes) / 60

    return float(hours)+minuteInNumber

main()