#returns the users's interests or tags as keys to a dictionary with value of "placeholder"
import copy
def transform_user(user, value_type):
    current_user = copy.deepcopy(user)
    if value_type == 'interest':
        for interest in current_user['interests']:
            current_user[interest] = "placeholder"
        current_user.pop('interests')
        current_user.pop('tags')
        current_user.pop('username')
        current_user.pop('profile_image')
        current_user.pop('biography')
    if value_type == 'tag':
        for tag in user['tags']:
            current_user[tag] = "placeholder"
        current_user.pop('interests')
        current_user.pop('tags')
        current_user.pop('username')
        current_user.pop('profile_image')
        current_user.pop('biography')

    return current_user