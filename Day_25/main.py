num = int(input("Please enter number: "));

for i in range(2, num):
    if(num % i == 0):
        print("It is not prime number");
        break;
else:
    print("It is prime number");