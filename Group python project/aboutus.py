import time
def aboutus():
    info = '''Car Tale is a customer-centric car company that offers a seamless experience for both buying second-hand cars and renting vehicles. 
    Specializing in high-quality pre-owned cars, we carefully select each vehicle for its reliability, condition, and value, ensuring that our customers receive dependable options at competitive prices.
    Whether you're purchasing your first car or upgrading to something new, Car Tale provides a diverse range of vehicles—from compact sedans to spacious SUVs—so you can find the perfect fit for your lifestyle and budget.'''

    mid = '''In addition to sales, Car Tale offers flexible car rental services for short-term needs. 
    Whether you need a car for a weekend trip, a business meeting, or just a temporary vehicle, our rental options are designed to suit all kinds of requirements.
    We pride ourselves on our transparent pricing, no hidden fees, and customer-first approach, making the rental process as smooth and straightforward as possible.'''

    end = '''With multiple locations and a reputation for reliability, Car Tale is committed to delivering a hassle-free experience, whether you’re buying or renting. 
    Our experienced team is always on hand to assist with every step, from choosing the right vehicle to handling paperwork, ensuring your complete satisfaction with every transaction.'''

    infos = info.split()
    middle = mid.split()
    ending = end.split()
    top = ' _____      ___       _____                _____     ___     _     ______'
    bel = '|          /   \\     |     |                 |      /   \\   |     |      '
    bel2= '|         /_____\\    |_____/                 |     /_____\\  |     |------'
    bel3= '|_____   /       \\   |     \\                 |    /       \\ |____ |______'

    a = '  ______'
    b = ' | ____ |'
    c = ' ||____||'
    e = ' |______|'
    f = '   | _|'
    g = '   |  |'
    h = '    \\_\\'
    i = '    / /'
    j = '    \\/ '
    print('\t\t\t\t\t\t',top)
    print('\t\t\t\t\t\t',bel)
    print('\t\t\t\t\t\t',bel2)
    print('\t\t\t\t\t\t',bel3)
    print('\t\t\t\t\t\t\t\t\t\t',a)
    print('\t\t\t\t\t\t\t\t\t\t',b)
    print('\t\t\t\t\t\t\t\t\t\t',c)
    print('\t\t\t\t\t\t\t\t\t\t',e)
    print('\t\t\t\t\t\t\t\t\t\t',f)
    print('\t\t\t\t\t\t\t\t\t\t',g)
    print('\t\t\t\t\t\t\t\t\t\t',h)
    print('\t\t\t\t\t\t\t\t\t\t',i)
    print('\t\t\t\t\t\t\t\t\t\t',j)
    print('+===================================================================================================================================================================+')

    for i in infos:
        print(i, end = ' ')
        time.sleep(0.02)
    print()
    print()
    print()
    for i in middle:
        print(i, end = ' ')
        time.sleep(0.02)
    print()
    print()
    print()
    for i in ending:
        print(i, end = ' ')
        time.sleep(0.02)
    print()
    print()
    print()
    print('+===================================================================================================================================================================+')

