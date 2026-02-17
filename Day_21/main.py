x = ["Hello", "World", 57, 98, 3];

for i in x:
    print(i);

y = 'Hello';
for i in y:
    print(i);

print('------------');

for i in range(2,10,3):
    print(i);

print('------------');

for i in range(15, 5, -1):
    print(i);

print('------------');

for i in range(1,20, 1):
    if(i%5 == 0):
        print(i);

for i in range(1,101,1):
    if(i % 3 != 0 and i % 5 != 0):
        print(i);