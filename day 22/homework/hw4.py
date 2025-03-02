# 5) მოცემული Flowchart-ის მიხედვით დაწერეთ if else statement-ებისგან შემდგარი კოდი, და კომენტარის სახით დაწერეთ თუ რა იქნება კოდის შედეგი მაშინ, როდესაც მომხმარებელი არის სტუდენტი და მის მიერ შემოტანილი ასაკი იქნება 17

status = "student" 
age = 17  
if status == "student":
    if age < 18:
        print("You are a student and a minor.")
    else:
        print("You are a student and an adult.") 
else:
    print("You are not a student.")