import random
password = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890qwertyuiopasdfghjklzxcvbnm!@#$%^&*()"
m = int(input("Enter the Length of Password: "))
a = "".join(random.sample(password,m))
print("Your password :",a)

