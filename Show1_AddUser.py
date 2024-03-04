import sys
import os
from os import listdir
from os.path import isfile, join
import argparse

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import tkinter.messagebox


import numpy as np
import pandas as pd

import warnings

import pickle
import datetime
import time
from time import sleep

visualise=1
import sys
import base64
import ecdsa

from random import randint
import re
import sys
import numpy as np
import smtplib
import os

THINGSPK=0
# #########################################################
#              CODE
# #########################################################


seed = 7
np.random.seed(seed)


# MAIN PANEL

window = Tk()
window.title("MARKET SALES PREDICTION ")
window.geometry('1200x500')
tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab6 = ttk.Frame(tab_control)

tab_control.add(tab3, text='ADD USER')

##########################################################################
def sendmail(values):
    eml='shubhamaher3877@gmail.com'
    with smtplib.SMTP('smtp.gmail.com',587)as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        #eml='prasadkalane@gmail.com'

        smtp.login('xxxx@gmail.com','xxxx')
        subject = str(values)
        body = "WELCOM TO BLOCKCHAIN!"

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(eml,eml,msg)

def RST():
        messagebox.showerror('CLOSE', 'CLOSE')
        window.quit()
        window.destroy()


# GENERATE HASHING
def GenHash(x):
    print('------------------------------------------------------\n')
    print('--------------- Generating Voter Block ---------------\n')
    sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) #this is your sign (private key)
    private_key = sk.to_string().hex() #convert your private key to hex
    vk = sk.get_verifying_key() #this is your verification key (public key)
    public_key = vk.to_string().hex()

    # Encode the public key to make it shorter
    public_key = base64.b64encode(bytes.fromhex(public_key))

    message = x
    bmessage = message.encode()
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
    signature = base64.b64encode(sk.sign(bmessage))
    print('Message \n',message)
    return public_key,signature

	
def GEN_SPEECH0():# ADDING USER
        values = np.random.randint(100,999,1)
        sendmail(values)
        OTP=int(input('Enter OTP') )
        if values==OTP:
            print('ADMIN VERIFIED')
        else:
           quit()
            
        ERR=0
        print('-----------------------------------------------------------\n')
        print('ENTER PARAMETER-\n')
        Aadhar=ee3.get()
        Name=ee4.get()
        Age=ee5.get()
        Sex=ee6.get()
        '''
        if len(Aadhar)!=16:
                ERR=1
        
        if len(Name)<=2:
                ERR=1
        
        if int(Age)<=18:
                ERR=1
        if len(Age)==0:
                ERR=1
        
        if len(Sex)==0:
                ERR=1
        '''
        Vaccine=ee7.get()
        Dose1=ee8.get()
        Dose2=ee9.get()
        Batch=ee10.get()
        Beneficiary_ID=str(float(ee11.get()))
        if len((Beneficiary_ID))==0:
                Beneficiary_ID='XXXXX'
        OMR=ee12.get()

        BC1=str([Beneficiary_ID])
        BCF1=[Aadhar+Name+Age+Sex+Vaccine+Dose1+Dose2+Batch+Beneficiary_ID+OMR]

        #Load Block
        file= open("BCLeisure.obj",'rb')
        BC = pickle.load(file)
        file.close()
        file= open("BCFLeisure.obj",'rb')
        BCF = pickle.load(file)
        file.close()
        print('LESURE SHAPE-',np.shape(BC),BC1)

        #Write
        BC.append([BC1])
        #BC[len(BC)+1,0]=[BC1]
        print('LESURE SHAPE-',np.shape(BC),BC1)
        BCF.append(BCF1)

        #Dump Block
        filehandler = open("BCLeisure.obj","wb")
        pickle.dump(BC,filehandler)
        filehandler.close()
        print('LESURE SHAPE-',np.shape(BC))
        filehandler = open("BCFLeisure.obj","wb")
        pickle.dump(BCF,filehandler)
        filehandler.close()

        # LOAD BLOCK CHAIN
        file= open("BCLeisure.obj",'rb')
        BC = pickle.load(file)
        file.close()

        # LOAD BLOCK CHAIN
        file= open("BCFLeisure.obj",'rb')
        BCF = pickle.load(file)
        file.close()
        print('BC-----',len(BC),BC)

        if THINGSPK==1:
                import urllib.request as urllib2,json
                # Enter Your API key here
                myAPI = 'YJIMN7N9Y6Z80HOB' 
                # URL where we will send the data, Don't change it
                baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
                
                C1=BC1
                # Sending the data to thingspeak
                conn = urllib2.urlopen(baseURL + '&field1=%s' % (C1))
                print(conn.read())
                # Closing the connection
                conn.close()
                # DHT22 requires 2 seconds to give a reading, so make sure to add delay of above 2 seconds.
                sleep(20)

        # Load existing PK and SK
        file= open("BC.pk",'rb')
        PK = pickle.load(file)
        file.close()
        file= open("BC.sk",'rb')
        SK = pickle.load(file)
        file.close()
        print('LESURE SHAPE-',np.shape(BC))

        [TotBlk,TotBlkv]=np.shape(BC)
        x=str(BC1);
        PK0,SK0=GenHash(x)
        print('Public Key: ',PK0,'\n')
        print('Signature Key: ',SK0,'\n')
        PK.append(PK0)
        SK.append(SK0)

        # Dump All Keys
        filehandler = open("BC.pk","wb")
        pickle.dump(PK,filehandler)
        filehandler.close()
        filehandler = open("BC.sk","wb")
        pickle.dump(SK,filehandler)
        filehandler.close()



        #################################################################
        # Load existing PK and SK
        file= open("BC.pk",'rb')
        PK = pickle.load(file)
        file.close()

        file= open("BC.sk",'rb')
        SK = pickle.load(file)
        file.close()

        print('KEY LENGTH',np.shape(PK),np.shape(SK))
        print('LENGTH',np.shape(BC),np.shape(BCF))



        top = Tk()  
        top.geometry("100x100")
        DATA='User Added Successfully'
        messagebox.showinfo("information",DATA)
        lbl3.configure(text=DATA)
        top.mainloop()


       

	 
#############################################################################################################################################################
lbl = Label(tab3, text="    ADD    ",font=("Arial Bold", 30),foreground =("red"))
lbl.grid(column=0, row=0)
lbl = Label(tab3, text="BLOCKCHAIN",font=("Arial Bold", 30),foreground =("red"))
lbl.grid(column=1, row=0)
lbl = Label(tab3, text="   USER   ",font=("Arial Bold", 30),foreground =("red"))
lbl.grid(column=2, row=0)
lbl = Label(tab3, text="          ",font=("Arial Bold", 30),foreground =("red"))
lbl.grid(column=3, row=0)
lbl = Label(tab3, text="          ",font=("Arial Bold", 30),foreground =("red"))
lbl.grid(column=4, row=0)

# ENTRY BOX
Label(tab3, text="Aadhar:",font=("Arial Bold", 15),foreground =("green")).grid(row=1,column=0,sticky=W,  padx=10, pady=10)
ee3 = Entry(tab3)
ee3.grid(row=1, column=1,sticky=W, padx=10, pady=10)

Label(tab3, text="Name",font=("Arial Bold", 15),foreground =("green")).grid(row=2,column=0,sticky=W,  padx=10, pady=10)
ee4 = Entry(tab3)
ee4.grid(row=2, column=1,sticky=W, padx=10, pady=10)

Label(tab3, text="Age:",font=("Arial Bold", 15),foreground =("green")).grid(row=3,column=0,sticky=W,  padx=10, pady=10)
ee5 = Entry(tab3)
ee5.grid(row=3, column=1,sticky=W, padx=10, pady=10)

Label(tab3, text="Sex:",font=("Arial Bold", 15),foreground =("green")).grid(row=4,column=0,sticky=W,  padx=10, pady=10)
ee6 = Entry(tab3)
ee6.grid(row=4, column=1,sticky=W, padx=10, pady=10)

Label(tab3, text="Vaccine:",font=("Arial Bold", 15),foreground =("green")).grid(row=5,column=0,sticky=W,  padx=10, pady=10)
ee7 = Entry(tab3)
ee7.grid(row=5, column=1,sticky=W, padx=10, pady=10)

Label(tab3, text="Dose1:",font=("Arial Bold", 15),foreground =("green")).grid(row=6,column=0,sticky=W,  padx=10, pady=10)
ee8 = Entry(tab3)
ee8.grid(row=6, column=1,sticky=W, padx=10, pady=10)

Label(tab3, text="Dose2:",font=("Arial Bold", 15),foreground =("green")).grid(row=7,column=0,sticky=W,  padx=10, pady=10)
ee9 = Entry(tab3)
ee9.grid(row=7, column=1,sticky=W, padx=20, pady=20)

Label(tab3, text="Batch:",font=("Arial Bold", 15),foreground =("green")).grid(row=8,column=0,sticky=W,  padx=10, pady=10)
ee10 = Entry(tab3)
ee10.grid(row=8, column=1,sticky=W, padx=10, pady=10)

Label(tab3, text="Benificiary:",font=("Arial Bold", 15),foreground =("green")).grid(row=9,column=0,sticky=W,  padx=10, pady=10)
ee11 = Entry(tab3)
ee11.grid(row=9, column=1,sticky=W, padx=10, pady=10)

Label(tab3, text="MR:",font=("Arial Bold", 15),foreground =("green")).grid(row=10,column=0,sticky=W,  padx=10, pady=10)
ee12 = Entry(tab3)
ee12.grid(row=10, column=1,sticky=W, padx=10, pady=10)

lbl3_1= Label(tab3, text="Aadhar",font=("Arial Bold", 10),foreground =("black"),background  =("white"));lbl3_1.grid(column=2, row=1)
lbl4_1= Label(tab3, text="Name",font=("Arial Bold", 10),foreground =("black"),background  =("white"));lbl4_1.grid(column=2, row=2)
lbl5_1= Label(tab3, text="Age",font=("Arial Bold", 10),foreground =("black"),background  =("white"));lbl5_1.grid(column=2, row=3)
lbl6_1= Label(tab3, text="Sex",font=("Arial Bold", 10),foreground =("black"),background  =("white"));lbl6_1.grid(column=2, row=4)
lbl7_1= Label(tab3, text="Vaccine",font=("Arial Bold", 10),foreground =("black"),background  =("white"));lbl7_1.grid(column=2, row=5)
lbl8_1= Label(tab3, text="Dose1",font=("Arial Bold", 10),foreground =("black"),background  =("white"));lbl8_1.grid(column=2, row=6)
lbl9_1= Label(tab3, text="Dose2",font=("Arial Bold", 10),foreground =("black"),background  =("white"));lbl9_1.grid(column=2, row=7)
lbl10_1= Label(tab3, text="Batch",font=("Arial Bold", 10),foreground =("black"),background  =("white"));lbl10_1.grid(column=2, row=8)
lbl11_1= Label(tab3, text="Benificiary",font=("Arial Bold", 10),foreground =("black"),background  =("white"));lbl11_1.grid(column=2, row=9)
lbl12_1= Label(tab3, text="Old Medical Record",font=("Arial Bold", 10),foreground =("black"),background  =("white"));lbl12_1.grid(column=2, row=10)

lbl3= Label(tab3, text="RESULT",font=("Arial Bold", 10),foreground =("black"),background  =("white"));lbl3.grid(column=3, row=5)

Button(tab3, text='ADD USER', command=GEN_SPEECH0,font=("Arial Bold", 15),foreground =("yellow"),background  =("brown")).grid(row=3, column=4, sticky=W, pady=4)
#############################################################################################################################################################
tab_control.pack(expand=1, fill='both')
window.mainloop()
