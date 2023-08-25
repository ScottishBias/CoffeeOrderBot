import sqlite3
import datetime
import string
from difflib import get_close_matches
from order import Orders

#list of coffee types
COFFEE_LIST =[
    'caffe latte', 'caffe mocha', 'white chocolate mocha', 'latte macchiato', 'caramel macchiato', 'cappuccino', 'caffe americano', 'espresso', 'espresso macchiato', 'espresso con panna', 'flat white','cortado', 'filter coffee', 'caffe misto', 'double espresso', 'caffe au lait', 'irish coffee', 'affogato'
]

#subroutine to make orders.txt more readable
def readable(lt):
    with open('orders.txt','w') as f:
        f.write('')
    for i in range(len(lt)):
        tup = lt[i]
        nam = tup[0].capitalize()
        cof = tup[1].capitalize()
        iced = tup[2]
        milk_t = tup[3].capitalize()
        decaf = tup[4]
        siz = tup[5].capitalize()
        tim = tup[6]
        
        if iced == 0:
                str_i = 'Un-iced'
        else:
                str_i = 'Iced'
        if decaf == 0:
                str_d = 'Decaffeinated'
        else:
                str_d = 'Caffeinated'
        with open('orders.txt','a') as f:
                f.write(f'{nam}: "{siz}" size {str_d} {str_i} {cof} with {milk_t} (milk)  {tim} \n')

#subroutine to match input for coffee to coffee_list
def coffee_type(typ, coffee_lt, n=3, cutoff=0):
    if typ.lower() in coffee_lt:
        return False
    typ=typ.lower()
    return get_close_matches(typ, coffee_lt, n=n, cutoff=cutoff)
    

def insert_orders(name, coffee, ice, milk, decaff, size):
    x = datetime.datetime.now()
    time = f'{x.strftime("%x")} {x.strftime("%X")}'   
    ord=Orders(name, coffee, ice, milk, decaff, size, time)
    with conn:
        c.execute("INSERT INTO orders VALUES (:name, :coffee, :ice, :milk, :decaff, :size, :time)",
        {'name': ord.name, 'coffee': ord.coffee, 'ice':ord.iced, 'milk': ord.milk, 'decaff': ord.decaff, 'size': ord.size, 'time': ord.time })

def get_orders():
    with conn:
        c.execute("SELECT * FROM orders")
        return c.fetchall()
    
conn = sqlite3.connect('orders.db')
# conn = sqlite3.connect(':memory:')
c=conn.cursor()
try:
        c.execute("""CREATE TABLE orders (
        name text,
        coffee text,
        ice integer,
        milk text,
        decaff integer,
        size text,
        time text
        )""")
except(sqlite3.OperationalError):

        while __name__ == '__main__':    
                print('''Would you like to:
1. Enter an Order
2. Check Orders
3. Clear Orders''')
                choice = input("Please enter '1', '2' or '3':  ")
                if choice == '1':
                        translator = str.maketrans('', '', string.punctuation)                        
                        #user inputs
                        name = input('Enter Your Name: ')
                        name = name.translate(translator)
                        
                        coffee = input('Enter Coffee Type: ')
                        test = coffee_type(coffee, COFFEE_LIST, n=3)
                        
                        while test is not False: #user picks which option is correct
                                print(f"""Did you mean:
1.{test[0]}
2.{test[1]}
3.{test[2]}""")
                                correction = input("Please enter '1', '2', '3' or 'none':  ")
                                if correction == 'none':
                                        coffee = input('Please reenter Coffee Type: ')
                                        test = coffee_type(coffee, COFFEE_LIST)
                                elif correction == '1' or correction == '2' or correction == '3':
                                        correct_int = int(correction)
                                        correct_int -= 1
                                        coffee = test[correct_int]
                                        print(coffee.capitalize())
                                        test = False
                                else:
                                        coffee = input('Please reenter Coffee Type: ')
                                        test = coffee_type(coffee, COFFEE_LIST)
                        ice = input('Do you want it Iced (yes/no)? ')
                        ice = ice.translate(translator)
                        Value_Ice = True
                        while Value_Ice is True: #changing the input to binary
                                if ice=='yes' or ice =='y':
                                        ice=1
                                        Value_Ice=False
                                elif ice == 'no' or ice == 'n':
                                        ice=0
                                        Value_Ice=False
                                else:
                                        print('Incorrect Input')
                                        ice = input('Do you want Ice (yes/no)? ')
                        milk = input('What sort of milk would you like? ')
                        milk = milk.translate(translator)
                        decaff = input('Decaffeinated (yes/no)? ')
                        decaff = decaff.translate(translator)
                        Value_Decaff=True
                        while Value_Decaff is True: #changing the input to binary
                                if decaff=='yes' or decaff== 'y':
                                        decaff = 1
                                        Value_Decaff = False
                                elif decaff == 'no' or decaff == 'n':
                                        decaff = 0
                                        Value_Decaff = False
                                else:
                                        print('Incorrect Input')
                                        decaff = input('Decaffeinated (yes/no)? ')
                        size= input('Enter Coffee size: ')
                        size = size.translate(translator)
                        insert_orders(name, coffee, ice, milk, decaff, size)
                        print('''
----Order Entered----
                              ''')
                elif choice == '2':
                                orders_list=get_orders()
                                readable(orders_list)
                                print('''
        ---------
Check orders.txt for Orders List
        ---------
                                                                ''')
                elif choice == '3':
                        with open('orders.txt','w') as f:
                                f.write('')
                        with conn:
                                c.execute("DELETE from orders")
                        print('')
                        print('''---Orders Cleared---
                        
                        ''')
                else:
                        print('Incorrect Input')
conn.close()
