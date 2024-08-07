import tkinter as tk
from tkinter import ttk, messagebox
import base64
import webbrowser

class EncoderDecoderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Encoder/Decoder")

        self.encoded_history = []
        self.decoded_history = []

        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.menu = tk.Menu(root)
        root.config(menu=self.menu)
        self.history_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="History", menu=self.history_menu)
        self.history_menu.add_command(label="View Encoded History", command=self.view_encoded_history)
        self.history_menu.add_command(label="View Decoded History", command=self.view_decoded_history)

        self.input_label = ttk.Label(self.frame, text="Input Text:")
        self.input_label.grid(row=0, column=0, sticky=tk.W)
        self.input_text = tk.Text(self.frame, height=5, width=40)
        self.input_text.grid(row=1, column=0, columnspan=2)

        self.encode_button = ttk.Button(self.frame, text="Encode", command=self.encode_text)
        self.encode_button.grid(row=2, column=0, pady=10, padx=10, sticky=tk.EW)

        self.decode_button = ttk.Button(self.frame, text="Decode", command=self.decode_text)
        self.decode_button.grid(row=2, column=1, pady=10, padx=10, sticky=tk.EW)

        self.output_label = ttk.Label(self.frame, text="Output Text:")
        self.output_label.grid(row=3, column=0, columnspan=2, sticky=tk.W)
        self.output_text = tk.Text(self.frame, height=5, width=40)
        self.output_text.grid(row=4, column=0, columnspan=2)

        self.donate_button = ttk.Button(self.frame, text="Donate Us", command=self.open_donation_page)
        self.donate_button.grid(row=6, column=1, pady=10, sticky=(tk.E, tk.S))
        
        self.about_button = ttk.Button(self.frame, text="About Us", command=self.open_github_page)
        self.about_button.grid(row=6, column=0, pady=10, sticky=(tk.W, tk.S))
        
        self.dev_label = ttk.Label(self.frame, text="Developed by Ebad Mahar", font=("Arial", 10))
        self.dev_label.grid(row=5, column=0, columnspan=2, pady=10, sticky=tk.S)

    def encode_text(self):
        input_data = self.input_text.get("1.0", tk.END).strip()
        if input_data:
            encoded_data = base64.b64encode(input_data.encode()).decode()
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, encoded_data)
            self.encoded_history.append(encoded_data)
        else:
            messagebox.showwarning("Input Error", "Please enter text to encode.")

    def decode_text(self):
        input_data = self.input_text.get("1.0", tk.END).strip()
        if input_data:
            try:
                decoded_data = base64.b64decode(input_data).decode()
                self.output_text.delete("1.0", tk.END)
                self.output_text.insert(tk.END, decoded_data)
                self.decoded_history.append(decoded_data)
            except Exception as e:
                messagebox.showerror("Decoding Error", f"Failed to decode text. Error: {e}")
        else:
            messagebox.showwarning("Input Error", "Please enter text to decode.")

    def view_encoded_history(self):
        self.show_history_window("Encoded History", self.encoded_history)

    def view_decoded_history(self):
        self.show_history_window("Decoded History", self.decoded_history)

    def show_history_window(self, title, history_list):
        history_window = tk.Toplevel(self.root)
        history_window.title(title)
        history_window.geometry("400x300")

        history_text = tk.Text(history_window, wrap=tk.WORD)
        history_text.pack(expand=True, fill=tk.BOTH)

        if history_list:
            history_text.insert(tk.END, "\n".join(history_list))
        else:
            history_text.insert(tk.END, "No history available.")

    def open_donation_page(self):
        webbrowser.open("https://buymeacoffee.com/maharebad")
    def open_github_page(self):
        webbrowser.open("https://github.com/ebadmahar")

def show_splash_screen(root):
    splash = tk.Toplevel(root)
    splash.title("Loading")
    splash.geometry("300x100")
    splash.configure(bg='white')

    progress = ttk.Progressbar(splash, mode='indeterminate')
    progress.pack(expand=True, fill=tk.X, padx=20, pady=20)
    progress.start()

    label = ttk.Label(splash, text="Your System Sucks..... Upgrade it....", font=("Arial", 9))
    label.pack()

    root.after(2000, lambda: (splash.destroy(), root.deiconify()))

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    show_splash_screen(root)

    app = EncoderDecoderApp(root)
    root.mainloop()
