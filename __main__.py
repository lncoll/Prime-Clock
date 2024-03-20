import math
from time import localtime, strftime, sleep

def esPrimo(numero):

    if ((numero % 6) in [0,2,3,4,]):
        return False
    for divisor in range(6, math.ceil(math.sqrt(numero)) + 1, 6):
        if (0 == numero % (divisor + 1)):
            return False
        if (0 == numero % (divisor - 1)):
            return False
    return True

def prueba():        
    for hora in range(0, 24):
        for minuto in range(0, 60):
            for segundo in range(0,60):
                valor = hora * 10000 + minuto * 100 + segundo
                if esPrimo(valor):
                    print(valor)

def reloj():
    tiempo = localtime()
    valor = tiempo.tm_hour * 10000 + tiempo.tm_min * 100 +tiempo.tm_sec
    if esPrimo(valor):
        print(strftime("%H:%M:%S", tiempo), end = '\r')

#prueba() 

while 1:
    reloj()
    sleep(1)

