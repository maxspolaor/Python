'''
Very simple exercise from Bro Code
'''

principle = 0 
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("principle needs to be positive")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("interest rate needs to be positive")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("time needs to be positive")

total = principle * pow((1 + rate/100), time)
print(f"Balance after {time} year/s: ${total: .2f}")