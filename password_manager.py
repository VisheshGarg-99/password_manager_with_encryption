from cryptography.fernet import Fernet



def en():     #----------encryption function

	data = readfile()
	fernet = Fernet(k)
	encrypted = fernet.encrypt(data)
	with open ('password.txt', 'wb') as d:
		d.write(encrypted)


def de(): #---------------decryption function

	data = readfile()
	fernet = Fernet(k)
	decrypted = fernet.decrypt(data)
	decrypted_ = decrypted.decode()
	with open ('password.txt', 'wb') as d:
		d.write(decrypted)


def readfile():

	with open ('password.txt' , 'rb') as v:
		data = v.read()
		return data


def read(n):

	if n==1:
		de()
		with open ('password.txt' , 'r') as v:
			data = v.readlines()
			r=1
			for i in data:
				print(f'{r}.) {i}' , end='')
				r+=1
			print()
		en()

	elif n==2:
		with open ('password.txt' , 'r') as v:
			data = v.readlines()
			r=1
			for i in data:
				print(f'{r}.) {i}', end='')
				r+=1
			print()
		return data
	
	elif n==3:
		de()
		with open ('password.txt' , 'r') as v:
			data = v.readlines()
			r=1
			for i in data:
				print(f'{r}.) {i}', end = '')
				r+=1
		return data

	else:
		pass


def append(n):

	de()
	new = input('enter the new password : ')
	with open ('password.txt' , 'a') as v:
		v.write(str('\n' + new))
	print(f'\n{new} is added successfully...')
	en()


def edit(n):

	r = read(3)
	total_pass = len(r)
	edit_pass = input('\n\nenter the password you want to edit : ')

	if edit_pass.isdigit():
		edit_pass = int(edit_pass)
		edit_pass = edit_pass-1

		if edit_pass>0 and edit_pass < total_pass:
			r[edit_pass] = r[edit_pass]
			confirm = input(f'are you sure you want to edit {r[edit_pass]} "Y" or "N" : ')

			if confirm == "y" or confirm == "Y":
				final = input('enter the new password : \n')
				final = final
				r[edit_pass] = final + '\n'
				with open(r'password.txt','w') as f:
					for i in r:
						f.write(str(i))
				print('The password is edited successfully...')

			elif confirm == "n" or confirm == "N":
				read(2)

			else:
				print('invalid input... please try again!')

		else:
			print('invalid input... please try again!')

	else:
		print('invalid input... please try again!')
			
	en()


def delete(n):

	r = read(3)
	total_pass = len(r)
	print(total_pass)
	del_pass = input('\nenter the password you want to delete : ')

	if del_pass.isdigit():
		del_pass = int(del_pass)
		del_pass = del_pass-1
		if del_pass < total_pass and del_pass>0:

			r[del_pass] = r[del_pass]
			confirm = input(f'are you sure you want to delete {r[del_pass]} "Y" or "N" : ')

			if confirm == "y" or confirm == "Y":
				delete = r.pop(del_pass)
				print(delete + 'is deleted successfully...')
				with open(r'password.txt','w') as f:
					for i in r:
						f.write(str(i))

			elif confirm == "n" or confirm == "N":
				read(2)

			else:
				print('invalid input... please try again!')		

		else:
			print('invalid input... please try again!')

	else:
		print('invalid input... please try again!')
		
	en()


n = input('enter 1 to view, 2 to add, 3 to edit, or 4 to delete  : ')

if n.isdigit():
	n = int(n)
	k = input('enter the key : ')
	if n==1:
		read(n)
	elif n==2:
		append(n)
	elif n==3:
		edit(n)
	elif n==4:
		delete(n)
	else:
		print('invalid input... please try again!')
		

else:
	print('invalid input... please try again!')
