class account:
    def __init__(self, name: str):
        """

        :param name: entering account name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float):
        """

        :param amount: float number deposited to account
        :return: balance successfully added
        """
        if amount > 0:

            self.__account_balance = self.__account_balance + amount

            return True

        else:

            return False

    def withdraw(self, amount: float):
        """

        :param amount: float number withdrawn to account
        :return: balance successfully subtracted
        """

        if amount > 0:

            if amount <= self.__account_balance:

                self.__account_balance = self.__account_balance - amount

                return True

            else:

                return False
        else:

            return False

    def getbalance(self):
        """

        :return: returns account balance
        """
        return self.__account_balance

    def getname(self):
        """

        :return: returns account name
        """
        return self.__account_name