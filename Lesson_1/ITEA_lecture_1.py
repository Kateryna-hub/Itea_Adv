##### task 1
n = 25
list_of_numbers = list(range(0, n))
print(list_of_numbers)
for i in list_of_numbers:
    if i % 2 == 0:
        print(i)
print()

##### task 2
dict_of_countries = {
    'Ukraine': 'Kyiv',
    'Belarus':  'Minsk',
    'France': 'Paris'}
list_of_countries = ['Ukraine', 'France', 0]
country = input('Введите страну: ')
if country in list_of_countries:
     print(dict_of_countries[country])
else:
    print('нет такой страны')
print()
# country in list_of_countries
# print(dict_of_countries[country])

##### task 3
list_of_numbers1 = list(range(1, 100))
for i in list_of_numbers1:
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)
print()

##### task 4
def bank(first_sum_deposit, date_deposit, rate_deposit):
    sum_deposit_year = first_sum_deposit
    sum_of_income = 0
    for i in range(date_deposit):
        rate_of_year = sum_deposit_year  * rate_deposit / 100
        sum_deposit_year += rate_of_year
        sum_of_income += rate_of_year
        result = round(sum_of_income + first_sum_deposit,2)
    return result

print()

total_deposit = bank(500, 4, 5)
print('Конечная сумма по депозиту: ', total_deposit)