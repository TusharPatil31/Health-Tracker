# This function is to calculate BMI
def bmi(Weight, Height):
    bmi = Weight / ((Height/100)**2)
    if bmi <= 18.4:
        print(f"Your BMI: {format(bmi,'.1f')}. Try to put on some weight !")
    elif bmi >= 25.0:
        print(f"Your BMI: {format(bmi,'.1f')}. Try to loss weight !")
    else:
        print(f"Your BMI: {format(bmi,'.1f')}. Normal weight !")

# For Speed Calculation
def For_Speed(WorkOut, Day):
    Fast_Speed = 0
    Avg_Speed = 0
    speed = 0
    for key in WorkOut:
        x = WorkOut[key]
        sec = 0
        for i in x[1].split(":"):
            sec = sec*60 + int(i,10)
        if int(x[0]) != 0:
            speed = ((int(x[0]))*3600) / (sec*1400)
            Avg_Speed = Avg_Speed + speed
       
        if Fast_Speed < speed:
            Fast_Speed = speed
        if key == 1:
            Slow_Speed = speed
        if Slow_Speed > speed:
            Slow_Speed = speed

    Avg_Speed = Avg_Speed / Day
    return Fast_Speed, Slow_Speed, Avg_Speed  

#For Distance Calculation
def For_Distance(WorkOut):
    Long_Distance = 0
    Avg_Distance = 0
    for key in WorkOut:
        x = WorkOut[key]
        Avg_Distance = Avg_Distance + int(x[0])
        if int(x[0]) != 0:
            Distance = (int(x[0]))/1400
        
        if Long_Distance < Distance:
            Long_Distance = Distance
        if key == 1:
            Short_Distance = Distance
        if Short_Distance > Distance:
            Short_Distance = Distance

    Avg_Distance = Avg_Distance / 1400
    return Long_Distance, Short_Distance, Avg_Distance

WorkOut = { }

#Initial Inputs
Name = input("Name: ")
Sex = input("Sex: ")
Age = int(input("Age(Years): "))
Weight = float(input("Weight(Kg): "))
Height = int(input("Height(cms): "))

#input number of steps and time(HH:MM:SS)
for i in range(1,8):
    print(f"Enter a Day {i} Foot steps and time(HH:MM:SS)")
    Foot_time = input().split( )
    WorkOut[i] = Foot_time 

print()
print(f"Hi,{Name}")
bmi(Weight, Height)

#how much days of exercise
print("Your Weekly achievement is as follows:")
count = 0 
for key in WorkOut:
    x = WorkOut[key]
    if x[0] == '0':
        count += 1

if count == 0:
    print("No breakout in Sessions: You get a 7/7 award ! ")
    Day = 7
else:
    Day = 7 - count
    print("No Awards this week, as there are breaks in the schedule. ")


Fastest_Speed, Slowest_Speed, Avg_Speed = For_Speed(WorkOut,Day)    
Longest_Distance, Shortest_Distance, Avg_Distance = For_Distance(WorkOut) 

print(f"Your Fastest Speed is: {format(Fastest_Speed,'.2f')} Km/hr")
print(f"Your Longest Distance is: {format(Longest_Distance,'.1f')} Km")
print(f"Your Slowest Speed is: {format(Slowest_Speed,'.2f')} Km/hr")
print(f"Your Shortest Distance is: {format(Shortest_Distance,'.1f')} Km")
print(f"Your Weekly Average Speed is: {format(Avg_Speed,'.2f')} Km/hr")
print(f"Your Weekly Average Distance is: {format(Avg_Distance,'.2f')} Km")

