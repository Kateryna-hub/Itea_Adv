import BankCards


card1 = BankCards.BankCard('5678-5467-65456-7634', 'Ivan Ivanov', '15/21', '1234', 3000)
print(card1.status)
checkPIN = card1.chech_PIN()
print(checkPIN)
card1.sub_money(250)
print(card1.money)
card1.sub_money(3000)
print(card1.money)