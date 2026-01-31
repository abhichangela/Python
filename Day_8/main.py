# Dictionary
# if you want to accessing the data by using key then we are using dictionary
# Dictionary uses key and value pair

dir = {1: 'Hello', 2: 'World!', 4: 'How are you?', 'abc': 'All well'};
print(dir);
print(dir[2]);
print(dir['abc']);
# print(dir[3]); This will give error as 3 key is not present

# property of dictionary:
# key must be immutable and unique
# immutable means we can't change the value
# unique means we can't repeat the key 
# value can be anything
# we can access the value by using key 
# we can't access the value by using index
# we can't access the value by using value

print(dir.get(1));
print(dir.get(3));
print(dir.get(2,"No data found"));
print(dir.get(3,"No data found"));

# get() method:
# we can access the value by using get() method
# if key is present in dictionary then it will return the value
# if key is not present in dictionary then it will return None

key = ['Ramesh', 'Suresh', 'Paresh'];
values = ['Python', 'Java', 'C++'];
combineData = dict(zip(key, values));
print(combineData);
print(combineData['Ramesh']);
# print(combineData['Monika']); This will give error
combineData['Monika'] = 'JavaScript';
print(combineData);
print(combineData['Monika']);

del combineData['Suresh'];
print(combineData);

# use of zip() method:
# we can combine the two list by using zip() method
# it will return the tuple

# use of dict() method:
# we can convert the tuple into dictionary by using dict() method

program = {
    'JS': 'Atom',
    'CS': 'VS',
    'Python': ['Pycharm','Sublime'],
    'Java': {'JSE':'Netbeans','JEE':'Eclipse'}};
print(program);
print(program['JS']);
print(program['Python'][1]);
print(program['Java']['JSE']);