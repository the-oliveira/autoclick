import tkinter as tk
import threading
import time
import pyautogui

class AutoClicker:
    def __init__(self, master):
        self.master = master
        master.title("Autoclicker")

        self.running = False  # Controla o estado do autoclicker

        # Label e campo para definir o número de cliques por segundo
        self.rate_label = tk.Label(master, text="Cliques por segundo:")
        self.rate_label.pack(pady=5)

        self.click_rate_entry = tk.Entry(master, width=10)
        self.click_rate_entry.insert(0, "10")  # Valor padrão: 10 cliques/s
        self.click_rate_entry.pack(pady=5)

        # Botões para iniciar e parar o autoclicker
        self.start_button = tk.Button(master, text="Iniciar", command=self.start_clicking)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(master, text="Parar", command=self.stop_clicking)
        self.stop_button.pack(pady=5)

        # Label de status para auxiliar no debug
        self.status_label = tk.Label(master, text="Status: Parado")
        self.status_label.pack(pady=5)

    def start_clicking(self):
        if not self.running:
            self.running = True
            self.status_label.config(text="Status: Clicando")
            threading.Thread(target=self.click_loop, daemon=True).start()

    def stop_clicking(self):
        self.running = False
        self.status_label.config(text="Status: Parado")

    def click_loop(self):
        try:
            clicks_per_sec = float(self.click_rate_entry.get())
            delay = 1.0 / clicks_per_sec
        except ValueError:
            delay = 0.1  # Delay padrão se o valor for inválido

        while self.running:
            pyautogui.click()  # Realiza o clique
            time.sleep(delay)  # Aguarda o intervalo definido

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoClicker(root)
    root.mainloop()
