import tkinter as tk

flag = 0
m1 = "THE MATCH IS A TIE"
m2 = "PLAYER X WINS"
m3 = "PLAYER O WINS"

# FUNCTION TO CLOSE WINDOW


def close_application():
    root.destroy()

# FUNCTION TO INSERT EITHER X OR O ALONG WITH CHECKING IF A RESULT HAS OCCURED


def insert(button):
    global flag
    if flag % 2 == 0:
        button.config(text='X', state='disabled', disabledforeground='black')
    else:
        button.config(text='O', state='disabled', disabledforeground='black')
    flag += 1

    if ((b1.cget('text') == 'X' and b2.cget('text') == 'X' and b3.cget('text') == 'X') or ((b4.cget('text') == 'X' and b5.cget('text') == 'X' and b6.cget('text') == 'X')) or (b7.cget('text') == 'X' and b8.cget('text') == 'X' and b9.cget('text') == 'X') or (b1.cget('text') == 'X' and b4.cget('text') == 'X' and b7.cget('text') == 'X') or (b2.cget('text') == 'X' and b5.cget('text') == 'X' and b8.cget('text') == 'X') or (b3.cget('text') == 'X' and b6.cget('text') == 'X' and b9.cget('text') == 'X') or (b1.cget('text') == 'X' and b5.cget('text') == 'X' and b9.cget('text') == 'X') or (b3.cget('text') == 'X' and b5.cget('text') == 'X' and b7.cget('text') == 'X')):
        result_label.config(text=m2)
        root.after(5000, close_application)
    elif ((b1.cget('text') == 'O' and b2.cget('text') == 'O' and b3.cget('text') == 'O') or
          (b4.cget('text') == 'O' and b5.cget('text') == 'O' and b6.cget('text') == 'O') or
          (b7.cget('text') == 'O' and b8.cget('text') == 'O' and b9.cget('text') == 'O') or
          (b1.cget('text') == 'O' and b4.cget('text') == 'O' and b7.cget('text') == 'O') or
          (b2.cget('text') == 'O' and b5.cget('text') == 'O' and b8.cget('text') == 'O') or
          (b3.cget('text') == 'O' and b6.cget('text') == 'O' and b9.cget('text') == 'O') or
          (b1.cget('text') == 'O' and b5.cget('text') == 'O' and b9.cget('text') == 'O') or
            (b3.cget('text') == 'O' and b5.cget('text') == 'O' and b7.cget('text') == 'O')):
        result_label.config(text=m3)
        root.after(5000, close_application)
    elif flag > 8:
        result_label.config(text=m1)
        root.after(5000, close_application)
    else:
        pass


root = tk.Tk()
root.title("TIC-TAC-TOE")

# CREATION OF GAME BOARD FRAME
game_frame = tk.Frame(root, bg='white')
game_frame.pack()

# CREATION OF BUTTONS
b1 = tk.Button(game_frame, text="", width=10, height=5,
               bg="#C0C0FF", command=lambda: insert(b1))
b2 = tk.Button(game_frame, text="", width=10, height=5,
               bg="#C0C0FF", command=lambda: insert(b2))
b3 = tk.Button(game_frame, text="", width=10, height=5,
               bg="#C0C0FF", command=lambda: insert(b3))
b4 = tk.Button(game_frame, text="", width=10, height=5,
               bg="#C0C0FF", command=lambda: insert(b4))
b5 = tk.Button(game_frame, text="", width=10, height=5,
               bg="#C0C0FF", command=lambda: insert(b5))
b6 = tk.Button(game_frame, text="", width=10, height=5,
               bg="#C0C0FF", command=lambda: insert(b6))
b7 = tk.Button(game_frame, text="", width=10, height=5,
               bg="#C0C0FF", command=lambda: insert(b7))
b8 = tk.Button(game_frame, text="", width=10, height=5,
               bg="#C0C0FF", command=lambda: insert(b8))
b9 = tk.Button(game_frame, text="", width=10, height=5,
               bg="#C0C0FF", command=lambda: insert(b9))

# PLACEMENT OF BUTTONS AS A 3X3 GRID
b1.grid(row=0, column=0, padx=5, pady=5)
b2.grid(row=0, column=1, padx=5, pady=5)
b3.grid(row=0, column=2, padx=5, pady=5)
b4.grid(row=1, column=0, padx=5, pady=5)
b5.grid(row=1, column=1, padx=5, pady=5)
b6.grid(row=1, column=2, padx=5, pady=5)
b7.grid(row=2, column=0, padx=5, pady=5)
b8.grid(row=2, column=1, padx=5, pady=5)
b9.grid(row=2, column=2, padx=5, pady=5)

# RESULT FRAME
result_frame = tk.Frame(root, bg='white')
result_frame.pack()

result_label = tk.Label(result_frame, text="")
result_label.pack()

root.mainloop()
