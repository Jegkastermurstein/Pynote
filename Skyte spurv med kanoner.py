#Simulering


from pylab import *

def y(t, v_0, theta):
    g = 9.81
    return v_0*sin(theta)*t - 0.5*g*t**2

def yder(t, v_0, theta):
    g = 9.81
    return v_0*sin(theta) - g*t


def x(t, v_0, theta):
    return v_0*cos(theta)*t

def newtons(f, fder, x, v_0, theta, tol=1E-5, N=100):
    i = 0
    while abs(f(x, v_0, theta)) > tol and i <= 100:
        x = x - f(x, v_0, theta)/fder(x, v_0, theta)
        i = i +1
    return x
    
tid = newtons(y, yder, 10, 18, pi/10)
avstand = x(tid, 18, pi/10)
print("Tid:", tid, "avstand:", avstand)
#målinger =2,49m, 0.9s, 4,69m/s


listetid = []
listevinkel = []
listeavstand =  []

#oppgave e
for i in range(6, 2, -1):
    tid = newtons(y, yder, 10, 4.69, pi/i)
    avstand = x(tid, 4.69, pi/i)
    listetid.append(tid)
    listevinkel.append((pi/i)*180/pi)
    listeavstand.append(avstand)
print(listetid,"sekunder")
print(listevinkel, "grader")
print(listeavstand, "meter")  

plot(listevinkel, listeavstand, color = "red")
grid()
title("Skyte spurv med kanon")
xlabel("Grader")
ylabel("Avstand")
show()

   