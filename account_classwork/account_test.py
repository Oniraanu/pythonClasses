import unittest

from account_classwork import account


class AccountTest(unittest.TestCase):

    def test_that_account_can_be_created(self):
        account1 = account.Account("Tolani")
        self.assertIsNotNone(account1)

    def test_that_account_can_have_name(self):
        account1 = account.Account("Tolani")
        name = account1.name
        self.assertEqual("Tolani", name)

    def test_that_account_can_deposit(self):
        account1 = account.Account("Tolani")
        deposit = account1.deposit(2000)
        self.assertEqual(2000, account1.balance)

    def test_that_you_cannot_deposit_negative(self):
        account1 = account.Account("Tolani")
        account1.deposit(1000)
        self.assertRaises(ValueError, account1.deposit, -1000)
        self.assertEqual(1000, account1.balance)

    def test_that_account_can_withdraw(self):
        account1 = account.Account("Tolani")
        account1.deposit(2000)
        account1.withdraw(1000)
        self.assertEqual(1000, account1.balance)

    def test_that_account_cannot_withdraw_more_than_balance(self):
        account1 = account.Account("Tolani")
        account1.deposit(2000)
        account1.withdraw(3000)
        self.assertRaises(ValueError, account1.withdraw, 3000)
        self.assertEqual(2000, account1.balance)

    def test_that_account_can_top_up_mobile(self):
        account1 = account.Account("Tolani")
        account1.deposit(5000)
        account1.mobile_top_up(1000)
        self.assertEqual(4000, account1.balance)

    def test_that_account_can_transfer(self):
        account1 = account.Account("Tolani")
        account2 = account.Account("Bunmi")
        account1.deposit(5000)
        account1.transfer(2000, account2)
        self.assertEqual(3000, account1.balance)

    def test_that_amount_transferred_reflects_in_other_account(self):
        account1 = account.Account("Tolani")
        account2 = account.Account("Bunmi")
        account1.deposit(5000)
        account1.transfer(2000, account2)
        account2.deposit(2000)
        self.assertEqual(2000, account2.balance)
        self.assertEqual(3000, account1.balance)


if __name__ == '__main__':
    unittest.main()
