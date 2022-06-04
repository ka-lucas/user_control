from src.util.file import *


class UsersCore:
    def list_users(self):
        all_users = get_data()
        users_name = []
        for user in all_users:
            users_name.append(user['nome'])
        return users_name

    def create_user(self, data):
        all_users = get_data()
        all_users.append(data)
        insert_data(all_users)
        return all_users

    def update_user(self, data):
        all_users = get_data()
        for index, user in enumerate(all_users):
            if data['id'] == user['id']:
                all_users[index] = data
        insert_data(all_users)
        return all_users

    def remove_user(self, data):
        all_users = get_data()
        for index, user in enumerate(all_users):
            if data['id'] == user['id']:
                del (all_users[index])
        insert_data(all_users)
        return all_users


