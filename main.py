import tkinter
import buttonCommands.buttonFunction as buttonInfo


def button_clicked():
    print("Button Clicked!!")

def tkinterSetUp():
    root = tkinter.Tk()
    root.title("Simple Bugeting")
    root.configure(background="lightblue")
    root.minsize(300, 200)
    root.maxsize(800,600)
    root.geometry("400x400")
    
    needsofButton = buttonInfo.ButtonFunction

    w = tkinter.Label(root, text="Simple Bugeting")

    button1 = tkinter.Button(root, text="Click Button", command=needsofButton.button_clicked, 
                            activebackground="blue", activeforeground="white",
                            anchor="center", bd=3, bg="lightgray", cursor="hand2",
                            disabledforeground="gray", fg="black", font=("Arial", 12),
                            height=2, highlightbackground="black", highlightcolor="green",
                            highlightthickness=2, justify="center", overrelief="raised",
                            padx=10, pady=5, width=15, wraplength=100)
    

    button = tkinter.Button(root, text="Stop", command=root.destroy, 
                            activebackground="blue", activeforeground="white",
                            anchor="center", bd=3, bg="lightgray", cursor="hand2",
                            disabledforeground="gray", fg="black", font=("Arial", 12),
                            height=2, highlightbackground="black", highlightcolor="green",
                            highlightthickness=2, justify="center", overrelief="raised",
                            padx=10, pady=5, width=15, wraplength=100)
    
    w.pack()
    button1.pack(padx=20, pady=20)
    button.pack(padx=20, pady=20)
    root.mainloop()

def main():
    print("Welcome to Simple Bugeting")
    tkinterSetUp()

main()