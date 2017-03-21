names= ['John Doe', 'Jane Doe', 'Johnny Turk']
names[0] = 'Foo Bar'
print 'names now:', names

names.append('Molly Mormon')
names.append('Joe Bloggs')
print 'names finally:', names
print'last name in the list: %s' % names[-1]

joined_names = '\n' .join(names)
print'\n list of names:'
print joined_names

