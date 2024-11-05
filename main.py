import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import os

# START DONATION CODE
from tkinter import messagebox
from random import randint
import sys


#if randint(0,3) == 1 and not "--no-popup" in sys.argv:
   # messagebox.showinfo("BirdOffice 24.11", "Thank you for downloading BirdEncrypt! If you like this software, make sure to donate at www.mojavesoft.net/donate/!")


# END DONATION CODE

def generate_key():
    key = Fernet.generate_key()
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key.decode())
    log_message("Key generated in memory.")

def load_key():
    try:
        key_path = filedialog.askopenfilename(title="Select Key File", filetypes=[("Key Files", "*.key")])
        with open(key_path, "rb") as key_file:
            key = key_file.read()
        key_entry.delete(0, tk.END)
        key_entry.insert(0, key.decode())
        log_message("Key loaded successfully.")
    except Exception as e:
        log_message(f"Error loading key: {e}")

def save_key():
    try:
        key = key_entry.get().encode()
        key_path = filedialog.asksaveasfilename(defaultextension=".key", title="Save Key File", filetypes=[("Key Files", "*.key")])
        with open(key_path, "wb") as key_file:
            key_file.write(key)
        log_message("Key saved successfully.")
    except Exception as e:
        log_message(f"Error saving key: {e}")

def encrypt_file():
    try:
        file_path = filedialog.askopenfilename(title="Select File to Encrypt")
        if not file_path:
            return  # If user cancels the dialog

        key = key_entry.get().encode()
        fernet = Fernet(key)

        with open(file_path, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        # Ask user where to save the encrypted file
        save_path = filedialog.asksaveasfilename(defaultextension=".enc", title="Save Encrypted File")
        if not save_path:
            return  # If user cancels the dialog

        with open(save_path, "wb") as encrypted_file:
            encrypted_file.write(encrypted)
        log_message(f"File encrypted successfully and saved to {save_path}.")
    except Exception as e:
        log_message(f"Error encrypting file: {e}")

def decrypt_file():
    try:
        file_path = filedialog.askopenfilename(title="Select File to Decrypt")
        if not file_path:
            return  # If user cancels the dialog

        key = key_entry.get().encode()
        fernet = Fernet(key)

        with open(file_path, "rb") as encrypted_file:
            encrypted = encrypted_file.read()

        decrypted = fernet.decrypt(encrypted)

        # Ask user where to save the decrypted file
        save_path = filedialog.asksaveasfilename(defaultextension=".dec", title="Save Decrypted File")
        if not save_path:
            return  # If user cancels the dialog

        with open(save_path, "wb") as decrypted_file:
            decrypted_file.write(decrypted)
        log_message(f"File decrypted successfully and saved to {save_path}.")
    except Exception as e:
        log_message(f"Error decrypting file: {e}")

def log_message(message):
    global has_logged
    print(has_logged)
    if not has_logged:
        log_text.delete(1.0, tk.END)  # Clear the text box
        has_logged = True
    log_text.insert(tk.END, message + "\n")
    log_text.see(tk.END)


has_logged = False
root = tk.Tk()
root.title("BirdEncrypt for Business")
root.geometry("800x600")

key_label = tk.Label(root, text="Encryption Key:")
#key_label.pack(pady=5)
key_entry = tk.Entry(root, width=50)
key_entry.pack(pady=5, fill=tk.X)

# Frame for all buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10, fill=tk.X)

# All buttons on a single row
generate_key_button = tk.Button(button_frame, text="Generate Key", command=generate_key, bg='blue', fg='white')
generate_key_button.pack(side=tk.LEFT, expand=True, fill=tk.X)

load_key_button = tk.Button(button_frame, text="Load Key", command=load_key, bg='red', fg='white')
load_key_button.pack(side=tk.LEFT, expand=True, fill=tk.X)

save_key_button = tk.Button(button_frame, text="Save Key", command=save_key, bg='purple', fg='white')
save_key_button.pack(side=tk.LEFT, expand=True, fill=tk.X)

encrypt_button = tk.Button(button_frame, text="Encrypt File", command=encrypt_file, bg='green', fg='white')
encrypt_button.pack(side=tk.LEFT, expand=True, fill=tk.X)

decrypt_button = tk.Button(button_frame, text="Decrypt File", command=decrypt_file, bg='orange', fg='black')
decrypt_button.pack(side=tk.LEFT, expand=True, fill=tk.X)

# Adjust log_text to fill available height and width
log_text = tk.Text(root, height=10, width=70)
log_text.pack(pady=10, fill=tk.BOTH, expand=True)

generate_key()
has_logged = False
log_message("Mojavesoft BirdOffice 24.11, copyright October-November 2024.")

log_message("")
log_message("To begin, load an existing key or generate a new one using the 'Generate Key' button.")

log_message("")
log_message("NEVER send your keys online (except when using end-to-end encryption)!")

log_message("ALWAYS exchange keys offline, optimally hand-to-hand. Avoid using government-operated mailing services.")
log_message("")

log_message("For more security advice, consult a manual.")

has_logged = False

root.mainloop()
