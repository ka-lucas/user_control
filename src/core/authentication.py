from src.util.file import get_data


class AuthenticationCore:
    def log_in_user(self, data):
        all_users = get_data()
        for index, user in enumerate(all_users):
            if data == user:
                return 'usuario logado com sucesso'
        return 'falhou ao tentar fazer o login'
