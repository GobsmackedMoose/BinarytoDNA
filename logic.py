from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_Form):
     def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.sub())
        
     def sub(self):
         inn = self.lineEdit.text()
         try:
            in_type = self.buttonGroup.checkedButton().text()
            out_type = self.buttonGroup_2.checkedButton().text()
         except:
            self.label_5.setText("Please select input and output types.")
         try: 
            self.label_5.setWordWrap(True)
            self.label_5.setText(f'{in_type}  {out_type}') #clear output before new output is put in

            if in_type == "Alphabet" and out_type == "Binary":
               self.label_5.setText(str_binary(inn))
            elif in_type == "Binary" and out_type == "Alphabet":
               self.label_5.setText(binary_str(inn))
            elif in_type == "DNA Bases" and out_type == "Binary":
               self.label_5.setText(dna_binary(inn))
            elif in_type == "Binary" and out_type == "DNA Bases":
               self.label_5.setText(binary_dna(inn))
            elif in_type == "Alphabet" and out_type == "DNA Bases":
               self.label_5.setText(str_dna(inn))
            elif in_type == "DNA Bases" and out_type == "Alphabet":
               self.label_5.setText(dna_str(inn))
         except:
             self.label_5.setText("Invalid input. Please try again.")

        



def binary_str(inp):
    print("binary to string")
    print(inp)
    
    return chr(int(inp, 2)) # google gemini 

def str_binary(inp):
    out = ''.join(format(ord(char), '08b') for char in inp)
    return out
    #source: https://www.geeksforgeeks.org/python/python-convert-string-to-binary/ 

def dna_binary(inp):
    inp = inp.lower().split(",")
    outp = ""
    for i in inp:
        if i == "adenine":
            outp += "00"
        elif i == "thymine":
            outp += "11"
        elif i == "cytosine":
            outp += "10"
        elif i == "guanine":
            outp += "01"
    return outp

def binary_dna(inp):
    outp = ""
    for i in range(0, len(inp), 2):
        pair = inp[i:i+2]
        if pair == "00":
            outp += "Adenine, "
        elif pair == "11":
            outp += "Thymine, "
        elif pair == "10":
            outp += "Cytosine, "
        elif pair == "01":
            outp += "Guanine, "
    return outp[:-2]  # Remove the trailing comma

def str_dna(inp):
    inp = str_binary(inp)
    return binary_dna(inp)

def dna_str(inp):
    inp = dna_binary(inp)
    return binary_str(inp.encode('utf-8')) #https://www.askpython.com/python/examples/binary-to-utf8-conversion for encode 
