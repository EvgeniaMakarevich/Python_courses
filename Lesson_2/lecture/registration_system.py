class Registration_system:
    def __init__(self):
        self.users = {}



    def register(self, name, email, phone):
        if email in self.users:
            return "Ошибка: Пользователь с таким email уже существует!"
        self.users[email] = {'name': name, 'phone': phone, 'email': email}
        return "Пользователь успешно зарегистрирован!"

    def delete_all_users(self):
        self.users = {}
        return "Все пользователи успешно удалены!"

    def delete_user_by_email(self,email):
        if email not in self.users:
            return "Ошибка: Пользователь с таким email не найден!"

        del self.users[email]
        return f"Пользователь с email {email} успешно удален!"

    def view_all_users(self):
        return self.users



system = Registration_system()

print(system.register('Alex','alex@example.com','+1234567890'))
print(system.view_all_users())
print(system.delete_user_by_email('alex@example.com'))
print(system.delete_all_users())



