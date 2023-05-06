import tkinter as tk
from tkinter import filedialog, scrolledtext
import threading
import os
import cv2
from PIL import Image, ImageGrab
import pytesseract
import tkinter as tk  
from tkinter import filedialog, scrolledtext  
import pytesseract  
import cv2  
from PIL import Image, ImageGrab  
import os  
import threading  
import clipboard  
from tkinter import messagebox
  
  
class Image2Text:
    def __init__(self):
        self.root = tk.Tk()
        self.root.iconbitmap(os.path.join(os.path.dirname(__file__), 'Image2Text.ico'))
        self.root.geometry('500x400')
        self.root.title('Image2Text')
        self.root.configure(bg='black')  # setting background to black
        self.root.option_add("*Font", "Arial 12 bold")  # making font bold

        button_frame = tk.Frame(self.root, bg='#393939')  # adding a dark gray background to button frame

        browse_button = tk.Button(button_frame, text='Browse', command=self.browse_file, bg='#007BA7', fg='#FFFFFF')  # changing button colors
        browse_button.pack(side='left', padx=10, pady=10)

        clipboard_button = tk.Button(button_frame, text='Get from Clipboard', command=self.get_clipboard_image, bg='#007BA7', fg='#FFFFFF')
        clipboard_button.pack(side='left', padx=10, pady=10)
    
        copy_button = tk.Button(button_frame, text='Copy to Clipboard', command=self.copy_to_clipboard, bg='#007BA7', fg='#FFFFFF')
        copy_button.pack(side='left', padx=10, pady=10)

        button_frame.pack()

        self.text_label = scrolledtext.ScrolledText(self.root, font=('Arial', 12), wrap='word', width=45, height=30, bg='#1C1C1C', fg='#FFFFFF')  # changing text label colors
        self.text_label.pack(fill='both', expand=True, pady=20)

        self.progress_label = tk.Label(self.root, text="", bg='black', fg='#007BA7')  # changing progress label colors
        self.progress_label.pack(side="bottom")

        self.root.bind('<Configure>', self.resize_font)

        with open('C:\\Program Files\\Tesseract-OCR\\tesseract.exe', 'rb') as f:
            pytesseract.pytesseract.tesseract_cmd = f.name


    def ocr(self, image_path):
        """
        Extracts text from an image using Tesseract OCR.
        Inputs:
            image_path (str): The file path of the input image.
        Outputs:
            text (str): The extracted text from the image.
        """
        try:
            gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            if gray_image is None:
                raise ValueError("Failed to read image")
            with Image.open(image_path) as img:
                text = pytesseract.image_to_string(img, lang=None, nice=0)
                return text
        except Exception as e:
            messagebox.showerror("Error", f"Error reading image: {e}")
            return ""

    def browse_file(self):
        """
        Opens a file dialog box to browse for an image file.
        Inputs:
            None
        Outputs:
            None
        """
        try:
            file_path = filedialog.askopenfilename(filetypes=[('All Image Files', '*.*')])
            if file_path:
                t = threading.Thread(target=self.process_image, args=(file_path,))
                t.start()
        except:
            messagebox.showerror("Error", "Could not read the image. Please select another image.")
            self.root.mainloop()

    def get_clipboard_image(self):
        """
        Gets an image from the clipboard.
        Inputs:
            None
        Outputs:
            None
        """
        image = ImageGrab.grabclipboard()
        if image is not None:
            image_file = 'clipboard_image.png'
            image.save(image_file)
            t = threading.Thread(target=self.process_image, args=(image_file,))
            t.start()
        else:
            messagebox.showwarning("Warning", "No image found in clipboard")

    def process_image(self, image_path):
        """
        Processes the image and extracts text using Tesseract OCR.
        Inputs:
            image_path (str): The file path of the input image.
        Outputs:
            None
        """
        self.text_label.configure(state='normal')
        self.text_label.delete('1.0', 'end')
        self.progress_label.configure(text="Processing...")
        text = self.ocr(image_path)
        self.text_label.insert('end', text)
        self.progress_label.configure(text="")
        self.text_label.configure(state='disabled')

    def copy_to_clipboard(self):
        """
        Copies the text from the text_label widget to the clipboard.
        Inputs:
            None
        Outputs:
            None
        """
        text = self.text_label.get('1.0', 'end-1c')
        clipboard.copy(text)

    def resize_font(self, event):
        """
        Resizes the font of the text_label widget based on the size of the window.
        Inputs:
            event: The event that triggered the function call.
        Outputs:
            None
        """
        width = event.width
        height = event.height
        font_size = int(min(width/25, height/30))  # adjust the fontsize based on the window size
        self.text_label.configure(font=('Arial', font_size))
if __name__ == '__main__':
    image2text = Image2Text() 
    image2text.root.mainloop()