marks = float(input("Enter your marks: "))

if marks >= 80 and marks <= 100:
  print("Grade A")
elif marks >= 70 and marks <= 79:
  print("Grade B")
elif marks >= 60 and marks <= 69:
  print("Grade C")
elif marks >= 50 and marks <= 59:
  print("Grade D")
elif marks < 50 and marks >= 0:
  print("Grade F")
else:
  print("Invalid marks")
