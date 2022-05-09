'''
lab8 function
'''

#3.1


def count_words(inpu_str):
    
    return len( inpu_str.split( ))

print(count_words('this is a string'))
    

#3.2

demo_str = 'Hello World!'

print (count_words(demo_str))

#3.3


def find_min(input_list):
    
    min_item = input_list[0]
    
    
    for num in input_list:
        
        if type(num) is not str:
            if min_item >= num:
                min_item = num
        
    return min_item

#3.4

demo_list = [1,2,3,4,5,6]

print ( find_min(demo_list))

#3.5

mix_list = [0,2,3,'a',4,5,6]

print (find_min(mix_list))

