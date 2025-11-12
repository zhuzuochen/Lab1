import tkinter as tk
import random
import string
from PIL import Image, ImageTk  # 需要安装pillow库

MIN_AVERAGE = 10
MAX_AVERAGE = 15
KEY_LENGTHS = [5, 4, 4]

lbl_key = None

def get_weight(char):
    if char.isdigit():
        return int(char)
    return ord(char.upper()) - ord('A') + 1

def generate_block(length):
    
    max_attempts = 1000
    
    for _ in range(max_attempts):
        
        characters = []
        for _ in range(length):
            if random.random() > 0.5:  
                characters.append(random.choice(string.ascii_uppercase))
            else:
                characters.append(random.choice(string.digits))
        
        block = ''.join(characters)
        total_weight = sum(get_weight(c) for c in block)
        average_weight = total_weight / length
        
        if MIN_AVERAGE <= average_weight <= MAX_AVERAGE:
            return block
    
    return generate_fallback_block(length)

def generate_fallback_block(length):
    while True:
        characters = []
        for _ in range(length):
            if random.random() > 0.5:
                characters.append(random.choice(string.ascii_uppercase))
            else:
                characters.append(random.choice(string.digits))
        
        block = ''.join(characters)
        total_weight = sum(get_weight(c) for c in block)
        average_weight = total_weight / length
        
        if 8 <= average_weight <= 17:
            return block

def generate_key():
    blocks = []
    
    for length in KEY_LENGTHS:
        block = generate_block(length)
        blocks.append(block)
    
    return '-'.join(blocks)

def init_gui():
    root = tk.Tk()
    root.title("CS Key Generator")
    root.geometry("900x600")
    root.resizable(False, False)
    return root

def init_canvas(root):
    """初始化画布和背景图片"""
    try:
        # 使用PIL加载图片（支持webp格式）
        image_path = r"C:\Users\asus\Pictures\Screenshots\.venv\keyArt_tall.webp"
        pil_image = Image.open(image_path)
        
        # 调整图片大小适应窗口
        pil_image = pil_image.resize((900, 600), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(pil_image)
        
        # 创建主画布
        canvas = tk.Canvas(root, width=900, height=600)
        canvas.pack(fill="both", expand=True)
        
        # 添加背景图片
        canvas.create_image(0, 0, image=bg_image, anchor="nw")
        canvas.bg_image = bg_image  # 保持引用，防止被垃圾回收
        
        # 添加半透明层提高文字可读性
        canvas.create_rectangle(0, 0, 900, 600, fill="black", stipple="gray50")
        
        print("背景图片加载成功！")
        return canvas
        
    except Exception as e:
        print(f"Error loading background image: {e}")
        
        # 如果图片加载失败，使用纯色背景
        canvas = tk.Canvas(root, width=900, height=600, bg='#1a1a1a')
        canvas.pack(fill="both", expand=True)
        
        # 添加CS风格的文字
        canvas.create_text(450, 100, text="COUNTER-STRIKE", 
                          font=("Arial", 28, "bold"), 
                          fill="orange")
        canvas.create_text(450, 140, text="KEY GENERATOR", 
                          font=("Arial", 16), 
                          fill="white")
        
        return canvas

def display_key(canvas):
    global lbl_key
    key = generate_key()
    
    if lbl_key and lbl_key.winfo_exists():
        lbl_key.config(text=key)
    else:
        lbl_key = tk.Label(
            canvas,
            text=key,
            font=("Courier", 16, "bold"),
            background='#34495E',
            foreground='#2ECC71',
            relief='raised',
            bd=2,
            padx=20,
            pady=10
        )
        canvas.create_window(450, 300, window=lbl_key)

def init_input(canvas):
    
    btn_generate = tk.Button(
        canvas,
        text='Generate Key',
        font=("Arial", 14),
        command=lambda: display_key(canvas),
        bg='#E74C3C',
        fg='white',
        relief='raised',
        bd=3,
        padx=20,
        pady=10
    )
    canvas.create_window(450, 350, window=btn_generate)

if __name__ == '__main__':
    root = init_gui()
    canvas = init_canvas(root)
    init_input(canvas)
    root.mainloop()