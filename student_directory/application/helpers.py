# convers the user dictionary to a string
# seperated by commas
def convert_obj_to_string(user):
	return '{no},{f},{m},{l},{y},{age},{degree}'.format(
			no = user.get('studentNo'),
			f = user.get('fName'),
			m = user.get('mName'),
			l = user.get('sName'),
			y = user.get('year'),
			age = user.get('age'),
			degree = user.get('degree')
		)

# a helper that convers userEntry in string to dictionary
def convert_string_to_obj(userData):
	if type(userData) is str:
		userData = userData.split(',')
	if not len(userData):
		return ''
	return {
        "studentNo": userData[0],
        "fName" : userData[1],
        "mName" : userData[2],
        "sName": userData[3],
        "year" : userData[4],
        "age" : userData[5],
        "degree" : userData[6]
    }
# converts users in dictionaries to list of strings
def convert_users_to_list(users):
	return [ convert_obj_to_string(user) for user in users ]
# converts users in list to list of dictinaries
def convert_strings_to_obj(users):
	return [ convert_string_to_obj(user) for user in users  ]
	