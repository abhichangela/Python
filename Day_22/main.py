# Break keyword
x = int(input("How many ice cream you want to buy? "));
availabe = 3;
i = 1;
while i <= x:
    if(i > availabe):
        print("Out of stock!!!");
        break;
    
    print("Ice cream");
    i+= 1;

print("Thank you visit again");

# continue keyword
for i in range(1, 101):
    if(i % 3 == 0 or i % 5 == 0):
        continue;
    
    print(i);
print('-----------------------');

#Pass keyword
for i in range(1, 101):
    if(i%2 != 0):
        pass;
    else:
        print(i);