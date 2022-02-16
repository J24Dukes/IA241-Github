'''
lec4 talk about dictionary and tuple
'''


my_tuple = 'a','b','c','d','e'
print(my_tuple)

my_2nd_tuple = ('a','b','c','d','e')
print(my_2nd_tuple)

not_a_tuple = ('a')
print( type ( not_a_tuple) )

Is_as_tuple = ('a',)
print( type( Is_as_tuple) )

print(my_tuple[1])
print(my_tuple[1:3])
print(my_tuple[1:])
print(my_tuple[:3])
print(my_tuple[:])

my_car = { 
      'color': 'red',
      'maker': 'toyota',
      'year':2015
    }
print(my_car)
print(my_car['year'])
print(my_car['color'])

print(my_car.items())
print(my_car.keys())
print(my_car.values())
print(my_car.get('year'))

my_car['model'] = 'Corolla'
print(my_car)

my_car['year'] = 2020
print(my_car)

print( len(my_car))

print( 2020 in my_car)