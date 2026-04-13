from time import  sleep

def countdown(n):
    while n>=0:
        print(n)
        sleep(1)  #intervallo di 1 sec tra i numeri
        n-=1

def countdown_recursive(n):
    #condizione terminale
    if n==0:
        print("Stop")
    #cond non terminale
    else:
        print(n)
        sleep(1)
        countdown_recursive(n-1)

if __name__=="__main__":
    N=10
    countdown_recursive(N)