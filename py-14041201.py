# 2^3 = 2*2*2
def pow(x,y):
    if y == 1:
        return x
    return x * pow(x,y-1)

# print(pow(2,4))
# print(pow(4,3))

def sum_numbers(file):
    f = open(file, mode='r')
    lines = f.readlines()
    s = 0
    for line in lines:
        s += int(line.strip())
    return s

def sum_numbers_v2(file, mode='all'):
    f = open(file, mode='r')
    lines = f.readlines()
    s = 0
    for line in lines:
        x = int(line.strip())
        if mode == 'all':
            s += x
        elif mode == 'even':
            if x % 2 == 0:
                s += x
        elif mode == 'odd':
            if x % 2 == 1:
                s += x  
        else:
            return 0
    return s
    
# print(sum_numbers('files/numbers.txt'))

# print(sum_numbers_v2('files/numbers.txt'))
# print(sum_numbers_v2('files/numbers.txt', 'odd'))
# print(sum_numbers_v2('files/numbers.txt', 'even'))

# f = open('files/numbers.txt')
# f.close
# lines = ['10\n','20\n','30\n','40']
# with open('files/numbers.txt', mode='w') as f:
#     # f.write('\nhello')
#     f.writelines(lines)

import json

data = {
    'name':'ali',
    'age': 30
}
f = open('files/data.json', mode='w')
data_json = json.dump(data,f, indent=4)
f.close()

f = open('files/data.json')
data2 = json.load(f)
print(data2)
print(type(data2))