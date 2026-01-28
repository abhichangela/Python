abc = [20,10,43,35,68,22];
print(abc);
print(abc[0]);
print(abc[3:]);
print(abc[-2]);

abc.append(99);
print(abc);

abc.insert(1, 9);
print(abc);

abc.remove(43);
print(abc);

abc.pop(1);
print(abc);

abc.pop();
print(abc);

del abc[2:];
print(abc);

abc.extend([29,14,33]);
print(abc);

print(min(abc));
print(max(abc));
print(sum(abc));

abc.sort();
print(abc);
print(type(abc));

# abc.clear();
# print(abc);

# names = ['John', 'Kiran', 'Sumit'];
# print(names);

# mil = [abc, names];
# print(mil);
