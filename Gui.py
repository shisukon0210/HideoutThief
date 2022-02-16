from tkinter import *
from PIL import Image, ImageTk
import HideoutThief

class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.title('HideoutThief')
        self.text1 = Label(self.root, text="原始藏身處(含副檔名): ")
        self.text1.grid(row=0, column=0)
        self.input_hideout1 = Entry(self.root)
        self.input_hideout1.grid(row=0, column=1)
        self.text2 = Label(self.root, text="欲移動至藏身處(含副檔名): ")
        self.text2.grid(row=1, column=0)
        self.input_hideout2 = Entry(self.root)
        self.input_hideout2.grid(row=1, column=1)
        self.text3 = Label(self.root, text="以下輸入座標偏移(新的減去舊的)")
        self.text3.grid(row=2, column=0)
        self.text4 = Label(self.root, text="X")
        self.text4.grid(row=3, column=0)
        self.input_x = Entry(self.root)
        self.input_x.grid(row=3, column=1)
        self.text5 = Label(self.root, text="Y")
        self.text5.grid(row=4, column=0)
        self.input_y = Entry(self.root)
        self.input_y.grid(row=4, column=1)
        self.btn1 = Button(self.root, text="開始搬運", command=self.move)
        self.btn1.grid(row=5, column=1)
        self.text6 = Label(self.root, text="Copyright © 2021 shisukon0210.")
        self.text6.grid(row=6)
        self.img_open = Image.open('./icon/kuso_pekora.png')
        self.img1= ImageTk.PhotoImage(self.img_open)
        self.label_img = Label(self.root, image=self.img1)
        self.label_img.grid(row=0, rowspan=6, column=2, padx=5, pady=5)

    def move(self):
        fname = self.input_hideout1.get()
        fname2 = self.input_hideout2.get()
        x = self.input_x.get()
        y = self.input_y.get()
        HideoutThief.hideoutMoving(fname, fname2, int(x), int(y))

if __name__ == "__main__":
    G = Gui()
    mainloop()