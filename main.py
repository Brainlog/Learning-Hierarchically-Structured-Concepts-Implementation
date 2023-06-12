from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from functools import partial
m = Tk()
m.title('Hierarchially Structured Concepts')
m.configure(background='white')
screen_width = m.winfo_screenwidth()
screen_height = m.winfo_screenheight()
m.geometry(f"{screen_width}x{screen_height}+0+0")

def noise_free_learn(lis_of_data,status,labels):
    if lis_of_data == None:
        for widget in m.winfo_children():
            widget.destroy()
        fil = open("nodes.txt","r")
        lis_of_data = fil.readlines()
        lis_of_data = [int(i.strip()) for i in lis_of_data]
        maxh = max(lis_of_data)
        startx = (screen_width/(len(lis_of_data)+1))/(screen_width)
        starty = (screen_height/(maxh+1))/(screen_height)
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
                pointx = startx*(i+1)*screen_width
                pointy = starty*(j+1)*screen_height
                canv.create_text(pointx,pointy,text=f"{str(status[i][j][0])}",fill = "blue",font = ("Helvetica", 20))
                labels[i][j] = (pointx,pointy,status[i][j][0])
                
        ## update the status here
        ## Example update :
        for i in range(len(status)):
            for j in range(len(status[i])):
                status[i][j][0] = 1/(i+1) + status[i][j][0]

        for i in range(1,len(labels)):
            for j in range(len(labels[i])):
                for k in range(len(labels[i-1])):
                    canv.create_line(labels[i-1][k][0],labels[i-1][k][1],labels[i][j][0],labels[i][j][1],fill="white",width=2)

              
        buttonnext = Button(m,background='blue',text="Next",font=("Helvetica", 20),foreground='white',command=partial(noise_free_learn,lis_of_data,status,labels))
        buttonnext.place(relx=0.85,rely=0.9,relheight=0.05,relwidth=0.1)
    else:
        maxh = max(lis_of_data)
        startx = (screen_width/(len(lis_of_data)+1))/(screen_width)
        starty = (screen_height/(maxh+1))/(screen_height)
        print(lis_of_data)
        for widget in m.winfo_children():
            widget.destroy()
        canv = Canvas(m, width=screen_width, height=screen_height)
        canv.place(relx = 0.0, rely = 0.0, relheight=1,relwidth=1)
        for i in range(len(lis_of_data)):
            for j in range(lis_of_data[i]):
                pointx = startx*(i+1)*screen_width
                pointy = starty*(j+1)*screen_height
                ss = status[i][j][0]
                ss = str(ss)
                canv.create_text(pointx,pointy,text=f"{ss}",fill = "blue",font = ("Helvetica", 20))
                labels[i][j] = (pointx,pointy,status[i][j][0])

                
        ## update the status here
        ## Example update :
        for i in range(len(status)):
            for j in range(len(status[i])):
                status[i][j][0] = 1/(i+1) + status[i][j][0]

        for i in range(1,len(labels)):
            for j in range(len(labels[i])):
                for k in range(len(labels[i-1])):
                    canv.create_line(labels[i-1][k][0],labels[i-1][k][1],labels[i][j][0],labels[i][j][1],fill="white",width=2)

              
        buttonnext = Button(m,background='blue',text="Next",font=("Helvetica", 20),foreground='white',command=partial(noise_free_learn,lis_of_data,status,labels))
        buttonnext.place(relx=0.85,rely=0.9,relheight=0.05,relwidth=0.1)
        

def main():
    selectlabel = Label(m,background='red',text="Select the Algorithm",font=("Helvetica", 20),foreground='white')
    selectlabel.place(relx=0.35,rely=0.12,relheight=0.05,relwidth=0.3)
    buttonnoisefree = Button(m,background='red',text="Noise Free",font=("Helvetica", 20),foreground='white',command=partial(noise_free_learn,None,None,None))
    buttonnoisefree.place(relx=0.4,rely=0.2,relheight=0.05,relwidth=0.2)
    m.mainloop()

if __name__ == "__main__":
    main()
