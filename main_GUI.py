import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter import ttk
from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image, ImageTk
from io import BytesIO
import subprocess

# Language support
LANGUAGES = {
    'en': {
        'title': 'Barcode Generator',
        'select_file': 'Select .barcode File',
        'select_directory': 'Select Directory to Save Images',
        'edit_file': 'Edit .barcode File',
        'generate': 'Generate Barcodes',
        'language': 'Languages',
        'close': 'Close',
        'default_file': 'main.barcode',
        'default_directory': 'images'
    },
    'zh': {
        'title': '条形码生成器',
        'select_file': '选择.barcode文件',
        'select_directory': '选择保存图片的目录',
        'edit_file': '编辑.barcode文件',
        'generate': '生成条形码',
        'language': '简体中文',
        'close': '关闭',
        'default_file': 'main.barcode',
        'default_directory': 'images'
    }
}

class BarcodeGeneratorApp:
    def __init__(self, master, lang='en'):
        self.master = master
        self.lang = lang
        self.file_path = ''
        self.output_dir = ''
        
        self.create_widgets()
        self.set_language(lang)
    
    def set_language(self, lang):
        self.lang = lang
        self.update_texts()
    
    def update_texts(self):
        self.master.title(LANGUAGES[self.lang]['title'])
        self.select_file_button.config(text=LANGUAGES[self.lang]['select_file'])
        self.select_directory_button.config(text=LANGUAGES[self.lang]['select_directory'])
        self.edit_file_button.config(text=LANGUAGES[self.lang]['edit_file'])
        self.generate_button.config(text=LANGUAGES[self.lang]['generate'])
        self.language_menu.entryconfig(0, label="English")
        self.language_menu.entryconfig(1, label="简体中文")
        self.close_button.config(text=LANGUAGES[self.lang]['close'])
    
    def create_widgets(self):
        frame_buttons = ttk.Frame(self.master)
        frame_buttons.pack(pady=10)
        
        self.select_file_button = ttk.Button(frame_buttons, text='', command=self.select_file)
        self.select_file_button.pack(fill=tk.X, pady=5)
        
        self.select_directory_button = ttk.Button(frame_buttons, text='', command=self.select_directory)
        self.select_directory_button.pack(fill=tk.X, pady=5)
        
        self.edit_file_button = ttk.Button(frame_buttons, text='', command=self.edit_file)
        self.edit_file_button.pack(fill=tk.X, pady=5)
        
        self.generate_button = ttk.Button(frame_buttons, text='', command=self.generate_barcodes)
        self.generate_button.pack(fill=tk.X, pady=5)
        
        menubar = tk.Menu(self.master)
        self.language_menu = tk.Menu(menubar, tearoff=0)
        self.language_menu.add_command(label="English", command=lambda: self.set_language('en'))
        self.language_menu.add_command(label="简体中文", command=lambda: self.set_language('zh'))
        menubar.add_cascade(label=LANGUAGES[self.lang]['language'], menu=self.language_menu)
        self.master.config(menu=menubar)
        
        self.close_button = ttk.Button(frame_buttons, text='', command=self.master.quit)
        self.close_button.pack(fill=tk.X, pady=5)
    
    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Barcode files", "*.barcode")])
        if not self.file_path:
            self.file_path = LANGUAGES[self.lang]['default_file']
            if not os.path.exists(self.file_path):
                with open(self.file_path, 'w', encoding='utf-8') as file:
                    file.write("")  # 创建空文件
    
    def select_directory(self):
        self.output_dir = filedialog.askdirectory()
        if not self.output_dir:
            self.output_dir = LANGUAGES[self.lang]['default_directory']
            os.makedirs(self.output_dir, exist_ok=True)
    
    def edit_file(self):
        editor_choices = ['vim', 'nvim', 'vscode', 'notepad']
        editor = simpledialog.askstring("Editor Choice", "Choose an editor:\n" + "\n".join(editor_choices))
        if editor and editor in editor_choices:
            try:
                subprocess.run([editor, self.file_path])
            except FileNotFoundError:
                messagebox.showerror("Error", f"The editor '{editor}' is not installed or not found in your PATH.")
        else:
            messagebox.showwarning("Invalid Editor", "Please choose a valid editor.")
    
    def generate_barcodes(self):
        if not os.path.exists(self.file_path):
            messagebox.showerror("File Error", "The selected .barcode file does not exist.")
            return
        
        os.makedirs(self.output_dir, exist_ok=True)
        
        with open(self.file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        for idx, line in enumerate(lines):
            content = line.strip()
            
            barcode = Code128(content, writer=ImageWriter())
            buffer = BytesIO()
            barcode.write(buffer)
            buffer.seek(0)
            
            barcode_image = Image.open(buffer)
            barcode_image = barcode_image.resize((600, 400), Image.LANCZOS)
            
            new_image = Image.new('RGB', (600, 400), 'white')
            new_image.paste(barcode_image, (0, 0))
            
            final_image_path = os.path.join(self.output_dir, f'final_barcode_{idx}.png')
            new_image.save(final_image_path)
            
            buffer.close()
        
        messagebox.showinfo("Success", "Barcodes have been successfully generated.")
    
    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = BarcodeGeneratorApp(root)
    app.run()