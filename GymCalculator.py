#Calculates the BMI of the User
height=float(input("Please Enter Your Height(Metre)"))
weight=float(input("Please Enter Your Weight(Kilogram)"))
bmi=(weight/(height**2))
print("Your BMI is : ",bmi)
if(bmi<18.5):
    print(bmi,"UnderWeight")
elif(bmi>18.5 and bmi<24.9):
    print(bmi,"NormalWeight")
elif(bmi>25 and bmi<29.9):
    print(bmi,"OverWeight")
elif(bmi>30):
    print(bmi,"Obesity")



while True:
    try:
        goal = str(input("What is your goal? Enter M for maintaining, L for losing or G for gaining: "))  
        if goal not in ['M','L','G']:
            raise AssertionError('Please enter the letter M, L or G')
        break
    except AssertionError as e:
        print(e)
        
C =(weight, height)

activity = float(input('''
1.2 - Sedentary: Little or no physical activity.
1.3 - Lightly Active: Light exercise or activity 1-3 days per week.
1.5 - Moderately Active: Moderate exercise or activity 3-5 days per week.
1.7 - Very Active: Hard exercise or activity 6-7 days per week.
1.9 - Extremely Active: Hard daily exercise or activity and physical work 

Enter your activity multiplier according to the table above (number between 1.2 to 1.9): '''))


if goal == 'M':
    total_cal = C.TDEE(act_mult = activity)
elif goal == 'L':
    total_cal = C.cut(act_mult = activity)
elif goal == 'G':
    total_cal = C.bulk(act_mult = activity)  
    
protein = C.protein_intake(weight)

print('''Your daily minimum protein intake is: {} grams'''.format(protein))
