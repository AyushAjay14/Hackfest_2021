import tkinter as tk
import final_amazon

HEIGHT = 600
WIDTH = 600
def final_callback(product,attri,lowr,uppr):
    list1=final_amazon.start(product,attri,lowr,uppr)
    name = list1[0]
    str = "The recommended product is \n" , name.replace('{' ,'').replace("}", "" )

    label['text'] = str


root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
bg_image = tk.PhotoImage(file='egim.png')
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)
frame = tk.Frame(root, bg="#ff99ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.08, anchor='n')
product = tk.Entry(frame, font=('Bahnschrift', 18))
product.place(relx=0, relwidth=0.23, relheight=1)
attri = tk.Entry(frame, font=('Bahnschrift', 18))
attri.place(relx=0.25, relwidth=0.23, relheight=1)
lowr = tk.Entry(frame, font=('Bahnschrift', 18))
lowr.place(relx=0.50, relwidth=0.23, relheight=1)
uppr = tk.Entry(frame, font=('Bahnschrift', 18))
uppr.place(relx=0.75, relwidth=0.23, relheight=1)
button = tk.Button(root, text="GO!", font=('Bahnschrift', 12),command=lambda: [final_callback(product.get(), attri.get(), lowr.get(), uppr.get())])
button.place(relx=0.5, rely=0.21, relheight=0.06, relwidth=0.3, anchor='n')
frame2 = tk.Frame(root, bg='#80bfff', bd=10)
frame2.place(relx=0.5, rely=0.3, relheight=0.6, relwidth=0.9, anchor='n')
label = tk.Label(frame2, font=('Bahnschrift', 12))
label.place(relwidth=1, relheight=1, relx=0, rely=0)


root.mainloop()
