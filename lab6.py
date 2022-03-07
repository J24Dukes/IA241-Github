'''
lab6
'''


#3.1

for i in range(6):
   if i !=3:
    print(i)


#3.2

result = 1
for i in range (1,6):
    
    print(i) 
    
    result = result * i
print(result)

#3.3

result = 0
for i in range(1,6):
    
    print(i)
    result = result + i
    
print(result)

#3.4

result = 1

for i in range(3,9):
   
    print(i)
    
    result = result * i

print(result)

#3.5

result = 1

for i in range(4,9):
   
    print(i)
    
    result = result * i

print(result)


#3.6
result = 0
for word in 'this is my 6th string'.split():
    
    result = result +1
    print(word)

print(result)