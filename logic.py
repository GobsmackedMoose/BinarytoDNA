import csv
import os

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
            self.label_5.setText("") #clear output before new output is put in

            if in_type == "Alphabet" and out_type == "Binary":
               output = str_binary(inn)
               output = " ".join(output[i:i+8] for i in range(0, len(output), 8))
               self.label_5.setText(output)

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
            else: 
                raise ValueError("Invalid input/output type. Select an Input and Output type. Do not use the same type for both input and output.")
         except ValueError as v:
             self.label_5.setText(f"Error: {str(v)} Please correct the input and try again.")
         except UnboundLocalError:
                self.label_5.setText("Please select input and output types.")
         except Exception as e:
            self.label_5.setText(f"An error occurred: {str(e)}")

        #file writer

         if os.path.isfile("output.csv"):

            with open("output.csv", 'a', newline='') as file:
                new_text = csv.writer(file)
                new_text.writerow([inn, f"{in_type} to {out_type}", self.label_5.text()])
         else:
            
            with open("output.csv", 'w', newline='') as file:
                new_text = csv.writer(file)
                new_text.writerow(['Input','Function Used', 'Output'])

                new_text.writerow([inn, f"{in_type} to {out_type}", self.label_5.text()])
        



def binary_str(inp):
    print("binary to string")
    print(inp)
    output = chr(int(inp, 2)) # google gemini. also this is unicode, but its the same for regular ascii stuff so its good for my purposes.  
    
    try: 
        return output
    except ValueError:
        raise ValueError("Invalid binary input. Please ensure the input is valid binary.")

def str_binary(inp): #works
    out = ''.join(format(ord(char), '08b') for char in inp)
    return out
    #source: https://www.geeksforgeeks.org/python/python-convert-string-to-binary/ 

def dna_binary(inp): # works
    inp = inp.lower().split(",")
    outp = ""
    for i in inp:
        if i.strip() == "adenine":
            outp += "00"
        elif i.strip() == "thymine":
            outp += "11"
        elif i.strip() == "cytosine":
            outp += "10"
        elif i.strip() == "guanine":
            outp += "01"
        else:
            raise ValueError(f"Invalid DNA base: {i.strip()}. Please enter Adenine, Thymine, Cytosine, or Guanine.")
    return outp

def binary_dna(inp): #works
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
        else:
            raise ValueError(f"Invalid binary pair: {pair}. Each pair must be 00, 11, 10, or 01.")
    return outp[:-2]  # Remove the trailing comma

def str_dna(inp): # works
    inp = str_binary(inp)
    return binary_dna(inp)

def dna_str(inp): # works
    inp = dna_binary(inp)
    return binary_str(inp) #https://www.askpython.com/python/examples/binary-to-utf8-conversion for encode 
