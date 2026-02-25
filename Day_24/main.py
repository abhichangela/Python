nums = [12, 15, 18, 20, 26];

for i in nums:
    if(i%5 == 0):
        print(i);
print("------------------------");

for i in nums:
    if(i%5 == 0):
        print(i);
        break;
print("------------------------");

data = [12, 14, 18, 21, 26];
for i in data:
    if(i%5 == 0):
        print(i);
    else:
        print("Not found");

print("------------------------");

for i in data:
    if(i%5 == 0):
        print(i);
        break;
else:
    print("Not data found");