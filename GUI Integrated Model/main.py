from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from functools import partial
import noisy
import numpy as np
import math
import ast

m = Tk()
m.title('Hierarchially Structured Concepts')
m.configure(background='white')
screen_width = m.winfo_screenwidth()
screen_height = m.winfo_screenheight()
m.geometry(f"{screen_width}x{screen_height}+0+0")

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle


def learn(lis_of_data,status,labels,k,layer_num,flag):
    global traindata,net,training_set,test_set,testdata
    if(flag==0):
        # if(traindata==len(training_set)):
            # m.destroy()
        net.train(training_set[traindata])
        traindata=traindata+1
    else:
        # if(testdata==len(test_set)):
            # m.destroy()
        net.test(test_set[testdata])
        testdata=testdata+1
    if lis_of_data == None:
        for widget in m.winfo_children():
            widget.destroy()
        maxh = pow(k,layer_num)
        lis_of_data=[maxh for i in range(layer_num)]
        startx=0.05
        # startx = (screen_width/(len(lis_of_data)+1))/(screen_width)
        # starty = (screen_height/(maxh+1))/(screen_height)
        starty = 0.02
        labels = []
        for i in range(len(lis_of_data)):
            lis = []
            for j in range((lis_of_data[i])):
                lis.append(0)
            labels.append(lis)
            
        ## extend the tup for passing more information
        status = []
        for i in range(len(lis_of_data)):
            lis = []
            for j in range((lis_of_data[i])):
                tup = [0,0]
                lis.append(tup)
            status.append(lis)
        
    
        canv = Canvas(m, width=screen_width, height=screen_height)
        canv.place(relx = 0.0, rely = 0.0, relheight=1,relwidth=1)
        for i in range(len(lis_of_data)):
            for j in range(lis_of_data[i]):
                pointx = startx*screen_width
                pointy = starty*screen_height
                if net.states[i][j]==0:
                    canv.create_circle(pointx,pointy,10,fill="white",outline="blue",width=2)
                else:
                    canv.create_circle(pointx,pointy,10,fill="black",outline="black",width=2)
                # canv.create_text(pointx,pointy,text=f"{net.states[i][j]}",fill = "blue",font = ("Helvetica", 20))
                labels[i][j] = (pointx,pointy,status[i][j][0])
                starty = starty + 0.85/(maxh-1)
            startx = startx + 0.9/(len(lis_of_data)-1)
            starty = 0.02
                
        ## update the status here
        ## Example update :
        for i in range(len(status)):
            for j in range(len(status[i])):
                status[i][j][0] = 1/(i+1) + status[i][j][0]

        for i in range(1,len(labels)):
            for j in range(len(labels[i])):
                for kk in range(len(labels[i-1])):
                    canv.create_line(labels[i-1][kk][0]+10,labels[i-1][kk][1],labels[i][j][0]-10,labels[i][j][1],fill="black",width=10*net.weights[i-1][j][kk])

              
        buttonnext = Button(m,background='blue',text="Train",font=("Helvetica", 20),foreground='white',command=partial(learn,lis_of_data,status,labels,k,layer_num,0))
        buttonnext.place(relx=0.85,rely=0.9,relheight=0.05,relwidth=0.1)
        buttonnext = Button(m,background='blue',text="Test",font=("Helvetica", 20),foreground='white',command=partial(learn,lis_of_data,status,labels,k,layer_num,1))
        buttonnext.place(relx=0.70,rely=0.9,relheight=0.05,relwidth=0.1)
    else:
        maxh = max(lis_of_data)
        startx=0.05
        # startx = (screen_width/(len(lis_of_data)+1))/(screen_width)
        # starty = (screen_height/(maxh+1))/(screen_height)
        starty=0.02
        print(lis_of_data)
        for widget in m.winfo_children():
            widget.destroy()
        canv = Canvas(m, width=screen_width, height=screen_height)
        canv.place(relx = 0.0, rely = 0.0, relheight=1,relwidth=1)
        for i in range(len(lis_of_data)):
            for j in range(lis_of_data[i]):
                pointx = startx*screen_width
                pointy = starty*screen_height
                ss = status[i][j][0]
                ss = str(round(ss,4))
                if net.states[i][j]==0:
                    canv.create_circle(pointx,pointy,10,fill="white",outline="blue",width=2)
                else:
                    canv.create_circle(pointx,pointy,10,fill="black",outline="black",width=2)
                # canv.create_text(pointx,pointy,text=f"{net.states[i][j]}",fill = "blue",font = ("Helvetica", 20))
                labels[i][j] = (pointx,pointy,status[i][j][0])
                starty = starty + 0.85/(maxh-1)
            startx = startx + 0.9/(len(lis_of_data)-1)
            starty = 0.02
                
        ## update the status here
        ## Example update :
        for i in range(len(status)):
            for j in range(len(status[i])):
                status[i][j][0] = 1/(i+1) + status[i][j][0]

        for i in range(1,len(labels)):
            for j in range(len(labels[i])):
                for kk in range(len(labels[i-1])):
                    canv.create_line(labels[i-1][kk][0]+10,labels[i-1][kk][1],labels[i][j][0]-10,labels[i][j][1],fill="black",width=10*net.weights[i-1][j][kk])

              
        buttonnext = Button(m,background='blue',text="Train",font=("Helvetica", 20),foreground='white',command=partial(learn,lis_of_data,status,labels,k,layer_num,0))
        buttonnext.place(relx=0.85,rely=0.9,relheight=0.05,relwidth=0.1)
        buttonnext = Button(m,background='blue',text="Test",font=("Helvetica", 20),foreground='white',command=partial(learn,lis_of_data,status,labels,k,layer_num,1))
        buttonnext.place(relx=0.70,rely=0.9,relheight=0.05,relwidth=0.1)
    net.states[:][:] = 0
        

def main(k,layer_num):
    # selectlabel = Label(m,background='red',text="Select the Algorithm",font=("Helvetica", 20),foreground='white')
    # selectlabel.place(relx=0.35,rely=0.12,relheight=0.05,relwidth=0.3)
    buttonnoisefree = Button(m,background='red',text="Start",font=("Helvetica", 20),foreground='white',command=partial(learn,None,None,None,k,layer_num,0))
    buttonnoisefree.place(relx=0.4,rely=0.2,relheight=0.05,relwidth=0.2)
    m.mainloop()

open_file = open("training.txt","r")
training_set = open_file.readlines()
training_set = [i.strip() for i in training_set]
training_set = [ast.literal_eval(i) for i in training_set]

open_file = open("testing.txt","r")
test_set = open_file.readlines()
test_set = [i.strip() for i in test_set]
test_set = [ast.literal_eval(i) for i in test_set]

net = noisy.neuralNet(2,3,0.9,1)
traindata = 0
testdata = 0
main(2,3)
print(net.weights)