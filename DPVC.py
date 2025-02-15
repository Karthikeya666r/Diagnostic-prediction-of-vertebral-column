from tkinter import *
from tkinter import messagebox
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import os
import sys
import time
import csv

# Save data into a csv file
with open('lab_records.csv', 'a') as file:
        writer = csv.writer(file)
        if((os.path.getsize("lab_records.csv"))==0):
            writer.writerow(["Time","Patient Name","Age","Gender","Pelvic Incidence","Pelvic Tilt","Lumbar Lordosis Angle","Sacral slope","Pelvic Radius","Degree of Spondylolistesis","Result"])


# Tkinter Code
root =Tk()
root.title("Diagnostic Predictor")
root.geometry("1600x800")

tops = Frame(root, width = 1600, height = 50, bg = "powder blue", relief = SUNKEN)
tops.pack(side=TOP)

f1 = Frame(root, width = 800, height = 800, relief = SUNKEN)
f1.pack(side=LEFT)


# tkinter time module

localtime = time.asctime(time.localtime(time.time()))

# training and prediction code

dataset = pd.read_csv("vertebral_column_weka.csv")

def diagnostic_predict(pelvic_incidence, pelvic_tilt, lumbar_lordosis_angle, sacral_slope, pelvic_radius, degree_spondylolisthesis):
    # Compared with Logistic Regression, CART, Random Forest, KNN is easier for interpretation and low calculation time.
    knn = KNeighborsClassifier(n_neighbors = 13)
    x,y = dataset.loc[:,dataset.columns != 'class'], dataset.loc[:,'class']
    knn.fit(x,y)
    prediction = knn.predict(x)

    # Check val dimension with X_test before predicting
    val=[pelvic_incidence, pelvic_tilt, lumbar_lordosis_angle, sacral_slope, pelvic_radius, degree_spondylolisthesis ]
    pred = knn.predict([val])
    return pred


# functions used--------------------------------------------------------- 

#Predict Function
def predict():
    screen.delete(0.0, END)
    try:
        patient_name = entry_pn.get()
        pn_msg = "PATIENT NAME : "+ patient_name.upper()
    except:
        UnboundLocalError
        pn_msg = "PATIENT NAME : INVALID INPUT - ENTER VALID DATA\n"
    if (len(patient_name)==0):
        pn_msg = "PATIENT NAME : INVALID INPUT - ENTER VALID DATA\n"

    try:
        gender = entry_gn.get()
        if (gender == "M" or gender == "m"):
            gn_msg = "\nGENDER : Male"
        if (gender == "F" or gender == "f"):
            gn_msg = "\nGENDER : Female"
        if (gender == "O" or gender == "o"):
            gn_msg = "\nGENDER : Other"
    except:
         UnboundLocalError
         gn_msg = "GENDER : INVALID INPUT - ENTER VALID DATA\n"
    if (len(gender)==0):
         gn_msg = "GENDER : INVALID INPUT - ENTER VALID DATA\n"

    try:
        age = int(entry_age.get())
        age_msg = "\nAGE : "+ str(age)
        if (age < 1):
            age_msg = "AGE : INVALID INPUT - ENTER VALID DATA\n"
    except:
        ValueError
        age = 0
        age_msg = "AGE : INVALID INPUT - ENTER VALID DATA\n"

    try:
        pelvic_incidence = float(entry_pi.get())
        pi_msg = "\nPELVIC INCIDENCE : "+ str(pelvic_incidence)
        if (pelvic_incidence < 1):
            pi_msg = "PELVIC INCIDENCE : INVALID INPUT - ENTER VALID DATA\n"
    except:
        ValueError
        pelvic_incidence = 0
        pi_msg = "PELVIC INCIDENCE : INVALID INPUT - ENTER VALID DATA\n"

    try:
        pelvic_tilt = float(entry_pt.get())
        pt_msg = "\nPELVIC TILT : "+ str(pelvic_tilt)
        if (pelvic_tilt < 1):
            pt_msg = "PELVIC TILT : INVALID INPUT - ENTER VALID DATA\n"
    except:
        ValueError
        pelvic_tilt = 0
        pt_msg = "PELVIC TILT : INVALID INPUT - ENTER VALID DATA\n"

    try:
        lumbar_lordosis_angle = float(entry_lla.get())
        lla_msg = "\nLUMBAR LORDOSIS ANGLE : "+ str(lumbar_lordosis_angle)
        if (lumbar_lordosis_angle < 1):
            lla_msg = "LUMBAR LORDOSIS ANGLE : INVALID INPUT - ENTER VALID DATA\n"
    except:
        ValueError
        lumbar_lordosis_angle = 0
        lla_msg = "LUMBAR LORDOSIS ANGLE : INVALID INPUT - ENTER VALID DATA\n"

    try:
        sacral_slope = float(entry_ss.get())
        ss_msg = "\nSACRAL SLOPE : "+ str(sacral_slope)
        if (sacral_slope < 1):
            ss_msg = "SACRAL SLOPE : INVALID INPUT - ENTER VALID DATA\n"
    except:
        ValueError
        sacral_slope = 0
        ss_msg = "SACRAL SLOPE : INVALID INPUT - ENTER VALID DATA\n"

    try:
        pelvic_radius = float(entry_pr.get())
        pr_msg = "\nPELVIC RADIUS : "+ str(pelvic_radius)
        if (pelvic_radius < 1):
            pr_msg = "PELVIC RADIUS : INVALID INPUT - ENTER VALID DATA\n"
    except:
        ValueError
        pelvic_radius = 0
        pr_msg = "PELVIC RADIUS : INVALID INPUT - ENTER VALID DATA\n"

    try:
        degree_spondylolistesis = float(entry_ds.get())
        ds_msg = "\nDEGREE OF SPONDYLOLISTESIS : "+ str(degree_spondylolistesis)
        if (degree_spondylolistesis == 1):
            ds_msg = "DEGREE OF SPONDYLOLISTESIS : INVALID INPUT - ENTER VALID DATA\n"
    except:
        ValueError
        degree_spondylolistesis = 0
        ds_msg = "DEGREE OF SPONDYLOLISTESIS : INVALID INPUT - ENTER VALID DATA\n"
    

    if((pn_msg != "PATIENT NAME : INVALID INPUT - ENTER VALID DATA\n")
       and (age_msg != "AGE : INVALID INPUT - ENTER VALID DATA\n")
       and (gn_msg != "GENDER : INVALID INPUT - ENTER VALID DATA\n")
       and (pi_msg != "PELVIC INCIDENCE : INVALID INPUT - ENTER VALID DATA\n") 
       and (pt_msg != "PELVIC TILT : INVALID INPUT - ENTER VALID DATA\n")
       and (lla_msg != "LUMBAR LORDOSIS ANGLE : INVALID INPUT - ENTER VALID DATA\n")
       and (ss_msg != "SACRAL SLOPE : INVALID INPUT - ENTER VALID DATA\n") 
       and (pr_msg != "PELVIC RADIUS : INVALID INPUT - ENTER VALID DATA\n")
       and (ds_msg != "DEGREE OF SPONDYLOLISTESIS : INVALID INPUT - ENTER VALID DATA\n")
      ):
        [result] = diagnostic_predict(pelvic_incidence
                                    ,pelvic_tilt
                                    ,lumbar_lordosis_angle
                                    ,sacral_slope
                                    ,pelvic_radius
                                    ,degree_spondylolistesis
                                    )
                                          
        screen.insert(END,localtime+"\n"+pn_msg+age_msg+gn_msg+pi_msg+pt_msg+lla_msg+ss_msg+pr_msg+ds_msg+"\nRESULT : "+result+"\n")
        messagebox.showinfo("Result", result)
        with open('lab_records.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([localtime
                            ,patient_name
                            ,age
                            ,gender
                            ,pelvic_incidence
                            ,pelvic_tilt
                            ,lumbar_lordosis_angle
                            ,sacral_slope
                            ,pelvic_radius
                            ,degree_spondylolistesis
                            ,result])
    else:
        messagebox.showerror("Error", "Please Check Your Entered Data")
        screen.insert(END,pn_msg+age_msg+gn_msg+pi_msg+pt_msg+lla_msg+ss_msg+pr_msg+ds_msg)

# Clear function
def clear():
    # clear output screen
    screen.delete(0.0,END)
    # clear all entry boxes
    entry_pn.delete(0,END)
    entry_age.delete(0,END)
    entry_gn.delete(0,END)
    entry_pi.delete(0,END)
    entry_pt.delete(0,END)
    entry_lla.delete(0,END)
    entry_ss.delete(0,END)
    entry_pr.delete(0,END)
    entry_ds.delete(0,END)

# Quit Function
def quit():
    global root
    root.quit()

# tkinter labels code----------------------------------------------------

lblinfo = Label(tops, font = ('calibri',50,'bold'),text = "Pathologies Prediction of Vertebral Column Diagnosis", fg="steel blue", bd = 10, anchor ='w') 
lblinfo.grid(row=0,column=0)

lbltime = Label(tops, font = ('calibri',20,'bold'),text =localtime, fg="steel blue", bd = 10, anchor ='w') 
lbltime.grid(row=1,column=0)

label_pn = Label(f1,text="PATIENT NAME",font=("calibri",18,"bold"))
label_pn.grid(row=0,column=0,sticky=W,padx=7, pady = 10)

label_age = Label(f1,text="AGE",font=("calibri",18,"bold"))
label_age.grid(row=1,column=0,sticky=W,padx=7, pady = 10)

label_gn = Label(f1,text="GENDER",font=("calibri",18,"bold"))
label_gn.grid(row=2,column=0,sticky=W,padx=7, pady = 10)

label_pi = Label(f1,text="PELVIC INCIDENCE",font=("calibri",18,"bold"))
label_pi.grid(row=3,column=0,sticky=W,padx=7, pady = 10)

label_pt = Label(f1,text="PELVIC TILT",font=("calibri",18,"bold"))
label_pt.grid(row=4,column=0,sticky=W,padx=7, pady = 10)

label_lla = Label(f1,text="LUMBAR LORDSIS ANGLE",font=("calibri",18,"bold"))
label_lla.grid(row=5,column=0,sticky=W,padx=7, pady = 10)

label_ss = Label(f1,text="SACRAL SLOPE",font=("calibri",18,"bold"))
label_ss.grid(row=6,column=0,sticky=W,padx=7, pady = 10)

label_pr = Label(f1,text="PELVIC RADIUS",font=("calibri",18,"bold"))
label_pr.grid(row=7,column=0,sticky=W,padx=7, pady = 10)

label_ds = Label(f1,text="DEGREE OF SPONDYLOLISTESIS",font=("calibri",18,"bold"))
label_ds.grid(row=8,column=0,sticky=W,padx=7, pady = 10)

# tkinter entry boxes code---------------------------------------------

entry_pn = Entry(f1,insertwidth=5,bg="lightblue", bd=10,justify='right') 
entry_pn.grid(row=0,column=1, pady = 12)

entry_age = Entry(f1,insertwidth=5,bg="lightblue", bd=10,justify='right') 
entry_age.grid(row=1,column=1, pady = 12)

entry_gn = Entry(f1,insertwidth=5,bg="lightblue", bd=10,justify='right') 
entry_gn.grid(row=2,column=1, pady = 12)

entry_pi = Entry(f1,insertwidth=5,bg="lightblue", bd=10,justify='right')  
entry_pi.grid(row=3,column=1, pady = 12)

entry_pt = Entry(f1,insertwidth=5,bg="lightblue", bd=10,justify='right')
entry_pt.grid(row=4,column=1, pady = 12)

entry_lla = Entry(f1,insertwidth=5,bg="lightblue", bd=10,justify='right')
entry_lla.grid(row=5,column=1, pady = 12)

entry_ss = Entry(f1,insertwidth=5,bg="lightblue", bd=10,justify='right')
entry_ss.grid(row=6,column=1, pady = 12)

entry_pr = Entry(f1,insertwidth=5,bg="lightblue", bd=10,justify='right')
entry_pr.grid(row=7,column=1, pady = 12)

entry_ds = Entry(f1,insertwidth=5,bg="lightblue", bd=10,justify='right')
entry_ds.grid(row=8,column=1, pady = 12)

# tkinter buttons-------------------------------------------------------

# Predict Button
Predict_button = Button(f1, text = "SUBMIT", width=13, height=2, font = ("times", 16, "bold"), fg="black", bg="powder blue", bd = 5, command = predict).grid(row = 9, column = 0,pady = 20)

# Clear Button
Clear_Button = Button(f1, text="CLEAR", width=13, height=2, font = ('times', 16, 'bold'), fg="black", bg="powder blue", bd = 5, command = clear).grid(row = 9, column = 1,pady = 20, sticky=W)

# Quit Button
Quit_button = Button(f1, text="QUIT", width=13, height=2, font = ('times', 16, 'bold'), fg="black", bg="powder blue", bd = 5, command = quit).grid(row = 9, column = 2, padx = 70, pady = 20, sticky=E)


# tkinter Report Screen module 

report = Label(f1,text="REPORT DETAILS",font=("calibri",18,"bold"))
report.grid(row=0,column=3, sticky = W)

screen = Text(f1, width=60, height=15, wrap = WORD, bd = 8, background = "light blue",font=(18))
screen.grid(row = 1, column = 3, rowspan = 8, sticky = W)

root.mainloop()