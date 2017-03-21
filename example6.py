first_name = raw_input ('your first name: ')
last_name = raw_input ('your last name: ')

print('hello %s %s!' % (first_name , last_name))
print('hello {} {}!' .format(first_name , last_name))
print('hello {0} {1}!' .format(first_name , last_name))

print('hello {1} {0}!' .format(first_name , last_name))
print('hello {0} {0} {1}!' .format(first_name , last_name))