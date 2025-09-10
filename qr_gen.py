import qrcode
from PIL import ImageFont, ImageDraw
import tkinter as tk
from tkinter import messagebox

def generate_qr_code(name, id_no):
    data = f"Name: {name}\nId.No: {id_no}"
    
    # Create QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    qr_img = qr_img.convert("RGB")
    qr_img_width, qr_img_height = qr_img.size
    
    # Add ID number label at the bottom
    label_font_size = qr_img_width // 20
    try:
        label_font = ImageFont.truetype("arial.ttf", label_font_size)
    except:
        label_font = ImageFont.load_default()
    
    draw = ImageDraw.Draw(qr_img)
    label_text = f"Id-No: {id_no}"
    
    label_bbox = draw.textbbox((0, 0), label_text, font=label_font)
    label_width, label_height = label_bbox[2] - label_bbox[0], label_bbox[3] - label_bbox[1]
    label_position = (qr_img_width // 2 - label_width // 2, qr_img_height - label_height - 10)
    
    draw.text(label_position, label_text, font=label_font, fill=(0, 0, 0))
    
    # Save with candidate name
    filename = f"{name}.png"
    qr_img.save(filename)
    messagebox.showinfo("Success", f"QR Code saved as {filename}")

# GUI Part
def submit():
    name = entry_name.get().strip()
    id_no = entry_id.get().strip()
    if not name or not id_no:
        messagebox.showerror("Error", "Please enter both Name and ID.")
        return
    generate_qr_code(name, id_no)

# Tkinter Window
root = tk.Tk()
root.title("QR Code Generator")

tk.Label(root, text="Candidate Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Candidate ID:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_id = tk.Entry(root, width=30)
entry_id.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Generate QR Code", command=submit, bg="green", fg="white").grid(row=2, columnspan=2, pady=10)

root.mainloop()
