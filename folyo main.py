
#Inicializálás

import folyo_class #Class import

from adatbeolvasas import adat_beolvasas_name    #adatbeolvasás  folyó név importálása

from adatbeolvasas import adat_beolvasas_length #adatbeolvasás  folyó hossza importálása

rekordok=[]   #lista amiben tárolunk, hozzá írunk ezzel kell dolgozni



#File-ból való beolvasás

def Input(file,lista):  #Beolvas egy file-t Menuben majd adok neki helyet
    f=open(file,"r")
    for sor in f:
        sor=sor[:-1].split(";") #most bontjuk a sorokat , kivesszük a ; a helyéről
        rekordok.append(folyo_class.Folyó(sor[0],int(sor[1])))
    f.close()




#Gyakorlatilag főprogram, de inkább keretnek használom

    
def f1(label):#Főprogram váza  a menu
    is_on=True
    while is_on:
        print("\n\t\tMENÜ\n\t1.Beolvasás\n\t2.Adatok Bevitele\n\t3.Új file létrehozzása\n\t4.Keresés\n\t5.Leghosszabb folyó\n\t6.Legrövidebb folyó\n\t7.Folyók hosszának átlaga")
        valasz=int(input("\n\tKérem válasszon egy menüpontot: "))
        folytassa=True
        if valasz==1:#File bevitel
            src=input("\tKérem adja meg melyik file-t akarja használni az adatok beviteléhez: ")
            Input(src,rekordok)
            

        elif valasz==2:#Manuális bevitel
            i=0
            while folytassa:
                nev=adat_beolvasas_name()
                hossz=adat_beolvasas_length()
                rekordok.append(folyo_class.Folyó(nev,hossz))
                flag=input("\tTovábbi adatokat is szeretne bevinni (I/N):?")
                if flag!="I":
                    folytassa=False
                else:
                    i+=1
                
                    
                    

        elif valasz==3:#Adatok kiírása választható nevű fileba
            answer=input("\tMilyen néven mentsük az  adatokat? ")
            file_name=answer+".txt"
            f=open(file_name,"w")
            txt=""
            for i in range(0,len(rekordok),1):
                n=rekordok[i].folyónév
                h=rekordok[i].folyóhossz
                txt+=n+"; "+str(h)+"\n"
            f.write(txt)
            f.close()
    
        elif valasz==4:#Keresés folyónév alapján a rekordok listában
            search=input("\n\tKérem adja meg a melyik folyót keresi a listában: ")
            count=0
            for i in range(0,len(rekordok),1):
                if search==rekordok[i].folyónév:
                    count+=1
            if count>0:
                print("\n\tA folyó már a listában szerepel")
            else:
                print("\n\tA folyó még nincs a listában")
        elif valasz==5:
            maxIndex=0
            for i in range(0, len(rekordok),1):
                
                if (rekordok[i].folyóhossz>rekordok[maxIndex].folyóhossz):
                    maxIndex=i
                    txt=rekordok[maxIndex].folyónév+", "+str(rekordok[maxIndex].folyóhossz)+" méter."
            print("\t"+txt)
        elif valasz==6:
            minIndex=0
            for i in range(0, len(rekordok),1):
                if (rekordok[i].folyóhossz<rekordok[minIndex].folyóhossz):
                    minIndex=i
            txt=rekordok[minIndex].folyónév+", "+str(rekordok[minIndex].folyóhossz)+" méter."
            print("\t"+txt)
        elif valasz==7:
           avg_hossz=0
           for i in range(0,len(rekordok),1):
               avg_hossz=avg_hossz+rekordok[i].folyóhossz
               avg_hossz=avg_hossz/len(rekordok)
           print("\tA folyók átlag hossza: "+str(round(avg_hossz,1))+" méter")
                  
        valasz2=input("\tVálasszon a menüpontokból (I/N): ")
        if valasz2=="I":
            is_on=True
        else:
            print("\n\t\tProgram kilép....")
            is_on=False
    









#Itt indítom a programo terveim szerint csak f1 kell többet majd berakok
f1("Projekt Munka")
