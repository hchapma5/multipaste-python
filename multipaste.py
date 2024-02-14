from tkinter import Tk, Entry, Label, Checkbutton, NORMAL, DISABLED, Toplevel, Button
import threading
from pynput.keyboard import Key, Controller, Listener
import pyperclip
import time
from pynput import keyboard

KEYBIND = keyboard.Key.f8

class MultiPasteGUI:
    def __init__(self, root):
        self.root = root
        self.setup_gui()

    def setup_gui(self):
        self.root.geometry("300x150")
        self.root.title("MultiPaste")

        # Barcode Entry and Label
        Label(self.root, text="Enter SKU:").grid(
            column=0, row=0, sticky="e", padx=10, pady=10
        )
        self.barcode_entry = Entry(self.root, width=20)
        self.barcode_entry.grid(column=1, row=0, padx=10, pady=10)
        self.barcode_lock = Checkbutton(
            self.root, text="Lock", command=self.toggle_barcode_lock
        )
        self.barcode_lock.grid(column=2, row=0)

        # Quantity Entry and Label
        Label(self.root, text="Qty:").grid(
            column=0, row=1, sticky="e", padx=10, pady=10
        )
        self.quantity_entry = Entry(self.root, width=20)
        self.quantity_entry.grid(column=1, row=1, padx=10, pady=10)
        self.quantity_lock = Checkbutton(
            self.root, text="Lock", command=self.toggle_quantity_lock
        )
        self.quantity_lock.grid(column=2, row=1)

        # Keybind Label
        Label(self.root, text=f"Press {KEYBIND} to start pasting").grid(
            column=1, row=2, pady=10
        )

    def toggle_barcode_lock(self):
        state = DISABLED if self.barcode_entry["state"] == NORMAL else NORMAL
        self.barcode_entry.config(state=state)

    def toggle_quantity_lock(self):
        quantity_str = self.quantity_entry.get()
        if not quantity_str.isdigit():
            self.quantity_lock.deselect()
            self.show_error("Invalid input, quantity must be a positive integer.")
            return
        state = DISABLED if self.quantity_entry["state"] == NORMAL else NORMAL
        self.quantity_entry.config(state=state)

    def show_error(self, message):
        error_window = Toplevel(self.root)
        error_window.title("Error")
        Label(error_window, text=message, fg="red").pack(padx=20, pady=20)
        Button(error_window, text="OK", command=error_window.destroy).pack(pady=10)


class KeyboardListener:
    def __init__(self, gui):
        self.kb = keyboard.Controller()
        self.gui = gui
        self.listener_thread = threading.Thread(
            target=self.start_keyboard_listener, daemon=True
        )
        self.listener_thread.start()

    def start_keyboard_listener(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

    def on_press(self, key):
        if key == KEYBIND:
            barcode = self.gui.barcode_entry.get()
            quantity_str = self.gui.quantity_entry.get()
            if barcode and quantity_str.isdigit():
                quantity = int(quantity_str)
                threading.Thread(target=self.simulate_typing, args=(barcode, quantity), daemon=True).start()
            else:
                self.gui.show_error("Invalid input, quantity must be a positive integer.")

    def simulate_typing(self, barcode, quantity):
        pyperclip.copy(barcode)
        for _ in range(quantity):
            self.kb.press(Key.ctrl)
            self.kb.press("v")
            self.kb.release("v")
            self.kb.release(Key.ctrl)
            time.sleep(0.05)
            self.kb.press(Key.enter)
            self.kb.release(Key.enter)
            time.sleep(0.05)


if __name__ == "__main__":
    root = Tk()
    gui = MultiPasteGUI(root)
    listener = KeyboardListener(gui)
    root.mainloop()