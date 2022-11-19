from account import *  # importing class account from account.py in the same directory


class Test:
    def setup_method(self):
        self.person = account('Uma')

    def teardown_method(self):
        del self.person

    def test_init(self):
        # test for init method
        assert self.person.getname() == "Uma"  # checking name
        assert self.person.getbalance() == 0  # checking balance


    def test_deposit(self):
        # test for deposit method

        self.person.deposit(20)
        assert self.person.getbalance() == 20  # checking balance


    def test_withdraw(self):
        # test for withdraw method
        self.person.deposit(100)
        self.person.withdraw(20)
        assert self.person.getbalance() == 80  # checking balance