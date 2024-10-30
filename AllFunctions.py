class multiplefunction():
     
    def subfields():
        subfields_list=["Machine learning","Neural networks","Vision","Robotics","Speech processing","Natural Language processing"]
        print("Subfields in AI are:")
        for fields in subfields_list:
         print(fields)

    def oddeven():
        num=int(input("Enter the number:"))
        if (num % 2) == 0:
             print(num,"is even number")
        else:
             print(num,"is odd number")


    def eligible():
       age=int(input("Enter your age:"))
       gender=input("Enter your Gender (male/female): ")
       if age > 21 and gender.lower() == "male":
            print("Eligible")
            message="Eligible"
       elif age > 18 and gender.lower() == "female": 
            print("Eligible")
            message="Eligible"
       else:
            print("Not eligible")
            message="Not eigible"



    def markscored():
        subject1=int(input("Subject1:"))
        subject2=int(input("Subject2:"))
        subject3=int(input("Subject3:"))
        subject4=int(input("Subject4:"))
        subject5=int(input("Subject5:"))
        Total=(subject1+subject2+subject3+subject4+subject5)
        print("Total:",Total)
        percentage=Total/5
        print("Percentage:", percentage)
    


    def triangle():
        Height=int(input("Height"))
        Breadth=int(input("Breadth"))
        Area=(Height*Breadth)/2
        print("Area of the triangle:", Area)
        Height1=int(input("Height1"))
        Height2=int(input("Height2"))
        Breadth=int(input("Breadth"))
        Perimeter= Height1+Height2+Breadth
        print("Perimeter of the triangle:", Perimeter)
    