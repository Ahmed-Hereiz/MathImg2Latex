import tkinter as tk
from PIL import Image, ImageEnhance, ImageOps
import os  

def gui_draw():
    def draw(event):
        x, y = event.x, event.y
        canvas.create_oval(x-5, y-5, x+5, y+5, fill="black")  

    def enhance_image(image_path):
        img = Image.open(image_path).convert("L")  
        img = img.resize((512, 512), Image.Resampling.LANCZOS)
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2.0)  
        img = ImageOps.autocontrast(img)
        return img

    def save_image():
        canvas.postscript(file="temp.eps")  
        img = Image.open("temp.eps")
        img.save("math2latex.png")
        os.remove("temp.eps")  

        enhanced_img = enhance_image("math2latex.png")
        enhanced_img.save("math2latex.png")
        window.destroy()  

    window = tk.Tk()
    window.title("Math Equation Drawer")
    window.geometry("1000x800")

    canvas = tk.Canvas(window, bg="white", width=1000, height=750)
    canvas.pack()

    canvas.bind("<B1-Motion>", draw)

    save_button = tk.Button(window, text="Save Image", command=save_image)
    save_button.pack(pady=10)

    window.bind("<Control-s>", lambda event: save_image())  
    window.mainloop()
