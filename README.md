# Image2Text 
 
The **Image2Text** class is a graphical user interface (GUI) that allows users to extract text from images using Tesseract OCR. 

<center>
  <img src="https://user-images.githubusercontent.com/92559302/236647407-9e36c923-4efb-4341-be40-c67966f3f184.png" alt="Untitled" style="display: block; margin: auto;">
</center>

## Functionalities !
 
The main functionalities of the class include: 
- Browsing for an image file and extracting text from it 
- Getting an image from the clipboard and extracting text from it 
- Copying the extracted text to the clipboard 
- Resizing the font of the text_label widget based on the size of the window 
 
## Methods 
 
The following methods are defined in the  Image2Text  class: 
 
###  __init__()  
 
Initializes the GUI and sets up the buttons, text label, and progress label. 
 
###  ocr()  
 
Extracts text from an image using Tesseract OCR. 
 
###  browse_file()  
 
Opens a file dialog box to browse for an image file and starts a new thread to process the image. 
 
###  get_clipboard_image()  
 
Gets an image from the clipboard, saves it to a file, and starts a new thread to process the image. 
 
###  process_image()  
 
Processes the image and extracts text using Tesseract OCR, updates the text label and progress label. 
 
###  copy_to_clipboard()  
 
Copies the extracted text to the clipboard. 
 
###  resize_font()  
 
Resizes the font of the text_label widget based on the size of the window. 
 
## Fields 
 
The class has the following fields: 
-  root : the main tkinter window 
-  text_label : the  scrolledtext  widget that displays the extracted text 
-  progress_label : the label that displays the progress of the OCR process.
