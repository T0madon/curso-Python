from pessoa import Cliente
from conta import Conta, ContaCorrente, ContaPoupanca

class Banco:
    def __init__(
        self, 
        bank: str,
        users: list[Cliente] | None = None,
        accounts: list[ContaCorrente] | list[ContaCorrente] | None = None,
        agencies: list[int] | None = None,
    ):
        self.bank = bank
        self._users = users or [] 
        self._accounts = accounts or [] 
        self._agencies = agencies or []

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self._agencies!r}, {self._users!r}, {self._accounts!r})'
        return f'{class_name}{attrs}'
    
    # Métodos para autenticação

    def _check_agency(self, agency):
        if agency.agency in self._agencies:
            return True
        return False

    def _check_account(self, account):
        if account in self._accounts:
            return True
        return False

    def _check_user(self, user):
        if user in self._users:
            return True
        return False

    def authenticate(self, account, user):
        return self._check_account(account) and \
            self._check_agency(account) and \
            self._check_user(user)
    
    # Método dinâmico para add coisas no banco

    def add(self, attr):
        clas = type(attr).__name__

        if clas == 'Cliente':
            self._users.append(attr)
            return
        if ((clas == 'ContaCorrente') | (clas == 'ContaPoupanca')) and \
            (attr.agency in self._agencies):
            self._accounts.append(attr)
            return
        self._agencies.append(attr)

    # Mostrar informações do banco

    def show_users(self) -> None:
        print(f'Usuários {self.bank}:')
        for user in self._users:
            print(f'({user.name}, {user.age})')

    def show_accounts(self) -> None:
        print(f'Contas existentes:')
        for acc in self._accounts:
            if (type(acc).__name__ == 'ContaPoupanca'):
                print(f'Agência: {acc.agency} # Número: {acc.number} '
                f'  # Saldo {acc.balance}')
            else:
                print(f'Agência: {acc.agency} # Número: {acc.number} '
                f'  # Saldo {acc.balance} # Limite: {acc.lim}')    

    






