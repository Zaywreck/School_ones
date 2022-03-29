from tkinter import *
import math

root = Tk()

root.title("COCOMO Hesaplayıcı")


Label(root,text='Kloc').grid(row=1,column=2)
Kloc_entry = Entry(root, width=25, borderwidth=5)
Kloc_entry.grid(row=1, column=2, columnspan=3, padx=10, pady=10)

org_month_result = Entry(root,width=25,borderwidth=5)
org_month_result.grid(row=3, column=1, columnspan=3, padx=10, pady=10)
Label(root,text='Kaç ay lazım-organik').grid(row=3)

sd_month_result = Entry(root,width=25,borderwidth=5)
sd_month_result.grid(row=4,column=1,columnspan=3, padx=10, pady=10)
Label(root,text='Kaç ay lazım-yarıgömülü').grid(row=4)

embedded_month_result = Entry(root,width=25,borderwidth=5)
embedded_month_result.grid(row=5,column=1,columnspan=3,padx=10,pady=10)
Label(root,text='Kaç ay lazım-gömülü').grid(row=5)

org_people_needed = Entry(root, width=25, borderwidth=5)
Label(root,text='Kaç insan lazım-organik').grid(row=3,column=4)
org_people_needed.grid(row=3, column=5, columnspan=3, padx=10, pady=10)

sd_people_needed = Entry(root, width=25, borderwidth=5)
Label(root,text='Kaç insan lazım-yarıgömülü').grid(row=4,column=4)
sd_people_needed.grid(row=4, column=5, columnspan=3, padx=10, pady=10)

emb_people_needed = Entry(root, width=25, borderwidth=5)
Label(root,text='Kaç insan lazım-gömülü').grid(row=5,column=4)
emb_people_needed.grid(row=5, column=5, columnspan=3, padx=10, pady=10)


a1,b1,c1,d1 = 2.4,1.05,2.5,0.38
a2,b2,c2,d2 = 3.0,1.12,2.5,0.35
a3,b3,c3,d3 = 3.6,1.20,2.5,0.32


def hesapla(x):
    
    K_org = a1*math.pow(x,b1)
    org_value_months = c1*math.pow(K_org,d1)
    people1 = round(K_org/org_value_months)
    str(org_value_months)
    str(people1)
    org_month_result.insert(0, org_value_months)
    org_people_needed.insert(0, people1)
    
    K_sd = a2*math.pow(x,b2)
    sd_value_months = c2*math.pow(K_sd,d2)
    people2 = round(K_sd/sd_value_months)
    str(sd_value_months)
    str(people2)
    sd_month_result.insert(0, sd_value_months)
    sd_people_needed.insert(0, people2)
    
    K_emb = a3*math.pow(x,b3)
    embedded_value_months = c3*math.pow(K_emb,d3)
    people3 = round(K_emb/embedded_value_months)
    str(people3)
    str(embedded_value_months)
    embedded_month_result.insert(0, embedded_value_months)
    emb_people_needed.insert(0, people3)
    
    


hesap_butonu = Button(root, text="Hesapla", padx=40, pady=20, command=lambda: hesapla(int(Kloc_entry.get())))
hesap_butonu.grid(row=10,column=5,columnspan=1,padx=10,pady=10)


root.mainloop()