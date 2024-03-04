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
        print('VERIFY \n')
        # Load All Keys
        file= open("BC.pk",'rb')
        PK = pickle.load(file)
        file.close()
        file= open("BC.sk",'rb')
        SK = pickle.load(file)
        file.close()


        # Load Userinfo
        file= open("BCLeisure.obj",'rb')
        BC = pickle.load(file)
        file.close()
        print(BC)
        file= open("BCFLeisure.obj",'rb')
        BCF = pickle.load(file)
        file.close()
        #[TotBlk,Totwid]=np.shape(BC)
        [TotBlk,TotBlkv]=np.shape(BC)
        print('Existing Blocks are: ',TotBlk,'\n')
        print('-----------------------------------------------------------\n')
        print('ENTER PARAMETER-\n')
        Beneficiary_ID=str(float(ee3.get()))
        PassportDetail=str([Beneficiary_ID])#str([Aadhar+Name+Age+Sex+Vaccine+Dose1+Dose2+Batch+Beneficiary_ID])
        print('USER ENTER B.ID',PassportDetail)



        TP=0;
        ValInd=0
        for ik in range(TotBlk):
            print(ik)
            # Verification
            public_key=PK[ik]
            signature=SK[ik]
            public_key = (base64.b64decode(public_key)).hex()
            signature = base64.b64decode(signature)
            vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(public_key), curve=ecdsa.SECP256k1)
            #print('signature:',signature)
            try:
                print('This User Credential is :',vk.verify(signature, PassportDetail.encode()),'\n')
                print('This Passport Credential is verified \n')
                TP=TP+1
                ValInd=ik
            except:
                    print('.\n')
                


        if TP>=1:
                print('This Passport Credential is verified \n')
                print(BCF[ValInd])
                msg1='This Passport Credential is verified'
                msg2='Verified'
        else:
                print('This Passport Credential is Rejected \n')
                msg1='This Passport Credential is Rejected'
                msg2='Rejected'
                
                
        
        top = Tk()  
        top.geometry("100x100")
        messagebox.showinfo("information",msg1)
        lbl3.configure(text=msg2)
        top.mainloop()


       

	 
#############################################################################################################################################################
lbl = Label(tab3, text="    VERIFY    ",font=("Arial Bold", 30),foreground =("red"))
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
Label(tab3, text="Benificiary:",font=("Arial Bold", 15),foreground =("green")).grid(row=1,column=0,sticky=W,  padx=10, pady=10)
ee3 = Entry(tab3)
ee3.grid(row=1, column=1,sticky=W, padx=10, pady=10)

lbl3_1= Label(tab3, text="Benificiary ID",font=("Arial Bold", 10),foreground =("black"),background  =("white"));lbl3_1.grid(column=2, row=1)

lbl3= Label(tab3, text="STATUS",font=("Arial Bold", 10),foreground =("black"),background  =("white"));lbl3.grid(column=3, row=3)
lbl4= Label(tab3, text="RESULT",font=("Arial Bold", 10),foreground =("black"),background  =("white"));lbl4.grid(column=4, row=3)

Button(tab3, text='PREDICT', command=GEN_SPEECH0,font=("Arial Bold", 15),foreground =("yellow"),background  =("brown")).grid(row=3, column=4, sticky=W, pady=4)
#############################################################################################################################################################
tab_control.pack(expand=1, fill='both')
window.mainloop()
