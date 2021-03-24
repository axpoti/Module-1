count=0.0

upper_limit=0

upper_limit = int(input ('What number should I go up to? '))
while True:
    count=count+1
    if count > upper_limit:
        break
    if count/17 == int(count/17):
        if count/3 == int(count/3):
            print ('FizzFezz')
        elif count/5 == int(count/5):
            print ('BuzzFezz')
        elif count/7 == int(count/7):
            print ('BangFezz')
        elif count/11 == int(count/11):
            print ('BongFezz')
    elif count/13 == int(count/13):
            if count/3 == int(count/3):
                print ('FizzFezz')
            elif count/5 == int(count/5):
                print ('FezzBuzz')
            elif count/7 == int(count/7):
                print ('FezzBang')
            elif count/11 == int(count/11):
                print ('FezzBong')
    elif count/11 == int(count/11):
            print ('Bong' )
    elif count/7 == int(count/7):
            if count/5 == int(count/5) or count/3 == int(count/3):
                print ('FizzBang' )
            else:
                print ('Bang')           
    elif count/5 == int(count/5):
            print ('FizzBuzz' )           
    elif count/3 == int(count/3):
            print ('Fizz' )            
    else:
            print ('The number is ' + str(int(count)))