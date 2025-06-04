import time
top = "  ________  "
middle = " / _____  \\ "
body = "| |___|__| |_"
bottom = "|____________|"
wheels = " OO       OO"
car_parts = [top, middle, body, bottom, wheels]
def carload():
    '''print(top)
    print(middle)
    print(body)
    print(bottom)
    print(wheels, end='')'''
    print(top+'\n'+middle+'\n'+body+'\n'+bottom+'\n'+wheels,end='')
    for  i in range(14):
        time.sleep(0.1)
        print('\t.',end='')
    print('Loading Completed!!!')




