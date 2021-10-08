from replit import db

name = input('what do you want to be called ')


x = 1
while x == 1:
	say = input('what do you want to say(if you want to see the last chat say see) ')
	if say == 'see':
		value = db["message"]
		print(value)
	else:
		db["message"] = name + ' said:' + say
