import time

#Author: Ehirim Williams Uchenna

fruits = {"apple":60, "banana":80, "beetroot":180, "cherry":40, "pawpaw":140, \
          "soursop":200, "avocado":180, "pear":45, "mango":65, "corn":70, \
          "water melon":150}

print('Apple\t\t60 naira')
print('Banana\t\t80 naira')
print('Beetroot\t180 naira')
print('Soursop\t\t200 naira')
print('Pawpaw\t\t140 naira')
print('Cheery\t\t40 naira')
print('Water Melon\t150 naira')
print('Mango\t\t65 naira')
print('Corn\t\t70 naira')
print('Pear\t\t45 naira')
print('Avocado\t\t180 naira\n')

cashier = "Cashier:\tEhirim Williams U."
print(cashier)

my_fruits = []
total_price = 0

n = False

print("\nType 'N' at any time to proceed to checkout")
while not n:
    selection = input("\nPlease select a fruit: ").lower()
    if selection == 'n':
        break
        time.sleep(1)
    my_fruits.append(selection)
    if selection in fruits:
        total_price += fruits.get(selection)
    else:
        print("We don't have this fruit in stock, select from our stock list")
        my_fruits.pop()
        continue
    if total_price > 500:
        print('\nyou don\'t have sufficient funds, please return an item')
        to_return = input('Select fruit to return. ').lower()
        my_fruits.remove(to_return)
        total_price -= fruits.get(to_return)
        break
        time.sleep(1)

print('\n\nYour selection is', *my_fruits, sep=', ')
time.sleep(0.5)
print('Your total is, ' + str(total_price) + ' naira')
print('*'*50)
time.sleep(1)
print('\nThank you for your patronage\nWe look forward to seeing you again.')
