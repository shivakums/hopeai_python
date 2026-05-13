class multipleFunction():
    
    def AgeCategory():
        age = int(input("Enter age:"))
        if(age < 18):
            print("Children")
            cat = "Children1"
        elif(age<35):
            print("Adult")
            cat = "Adult1"
        elif(age < 60):
            print("Citizen")
            cat = "Citizen1"
        else:
            print("Senior Citizen")
            cat = "Senior Citizen1"
    
        return cat    

    def OddEven():
        num=int(input("Enter the number:"))
        if ((num%2)==0):
            print("Even number")
            message = "Even number"
        else:
            print("Odd Number")
            message = "Odd number"
        return message
    def BMI():
        bmi = float(input("Enter the BMI Index:"))
        if(bmi < 18.5):
            print("Underweight")
            message = "Underweight"
        elif(bmi >= 18.5 and bmi <= 24.9):
            print("Healthy Weight")
            message = "Healthy Weight"
        elif(bmi > 24.5 and bmi <= 29.9):
            print("Over Weight")
            message = "Over Weight"
        elif(bmi > 29.9 and bmi <= 34.9):
            print("Obese Class1")
            message = "Obese Class1"
        elif(bmi > 34.9 and bmi <= 39.9):
            print("Obese Class2")
            message = "Obese Class2"
        elif(bmi > 39.9 ):
            print("Obese Class3")
            message = "Obese Class3"
        return message    

    def addition(num1,num2):
        add = num1 + num2
        return add   
    
    def subtraction(num1,num2):
        add = num1 - num2
        return add   
