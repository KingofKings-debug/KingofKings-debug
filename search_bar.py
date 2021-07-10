from tkinter import *
import webbrowser
from list_taken import name
from list_taken import network
root=Tk()
root.title("Search bar")
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
#name=["youtube","redit","insta","whatsapp"]
#network=["https://www.youtube.com/","https://www.reddit.com/","https://www.instagram.com/","https://web.whatsapp.com/"]
def saving(name0, network0):
    name.append(name0)
    network.append(network0)
    my_file=open("list_taken.py","w")
    my_file.write("name="+str(name)+"\n")
    my_file.write("network="+str(network))
    my_file.close()

  
def search():
    
   
    url=entry.get()
    tf=url not in name
    if (tf==False):
        item = name.index(url)
        url3=network[item]
        webbrowser.get(chrome_path).open(url3)
    if (tf==True):
        starting="https://google.com/search?q="
        url2=(starting+url)
        webbrowser.get(chrome_path).open(url2)

        
def save():
    root2=Tk()
    root2.title("Save New")
    
    label_name=Label(root2,text="Name",font=("arial",15,"bold"))
    label_name.grid(row=1,column=0)

    name_entry=Entry(root2,width=30)
    name_entry.grid(row=1,column=1)

    Label(root2,text="").grid(row=2,column=0)

   
    label_network=Label(root2,text="Adress",font=("arial",15,"bold"))
    label_network.grid(row=3,column=0)

    network_entry=Entry(root2,width=50)
    network_entry.grid(row=3,column=1)

    
    def plz():
        name=name_entry.get()
        network=network_entry.get()
        saving(name,network)

    save_btn=Button(root2,text="Save",command= plz,bg="white",fg="black",font=("arial",15,"bold"))
    save_btn.grid(row=4,columnspan=100)


label1=Label(root,text="Enter to Serch:",font=("arial",15,"bold"))
label1.grid(row=0,column=0)


entry=Entry(root,width=50,)
entry.grid(row=0,column=1)


btn=Button(root,text="Search",command=search,bg="blue",fg="white",font=("arial",14,"bold"))
btn.grid(row=1,column=0,columnspan=3,pady=10)


btn2=Button(root,text="New",command=save,bg="green",fg="white",font=("arial",12,"bold"))
btn2.grid(row=1,column=1,columnspan=2,pady=10)


root.mainloop()
