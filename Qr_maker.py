import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    text = entry.get()
    if not text:
        messagebox.showerror("Input Error", "Please enter text or a URL for the QR code.")
        return
    
    # Generate QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Resize QR code
    try:
        size = int(size_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for size.")
        return
    
    img = img.resize((size, size), Image.LANCZOS)

    # Save QR code to file
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
    if file_path:
        img.save(file_path)
        messagebox.showinfo("Success", f"QR code saved to {file_path}")

        # Display QR code in the window
        img_display = img.resize((200, 200))  # Resize for display in the window
        img_tk = ImageTk.PhotoImage(img_display)
        qr_label.configure(image=img_tk)
        qr_label.image = img_tk  # Keep a reference to avoid garbage collection

# Create the main window
window = tk.Tk()
window.title("QR Code Generator")

# Create widgets
tk.Label(window, text="Enter text or URL:").pack(pady=10)
entry = tk.Entry(window, width=50)
entry.pack(pady=5)

tk.Label(window, text="Enter QR code size (pixels):").pack(pady=10)
size_entry = tk.Entry(window, width=10)
size_entry.insert(0, "300")  # Default size
size_entry.pack(pady=5)

generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

qr_label = tk.Label(window)
qr_label.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
