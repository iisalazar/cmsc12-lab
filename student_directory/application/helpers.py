
def convert_obj_to_string(user):
	return '{no},{f},{m},{l},{y},{age}'.format(
			no = user.get('studentNo'),
			f = user.get('fName'),
			m = user.get('mName'),
			l = user.get('sName'),
			y = user.get('year'),
			age = user.get('age')
		)

def convert_users_to_list(users):
	_users = []
	for user in users:
		_users.append(convert_obj_to_string(user))

	return _users