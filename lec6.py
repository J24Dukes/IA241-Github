'''
lec6
'''

for letter in ['a','b','c']:
    print (letter)
    
demo_str = 'This is my string'

for c in demo_str:
    print (c)
    
for word in demo_str.split():
    print(word)
    
for i in range(5):
    print(i)
    
for i in range(1,5):
    print(i)
    
for i in range(1,5,2):
    print(i)
    
num_list = [1,2,9,1]

max_item = num_list[0]

for num in num_list:
    if max_item <= num:
        max_item = num
        
print(max_item)

