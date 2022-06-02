#returns the users's interests or tags as keys to a dictionary with value of "placeholder"
def transform_user(user, value_type):
    if value_type == 'interest':
        for interest in user['interests']:
            user[interest] = "placeholder"
        user.pop('interests')
        user.pop('tags')
        user.pop('username')
        user.pop('profile_image')
        user.pop('biography')
    if value_type == 'tag':
        for tag in user['tags']:
            user[tag] = "placeholder"
        user.pop('interests')
        user.pop('tags')
        user.pop('username')
        user.pop('profile_image')
        user.pop('biography')

    return user