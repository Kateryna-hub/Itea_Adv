class BankCard:
    def __init__(self, number, username, validTHRU, PIN, money, status = 'On'):
        self.number = number
        self.username = username
        self.validTHRU = validTHRU
        self.PIN = PIN
        self.money = money
        self.status = status

    def chech_PIN(self):
        flag_check_pin = 1
        counter_entered_pin = 1
        while counter_entered_pin <=4:
            if counter_entered_pin == 4:
                self.status = 'OFF'
                print('Card locked, pleas call to Bank')
                flag_check_pin = 2
                return flag_check_pin
                break
            input_PIN = input('Input PIN code: ')
            if input_PIN == self.PIN:
                return flag_check_pin
                break
            else:
                counter_entered_pin += 1
                print('incorrect PIN')

    def sub_money(self, sum_of_money):
        if sum_of_money <= self.money:
            self.money -= sum_of_money
            print('Successfully')
        else:
            print('there is not enough money on the card')






card1 = BankCard('5678-5467-65456-7634', 'Ivan Ivanov', '15/21', '1234', 3000)
print(card1.status)
c = card1.chech_PIN()
print(c)
card1.sub_money(250)
print(card1.money)
card1.sub_money(3000)
print(card1.money)