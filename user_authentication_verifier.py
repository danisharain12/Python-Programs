email = "danish12@gmail.com"
password = '123'

a = input("Enter your email: ")
b = input("Enter your password: ")

if a == email and b == password:
  print("Login successful!")
elif a != email:
  print("Invalid email.")
else:
  print("Invalid password.")
