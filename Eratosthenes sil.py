
#Eratosthenes sil program

def eratosthenes(n):        
    Primtall = []           #Liste med primtall
    for i in range (2, n+1): #tar alle tall fra 
        if i not in Primtall:
            print(i)
            for p in range(i*i, n+1, i):
                Primtall.append(p)
                
                
eratosthenes(100)