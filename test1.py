print("Hello world")
print 28+45
print 34*46

fred = 100;
john = fred
print john;

found_coins = 20
magic_coins = 10
stolen_coins = 3

print (found_coins + magic_coins * 365 - stolen_coins * 52)
stolen_coins = 2
print (found_coins + magic_coins * 365 - stolen_coins * 52)

fred = '''Why do gorillas have big nostrils?
Big fingers!!'''  ##
print fred;

single_quote_str = 'He said, "Aren\'t can\'t shouldn\'t wouldn\'t."'
double_quote_str = "He said, \"Aren't can't shouldn't wouldn't.\""

print(single_quote_str)
print(double_quote_str)

myscore = 100
message = 'I scored %s is %s points'
print (message % (myscore,myscore))

print (10 * '1')

space = ' ' * 25
print('%s 12 Butts Wynd' % space)
print('%s Twinklebottom Heath' % space)
print('%s West Snoring' % space)
print()
print()
print('Dear Sir')
print()
print('I wish to report that tiles are missing from the')
print('outside toilet roof')
print('I think it was bad wind the other night that blew them away')
print()
print('Regards')
print('Malcolm Dithering')

##print(1000 * 'snirt')

wizard_list = ['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'snake dandruff']

print(wizard_list)



wizard_list[2] = 'Human hand'
print(wizard_list)
print(wizard_list[2:5])


numbers = [1,3,4,5,6,8]
string = ['Guo', 'Lulu', 'Chang', 'Shuting']
mylist = [numbers, string]
print(mylist)

wizard_list.append('Bear burp')
print(wizard_list)

del wizard_list[5]
print(wizard_list)

list1  = numbers * 5

print (list1)

print (numbers + string)

favorite_sport = {'A' : 'football',
                  'B' : 'Basketball',
                  'D' : 'Bjarb',
                  'C' : 'Netball',
                  'E' : 'Rugby' }

favorite_color = {'A' : 'Red',
                  'B' : 'Yellow',
                  'C' : 'Blue'}

##favorite_sport['D'] = 'Ice Hockey'

##print(favorite_sport + favorite_color)

##import turtle

##t = turtle.Pen()
##t.forward(40)

age  = 13
if age == 20 or age == 15 or age == 13:
    print('You are too old!')
elif age == 14:
    print('You are a 13!')
##else:
    ##

myval = None
print(myval)

if myval == None:
    print('It dose not have any value !')
age = 10
converted_age = str(age)

if converted_age == '10':
    print('Age is 10 !')


money = 200
if money > 1000:
    print("I am Rich!")
else:
    print("I'am not ritch")
    print("But I might be later")

for x in range(0, 10):
    print('Hello %s' % x)

print(list(range(10,20)))


for i in wizard_list:
    print(i)

hugehairypants = ['huge', 'hair', 'pants']
for i in hugehairypants:
    print(i)
    for j in hugehairypants:
        print(j)
        
coins = found_coins
for week in range(1, 52):
    coins = coins + magic_coins - stolen_coins
    ##print('Week %s = %s', week, coins)

for step in range(1, 20):
    print(step)

x = 45
y = 80
while x < 50 and y < 100:
    x = x + 1
    y = y + 1
    print x, y
    
    if (x + y > 130):
        break

for x in range(0, 20):
    if (x % 2) == 0:
        print('hello %s' % x)

ingredients = ['snails', 'leeches', 'gorilla', 'cater']

for x in range(0,4):
    ##print(x+1)
    print(x+1),ingredients[x]
    
##page.69
