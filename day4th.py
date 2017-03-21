squares = [x**2 for x in range(10)]
print 'squares:', squares

numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = [x for x in numbers if x % 2 == 0]
odd_numbers = [x for x in numbers if x % 2 != 0]

print 'numbers:', numbers
print 'even numbers:', even_numbers
print 'odd numbers:', odd_numbers


	