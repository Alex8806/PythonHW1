#  Вы пользуетесь общественным транспортом? 
#  Вероятно, вы расплачивались за проезд и получали билет с номером. 
#  Счастливым билетом называют такой билет с шестизначным номером, 
#  где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
#   т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no
x = int(input('Ведите билет с шестизначным номером- '))
if 0 <= x < 1000000: # несовсем понял есть ли у нас билеты типа 001001, поэтому так.
    y1, y2=(x//1000), (x%1000)
    if (y1//100+y1%10+(y1%100)//10) == (y2//100+y2%10+(y2%100)//10):
        print("yes")
    else:
        print("no")
else:
    print("wrong ticket number")