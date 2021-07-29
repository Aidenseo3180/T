import tkinter as tk
from tkinter.constants import RAISED

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       label = tk.Label(self, text="This is page 1")

       label.pack(side="top", fill="both", expand=True)

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)


       label = tk.Label(self, text="This is page 2")
       label.pack(side="top", fill="both", expand=True)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)


       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side = "bottom", fill="x", expand=False)   #button들의 프레임 담당
        container.pack(side="top", fill="both", expand=True)        #container의 프레임 담당

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Run the Program", command=p1.show, relief = RAISED)
        b2 = tk.Button(buttonframe, text="How to Use", command=p2.show, relief = RAISED)
        b3 = tk.Button(buttonframe, text="About", command=p3.show, relief = RAISED)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()



if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.title("Twitch Downloader") #창 이름
    root.wm_geometry("400x400+500+100") #창 크기 + x 위치 + y위치
    root.resizable(True, True)  #크기 변경 가능

    root.mainloop()