equation = raw_input 'enter the equation of line in the form of y= mx+c'
rhs = equation.split('=')[1]
parts = rhs.split('+')
m = parts[0].repalce('x','').strip()
c = parts[1].strip()
print 'slope of line : {}'.format(m)
print 'y-intercept :{}'.format(c)
