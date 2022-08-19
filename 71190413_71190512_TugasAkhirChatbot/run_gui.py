from posixpath import split
from tkinter import *
from chatbot_backend import get_respond_from_backend
from auto_correct import correction

BG_GRAY = "#1f3c42"
BG_COLOR = "#91d3ff"
BG_COLOR2 = "#0081d6"
BG_COLOR3 = "#dbdbdb"
TEXT_COLOR = "#e1ffab"
TEXT_COLOR2 = "#ffffff"
TEXT_COLOR3 = "#000000"
TEXT_COLOR4 = "#000000"


FONT = "Ebrima 14"
FONT_BOLD = "Ebrima 15 bold"

FONT_USER = "Ebrima 13"
FONT_BOT = "Ebrima 15 bold"

class MaleoApp:
    
    def __init__(self):
        self.window = Tk()
        self.config_window()
        
    def run(self):
        self.window.mainloop()
        
    def config_window(self):
        self.window.title("MalBot")
        self.window.resizable(width=False, height=False)
        self.window.geometry("720x550")
        self.window.configure(width=720, height=550, bg=BG_COLOR)
        
        # head label
        head_label = Label(self.window, bg=BG_COLOR2, fg=TEXT_COLOR2,
                        text="Maleo ChatBot", font=FONT_BOLD, pady=8)
        head_label.place(relwidth=1)
        
        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.1, relheight=0.012)
        
        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR4,
                                font=FONT_USER, padx=5, pady=5)
        self.text_widget.place(relheight=0.865, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=0.1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        # bottom label
        bottom_label = Label(self.window, bg=BG_COLOR, height=50)
        bottom_label.place(relwidth=1, rely=0.895)
        
        # message entry box
        self.msg_entry = Entry(bottom_label, bg=BG_COLOR3, fg=TEXT_COLOR3, font=FONT_USER)
        self.msg_entry.place(relwidth=0.84, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20,fg='#ffffff', bg=BG_COLOR2,
                            command=lambda: self._on_enter_pressed(None))

        send_button.place(relx=0.87, rely=0.008, relheight=0.06, relwidth=0.12)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "Anda")
        
    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"Anda\t> {msg}\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        # Area Auto Correct
        msgCorrect =""
        arrayMsg = msg.split(" ")
        for kata in arrayMsg:
            msgCorrect+=correction(kata)+" "
        print("Hasil Koreksi : "+msgCorrect)
        
        # Supaya kalau respon memakan area panjang. Maka area terputus
        # Akan menjorok ke dalam atau untuk tab pada harga
        respond = get_respond_from_backend(msgCorrect).split(" ")
        tampungRespond = ""
        for kataRespond in respond:
            if(kataRespond=="~"):
                tampungRespond+="\n\t   "
                continue
            elif(kataRespond=="*"):
                tampungRespond+="\t"
                continue
            tampungRespond+=kataRespond+" "
        msg2 = f"Maleo\t> {tampungRespond}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)
        
if __name__ == "__main__":
    app = MaleoApp()
    app.run()