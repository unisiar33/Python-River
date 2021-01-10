#import folyok_class
folyok=[]

def inputFile(file, lista):
    f=open(file,"r")
    for sor in f:
        sor=sor[:-1].split(";")
        lista.append([str(sor[0]), int(sor[1])])
    f.close




def beolvas(label):
    print(label)
    inputFile("folyok.txt", folyok)
    print("\tA fájl beolvasás... kész!")

def f1(label):
    print(label)
    maxIndex=0
    for i in range(0, len(folyok),1):
        if (folyok[i][0]>folyok[i][maxIndex]):
            maxIndex=i
    txt="\tA leghosszabb folyó:\n"+"\t"+folyok[maxIndex][0]+"- "+str(folyok[maxIndex][1])+"kilométerrel"
    print(txt)

def hozzaad(label):
    print (label)
    txt="\tAdjon hozzá egy folyónevet:"
    name=input(txt)
    txt="\tMost a megadott folyó hosszát kilóméterben"
    length=input(txt)
    f=open(txt,"w")
    for i in range(0, len(folyok),1):
        txt=name[i]+";"+length[i]+"\n"
        f.write(txt)
    f.close
    txt="\tAz ön által megadott folyó hozzáadva a listához"
    print(txt)
    
        
    



beolvas("A fájl beolvasása")
f1("1. feladat")
hozzaad("adj hoozza")
input ("<<ENTER>>")
