import tkinter as tk
off_white ="#F8FAFF"
purple_c="#A060FA"
class calculator:
    window=tk.Tk()
    his=""
    current="0"
    
    numbers={
            7:(2,1),8:(2,2),9:(2,3),
            4:(3,1),5:(3,2),6:(3,3),
            1:(4,1),2:(4,2),3:(4,3),
            0:(5,2)
        }
    operators={
        '/':"\u00F7",'*':"\u00D7",'-':'-','+':'+'
    }
    def __init__(self):
        
        self.window.geometry("350x500")
        self.window.title("CALCULATOR")
        #self.window.resizable(0,0)
        self.display_f=self.create_df()
        self.buttons_f=self.create_b()
        self.hislabel,self.currentlabel=self.create_labels()
        self.buttons_f.rowconfigure(0,weight=1)
        for i in range(1,5):
            self.buttons_f.rowconfigure(i,weight=1)
            self.buttons_f.columnconfigure(i,weight=1)
        
        

        self.num_pad=self.create_numbers()
        self.num_pad_operside=self.create_side_operators()
        self.create_special()
        self.keys_bind()

        
    def run(self):
        self.window.mainloop()
        #creation of frames
    def create_df(self):
        df=tk.Frame(self.window,height=221,bg="#191919")
        df.pack(fill="both",expand=True)
        return df
    def create_b(self):
        bf=tk.Frame(self.window,bg="#191955")
        bf.pack(fill="both",expand=True)
        return bf
    


    def create_labels(self):
        hl=tk.Label(self.display_f,fg=purple_c,text=self.his,bg="#191919",font="Arial 15 bold",anchor=tk.E)
        hl.pack(expand=True,fill="both")
        cl=tk.Label(self.display_f,fg="white",text=self.current,bg="#191919",font="Arial 35 bold",anchor=tk.E)
        cl.pack(expand=True,fill="both")
        return hl,cl
    

    def create_numbers(self):
        for i,j in self.numbers.items():
            b=tk.Button(self.buttons_f,text=str(i),bg="#191919",fg="white",font="Arial 16 bold", borderwidth=0,relief=tk.SUNKEN,
                        command=lambda x=i: self.add_to_current(x))
            b.grid(row=j[0],column=j[1],sticky=tk.NSEW)
    def create_side_operators(self):
        r=1
        for i,j in self.operators.items():
            bt=tk.Button(self.buttons_f,text=j,bg="#191919",fg=off_white,font="Arial 14", borderwidth=0,relief=tk.SUNKEN,command=lambda x=i: self.append_operator(x))
            bt.grid(row=r,column=4,sticky=tk.NSEW)
            r+=1
    def create_equal(self):
        bt=tk.Button(self.buttons_f,text="=",bg=purple_c,fg=off_white,font="Arial 14", borderwidth=0,relief=tk.SUNKEN,command=self.evaluate)
        bt.grid(row=5,column=3,columnspan=2,sticky=tk.NSEW)
    def create_empty(self):
        bt=tk.Button(self.buttons_f,text="",bg="#191919",borderwidth=0,relief=tk.SUNKEN)
        bt.grid(row=5,column=1,sticky=tk.NSEW)
    def create_percent(self):
        bt=tk.Button(self.buttons_f,text="%",bg="#191919",fg=off_white,font="Arial 12", borderwidth=0,relief=tk.SUNKEN,command=self.update_percent)
        bt.grid(row=0,column=1,sticky=tk.NSEW)
    def create_CE(self):
        bt=tk.Button(self.buttons_f,text="CE",bg="#191919",fg=off_white,font="Arial 10", borderwidth=0,relief=tk.SUNKEN,command=self.clear)
        bt.grid(row=0,column=2,sticky=tk.NSEW)
    def create_AC(self):
        bt=tk.Button(self.buttons_f,text="AC",bg="#191919",fg=off_white,font="Arial 10", borderwidth=0,relief=tk.SUNKEN,command=self.clear_all)
        bt.grid(row=0,column=3,sticky=tk.NSEW)
    def create_dot(self):
        bt=tk.Button(self.buttons_f,text=".",bg="#191919",fg=off_white,font="Arial 25", borderwidth=0,relief=tk.SUNKEN,command=self.update_dot)
        bt.grid(row=5,column=1,sticky=tk.NSEW)
    def create_x_divide(self):
        bt=tk.Button(self.buttons_f,text="1/x",bg="#191919",fg=off_white,font="Arial 14", borderwidth=0,relief=tk.SUNKEN,command=self.update_dot)
        bt.grid(row=1,column=1,sticky=tk.NSEW)
    def create_x_square(self):
        bt=tk.Button(self.buttons_f,text="x\u00b2",bg="#191919",fg=off_white,font="Arial 14", borderwidth=0,relief=tk.SUNKEN,command=self.update_square)
        bt.grid(row=1,column=2,sticky=tk.NSEW)
    def create_x_root(self):
        bt=tk.Button(self.buttons_f,text="\u221ax",bg="#191919",fg=off_white,font="Arial 14", borderwidth=0,relief=tk.SUNKEN,command=self.update_x_root)
        bt.grid(row=1,column=3,sticky=tk.NSEW)
    def create_backspace(self):
        bt=tk.Button(self.buttons_f,text="\u232b",bg="#191919",fg=off_white,font="Arial 12", borderwidth=0,relief=tk.SUNKEN,command=self.update_backspace)
        bt.grid(row=0,column=4,sticky=tk.NSEW)
    
    def create_special(self):
        self.create_equal()
        self.create_empty()
        self.create_percent()
        self.create_CE()
        self.create_AC()
        self.create_dot()
        self.create_x_divide()
        self.create_x_square()
        self.create_x_root()
        self.create_backspace()

    #functionality
    def update_total_label(self):
        expression=self.his
        for operator ,symbol in self.operators.items():
            expression=expression.replace(operator,f" {symbol} ")
        self.hislabel.config(text=expression)
    def update_label(self):
        self.currentlabel.config(text=self.current[:11])
    def add_to_current(self,value):
        if self.current=="0":
            self.current=""
        self.current+=str(value)
        self.update_label()
    def append_operator(self,operator):
        self.current+=operator
        self.his+=self.current
        self.current=""
        self.update_total_label()
        self.update_label()
    def clear_all(self):
        self.his=""
        self.current=""
        self.update_label()
        self.update_total_label()
    def clear(self):
        self.current=""
        self.update_label()
    def evaluate(self):
        self.temp=self.his+self.current
        self.his=self.his+self.current+"="
        self.update_total_label()
        try:
            self.current=str(eval(self.temp))
            self.update_label()
        except Exception as e:
            self.his=""
            self.current="ERROR"
        finally:
            self.update_total_label()
            self.update_label()
    def update_dot(self):
        self.current+="."
        self.update_label()
    def update_square(self):
        self.his="sqrt("+str(self.current)+")"
        self.current=int(self.current)*int(self.current)
        #or self.current=str(eval(f"{self.current}**2"))
        self.update_total_label()
        self.update_label()
    def update_x_root(self):
        self.his="\u221a"+"("+str(self.current)+")"
        self.current=str(eval(f"{self.current}**0.5"))
        self.update_total_label()
        self.update_label()
    def update_backspace(self):
        temp=int(self.current)
        temp=int(temp/10)
        self.current=str(temp)
        self.update_label()
    def update_percent(self):
        temp=float(self.current)
        temp=temp/100
        self.current=str(temp)
        self.update_label()


    #binding with keyboard
    def keys_bind(self):
        self.window.bind("<Return>",lambda event:self.evaluate())
        for key in self.numbers:
            self.window.bind(str(key),lambda event,digit=key: self.add_to_current(digit))
        for key in self.operators:
            self.window.bind(key,lambda event,operator=key: self.append_operator(operator))
if __name__=='__main__':
    app=calculator()
    app.run()