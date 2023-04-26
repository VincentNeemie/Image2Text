import tkinter as tk 
from tkinter import filedialog, scrolledtext 
import pytesseract 
import cv2 
from PIL import Image, ImageGrab 
import os 
import threading 
import clipboard 
 
def ocr(image_path): 
    """ 
    Extracts text from an image using Tesseract OCR. 
    Inputs: 
        image_path (str): The file path of the input image. 
    Outputs: 
        text (str): The extracted text from the image. 
    """ 
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' 
    gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) 
    if gray_image is None: 
        raise ValueError("Failed to read image") 
    with Image.open(image_path) as img: 
        text = pytesseract.image_to_string(img, lang=None, nice=0) 
        return text 
 
def browse_file(): 
    """ 
    Opens a file dialog box to browse for an image file. 
    Inputs: 
        None 
    Outputs: 
        None 
    """ 
    file_path = filedialog.askopenfilename(filetypes=[('Image Files', ('*.jpg', '*.png'))]) 
    if file_path: 
        t = threading.Thread(target=process_image, args=(file_path,)) 
        t.start() 
 
def get_clipboard_image(): 
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
        t = threading.Thread(target=process_image, args=(image_file,)) 
        t.start() 
 
def process_image(image_path): 
    """ 
    Processes the image and extracts text using Tesseract OCR. 
    Inputs: 
        image_path (str): The file path of the input image. 
    Outputs: 
        None 
    """ 
    text_label.configure(state='normal') 
    text_label.delete('1.0', 'end') 
    progress_label.configure(text="Processing...") 
    text = ocr(image_path) 
    text_label.insert('end', text) 
    progress_label.configure(text="") 
    text_label.configure(state='disabled') 
    os.remove(image_path) 
 
def copy_to_clipboard(): 
    """ 
    Copies the text from the text_label widget to the clipboard. 
    Inputs: 
        None 
    Outputs: 
        None 
    """ 
    text = text_label.get('1.0', 'end-1c') 
    clipboard.copy(text) 
 
def resize_font(event): 
    """ 
    Resizes the font of the text_label widget based on the size of the window. 
    Inputs: 
        event: The event that triggered the function call. 
    Outputs: 
        None 
    """ 
    width = event.width 
    height = event.height 
    font_size = int(min(width/25, height/30)) # adjust the fontsize based on the window size 
    text_label.configure(font=('Arial', font_size)) 
 
root = tk.Tk() 
root.geometry('400x400') 
root.title('OCR Image') 
 
button_frame = tk.Frame(root) 

browse_button = tk.Button(button_frame, text='Browse', command=browse_file) 
browse_button.pack(side='left', padx=10, pady=10) 
 
clipboard_button = tk.Button(button_frame, text='Get from Clipboard', command=get_clipboard_image) 
clipboard_button.pack(side='left', padx=10, pady=10) 
 
copy_button = tk.Button(button_frame, text='Copy to Clipboard', command=copy_to_clipboard) 
copy_button.pack(side='left', padx=10, pady=10) 

button_frame.pack()

text_label = scrolledtext.ScrolledText(root, font=('Arial', 12), wrap='word', width=45, height=30) 
text_label.pack(fill='both', expand=True, pady=20) 
 
progress_label = tk.Label(root, text="") 
progress_label.pack(side="bottom") 
 
root.bind('<Configure>', resize_font) 
 
root.mainloop()