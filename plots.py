import pymysql as db
import numpy as np
from matplotlib import pyplot as plt

conn = db.connect("localhost", "root", "", "prospencore")
cur = conn.cursor()


def plot(v1):
    qry = " select "+v1+", count(*) from" \
          " sales group by "+v1
    cur.execute(qry)
    rs = cur.fetchall()
    car_list = []
    d_v = []
    for i in rs:
        if i[1] not in car_list:
            car_list.append(i[1])
        if i[0] not in d_v:
            d_v.append(i[0])
    d_v.sort()

    dic = {}
    for model in car_list:
        lst = []
        yr = []
        for y, m, c in rs:
            if m == model and y not in yr:
                lst.append(c)
                yr.append(y)
            elif m == model and y in yr:
                lst.pop()
                lst.append(c)
            else:
                if y not in yr:
                    lst.append(0)
                    yr.append(y)
        dic[model] = lst
    return d_v, dic


def pie_plt1():
    mod, c=plot("date_format(sale_date, '%Y'),model_id")
    s1 =list(c.values())
    m1=list(c.keys())
    m=[]
    s=[]
    for i in m1:
        m.append(i)
    for i in s1:
        p=sum(i)
        s.append(p)

    def autopct_val(s1):
         def my_autopct(pct):
             total=sum(s1)
             val=int(round(pct*total/100.00))
             return val
         return my_autopct

    plt.figure(figsize=(15,20))
    plt.subplot(1,2,1)
    plt.pie(s,labels=m,shadow=True,autopct="%2.2f%%")
    plt.title(label="According to Car Model (in percentage)",fontsize='20')

    plt.subplot(1, 2, 2)
    plt.pie(s, labels=m, shadow=True,autopct=autopct_val(s))
    plt.title(label="According to Car Model (in unit sold)", fontsize='20')
    plt.show()


def pie_plt2():
    mod, c=plot("date_format(sale_date, '%Y'),color")
    s1 =list(c.values())
    m1=list(c.keys())
    m=[]
    s=[]
    for i in m1:
       m.append(i)
    for i in s1:
        p=sum(i)
        s.append(p)

    def autopct_val(s1):
         def my_autopct(pct):
             total=sum(s1)
             val=int(round(pct*total/100.00))
             return val
         return my_autopct

    plt.figure(figsize=(15,20))
    plt.subplot(1,2,1)
    plt.pie(s,labels=m1,shadow=True,autopct="%2.2f%%")
    plt.title(label="According to Car Color (in percentage)",fontsize='20')

    plt.subplot(1, 2, 2)
    plt.pie(s, labels=m1, shadow=True,autopct=autopct_val(s))
    plt.title(label="According to Car Color (in unit sold)", fontsize='20')
    plt.show()


def pie_plt3():
    mod, c=plot("model_id,date_format(sale_date, '%Y')")
    s1 =list(c.values())
    m1=list(c.keys())
    m=[]
    s=[]
    for i in m1:
       m.append(i)
    for i in s1:
        p=sum(i)
        s.append(p)

    def autopct_val(s1):
         def my_autopct(pct):
             total=sum(s1)
             val=int(round(pct*total/100.00))
             return val
         return my_autopct

    plt.figure(figsize=(15,20))
    plt.subplot(1,2,1)
    plt.pie(s,labels=m,shadow=True,autopct="%2.2f%%")
    plt.title(label="According to Car Color (in percentage)",fontsize='20')

    plt.subplot(1, 2, 2)
    plt.pie(s, labels=m, shadow=True,autopct=autopct_val(s))
    plt.title(label="According to Car Color (in unit sold)", fontsize='20')
    plt.show()


def bar_plt2():
    mod, c=plot("date_format(sale_date, '%Y'),model_id")
    mod = np.array(mod, dtype=int)
    count = 0
    d = {}
    plt.figure(figsize=(15, 20))
    plt.subplot(1, 2, 1)
    for y in mod:
        k = 0
        for i, j in c.items():
            plt.bar(int(y) + k, j[count], label=i if i not in d else '', width=.05)
            d[i] = i
            k += .05
        count += 1
    plt.xticks(mod)
    plt.title(label="Combined Data Plot",fontsize='20')
    plt.xlabel("Years")
    plt.ylabel("Unit Sold")
    plt.legend()

    count = 0
    l={}
    plt.subplot(1, 2, 2)
    for y in mod:
        for i, j in c.items():
            plt.bar(y, j[count], label=i if i not in l else '', width=.05)
            l[i] = i
        count += 1
    plt.xticks(mod)
    plt.title(label="Combined Data Plot",fontsize='20')
    plt.xlabel("Years")
    plt.ylabel("Unit Sold")
    plt.legend()
    plt.show()


def bar_plt1():
    def show():
        plt.xticks(mod)
        plt.xlabel("Years")
        plt.ylabel("Unit Sold")
        plt.legend()

    mod, c=plot("date_format(sale_date, '%Y'),model_id")
    mod = np.array(mod, dtype=int)
    l = list(c.keys())
    j = list(c.values())

    plt.figure(figsize=(30, 20))

    plt.subplot(4, 2, 1)
    plt.bar(mod, j[0], label=l[0], width=.05)
    show()

    plt.subplot(4, 2, 2)
    plt.bar(mod, j[1], label=l[1], width=.05)
    show()

    plt.subplot(4, 2, 3)
    plt.bar(mod, j[2], label=l[2], width=.05)
    show()

    plt.subplot(4, 2, 4)
    plt.bar(mod, j[3], label=l[3], width=.05)
    show()

    plt.subplot(4, 2, 5)
    plt.bar(mod, j[4], label=l[4], width=.05)
    show()

    plt.subplot(4, 2, 6)
    plt.bar(mod, j[5], label=l[5], width=.05)
    show()

    plt.subplot(4, 2, 7)
    plt.bar(mod, j[6], label=l[6], width=.05)
    show()

    plt.subplot(4, 2, 8)
    plt.bar(mod, j[7], label=l[7], width=.05)
    show()

    plt.show()


def line_plt():
    mod, c = plot("date_format(sale_date, '%Y'),model_id")
    l = list(c.keys())
    j = list(c.values())
    plt.figure(figsize=(30, 20))
    plt.title("Car Sale Record")
    plt.plot(mod, j[0], label=l[0], linewidth=3, linestyle="-", marker="o", color="deeppink",markersize=10,markerfacecolor="black")
    plt.plot(mod, j[1], label=l[1], linewidth=3, linestyle="-", marker="1",color="yellow",markersize=10,markerfacecolor="green")
    plt.plot(mod, j[2], label=l[2], linewidth=3, linestyle=":", marker="*",color="red",markersize=10,markerfacecolor="blue")
    plt.plot(mod, j[3], label=l[3], linewidth=3, linestyle="--", marker="h",color="limegreen",markersize=10,markerfacecolor="yellow")
    plt.plot(mod, j[4], label=l[4], linewidth=3, linestyle="-", marker="+",color="turquoise",markersize=10,markerfacecolor="blue")
    plt.plot(mod, j[5], label=l[5], linewidth=3, linestyle="-", marker="d",color="grey",markersize=10,markerfacecolor="white")
    plt.plot(mod, j[6], label=l[6], linewidth=3, linestyle="-", marker="s",color="royalblue",markersize=10,markerfacecolor="white")
    plt.plot(mod, j[7], label=l[7], linewidth=3, linestyle="-", marker="^",color="black",markersize=10,markerfacecolor="white")
    plt.xlabel("Years")
    plt.ylabel("Unit Sold")
    plt.xticks(mod)
    plt.grid()
    plt.legend()
    plt.show()
