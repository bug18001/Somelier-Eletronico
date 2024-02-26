from tkinter import *
import tkinter as tk 
import pandas as pd
import numpy  as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder




def predicao():
    global teste
    global valuesNV
    global tagain
    global button2

    sc = StandardScaler()
    

    wineDF  = pd.read_csv('WineQT.csv')
    bins = (2, 6.5, 8)
    group_names = ['Bad', 'Good']
    wineDF['quality'] = pd.cut(wineDF['quality'], bins = bins, labels = group_names)


    X = wineDF.drop(['quality','Id','free sulfur dioxide','residual sugar','total sulfur dioxide'] ,axis = 1)
    y = wineDF['quality']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    rfc = RandomForestClassifier(n_estimators=300)

    rfc.fit(X_train, y_train)

    valores = ["fixed acidity","volatile acidity","citric acid","chlorides","density","pH","sulphates","alcohol"]
    VinhoDF = pd.DataFrame(columns= valores )
    vinhos = [1]
    
    for _ in vinhos:
        try:
            fa =  float(a.get())  #"fixed acidity      
            va =  float(b.get())  #volatile acidity"   
            ca =  float(c.get())  #"citric acid"        
            ch =  float(e.get())  #"chlorides"               
            den = float(h.get())  #"density            
            ph =  float(y1.get())  #"pH"                
            sph = float(z.get())  #"sulphates"         
            alc = float(i.get())  #"alcohol"           
                
        except (ValueError,IOError) as err:       
            valuesNV = Label(jnla, text ="Invalid values!")
            tagain = Label(jnla, text ="Try Again...")
            button1['state'] = DISABLED
            valuesNV.grid(row=21,column=2)
            tagain.grid(row=22,column=2)    
            button2 = tk.Button(jnla, text="Retry", command = Delete)   
            button2.grid(row=21, column=3)
            continue
        else:                        
            valoresDF = pd.DataFrame(data=[[fa,va,ca,ch,den,ph,sph,alc]], columns=valores)
      
            VinhoDF = pd.concat([VinhoDF,valoresDF], axis=0)
            VinhoDF = pd.concat([VinhoDF,valoresDF], axis=0)
            VinhoDF = sc.transform(VinhoDF)
      

            pred = rfc.predict(VinhoDF)
            print(pred)

            if  'Bad' in np.array(pred):                
                pred ="Bad Wine choice!"
            else:
                pred = "Its a Good wine!"

            print(pred)
        teste = Label(jnla, text= pred ,font=("Arial", 10))
        teste.grid(row=21,column=2)
    
    return
        
       

           
def Delete():
    
    try:  
        a.delete(0,END)
        b.delete(0,END)
        c.delete(0,END)
        e.delete(0,END)   
        h.delete(0,END)
        y1.delete(0,END)
        z.delete(0,END)
        i.delete(0,END)   
        valuesNV.destroy()
        tagain.destroy()
        button2.destroy()
        button1['state'] = NORMAL
        teste.destroy()
    except Exception:
        pass

   
jnla = tk.Tk()
jnla.title("Eletronic Sommelier")
jnla.geometry("310x310")

a =   Entry(jnla)     #"fixed acidity*"          
b =   Entry(jnla)     #"volatile acidity*",      
c =   Entry(jnla)     #"citric acid*"                   
e =   Entry(jnla)     #"chlorides*"                
h =   Entry(jnla)     #"density",                
y1 =  Entry(jnla)     #"pH"                      
z =   Entry(jnla)     #"sulphates*",             
i =   Entry(jnla)     #"alcohol*                 

a.grid(row= 3  ,column=2)       #"fixed acidity*"          
b.grid(row= 4  ,column=2)       #"volatile acidity*",       
c.grid(row= 5  ,column=2)       #"citric acid*"                          
e.grid(row= 7  ,column=2)       #"chlorides*"                       
h.grid(row= 10 ,column=2)       #"density",                     
y1.grid(row= 11 ,column=2)       #"pH"                           
z.grid(row= 12 ,column=2)       #"sulphates*",              
i.grid(row= 13 ,column=2)       #"alcohol*                    


fa=Label(jnla, text="fixed acidity:"       )
fa.grid(row= 3  ,column=1)

vo=Label(jnla, text="volatile acidity:"    )
vo.grid(row= 4  ,column=1)

sp=Label(jnla, text="sulphates:"           )
sp.grid(row= 12 ,column=1)

al=Label(jnla, text="alcohol:"             )
al.grid(row= 13 ,column=1)

ca=Label(jnla, text="citric acid:"         )
ca.grid(row= 5  ,column=1)

cl=Label(jnla, text="chlorides:"           )
cl.grid(row= 7  ,column=1)

de=Label(jnla, text="density:"             )
de.grid(row= 10 ,column=1)

ph=Label(jnla, text="pH:"                  )
ph.grid(row= 11 ,column=1)





Label(jnla, text="Insert Wine properties:",font=("Arial", 9)).grid(row=1, column=2)


button1 = tk.Button(jnla, text="Analise", command = predicao)
button1.grid(row=21, column=1)

button3 = tk.Button(jnla, text="clear", command = Delete)
button3.grid(row=22, column=1)



tk.mainloop()


    
        
            
            
    
    
