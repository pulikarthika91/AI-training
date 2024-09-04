class MultipleFunction():
    def Subfields():
    print("Sub-fields in AI are:")
        sublistinAI=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for sub in sublistinAI:
            print(sub)
        
    def OddEven():
        num=int(input("Enter a number:"))
        if(num%2==0):        
            print(num," is an Even number")
        else:        
            print(num," is an odd number")
    def Elegible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(age>=21 and gender=="Male"):
            print("ELIGIBLE")
        elif(age>=18 and gender=="Female"):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
    def getPercentage():
        Subject1= int(input("Subject1"))
        Subject2= int(input("Subject2"))
        Subject3= int(input("Subject3"))
        Subject4= int(input("Subject4"))
        Subject5= int(input("Subject5"))
        total=Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total : ",total)
        percentage=((total/5)*100)/100
        print("Percentage : ", percentage)
    def areaofTriangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        area=(height*breadth)/2
        print("Area of Triangle: ",area)    
    def perimeterofTriangle():
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth1=int(input("Breadth:"))
        perimeter=height1+height2+breadth1
        print("Perimeter of Triangle: ",perimeter)