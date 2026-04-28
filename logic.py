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
         """
            sub() is the main logic class for the application.
            It handles the conversion between different data types, and error handling for invalid inputs.
            All other pieces of logic except init are accessed from sub(). It also updates the output.csv. 
         """
         inn = self.lineEdit.text()
         try:
            in_type = self.buttonGroup.checkedButton().text()
            out_type = self.buttonGroup_2.checkedButton().text()
         except:
            self.label_5.setText("Please select input and output types.")
         try: 
            self.label_5.setWordWrap(True)
            self.label_5.setText("") 

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
             self.label_5.setText(f"{str(v)}")
         except UnboundLocalError:
            self.label_5.setText("Please select input and output types.")
            return 
         except Exception as e:
            self.label_5.setText(f"An error occurred: {str(e)}")

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
    """
        This function converts a binary input into a string. It splits input up into bytes because chr() only outputs single characters.
    """
    inp = inp.replace(" ", "")
    if len(inp) % 8 != 0:
        raise ValueError("Invalid binary input. The input must be divisible by 8")
    try: 
        output = ""
        for i in range(0, len(inp), 8):
            byte = inp[i:i+8]
            output += chr(int(byte, 2)) 
    except ValueError:
        raise ValueError("Invalid binary input. Please ensure the input is valid binary and is an appropriate length (each letter is 8 bits)")
    return output



def str_binary(inp): 
    """
        This function converts a string input into binary. 
        Originally encode and decode functions were used but they returned b'' strings 
    """
    out = ''.join(format(ord(char), '08b') for char in inp)
    return out
    #source: https://www.geeksforgeeks.org/python/python-convert-string-to-binary/ 

def dna_binary(inp):
    """
    This function converts a DNA string into binary. It must be seperated by commas.
    """
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




def binary_dna(inp): 
    """ 
    This function converts a binary input into a DNA string. It splits the input into pairs of bits and maps each pair to a DNA base.
    """
    outp = ""
    if len(inp) % 2 != 0:
        raise ValueError("Invalid binary input. The input must be divisible by 2")
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
            raise ValueError(f"Invalid binary input. Please ensure the input is valid binary.")
    return outp[:-2]  # Removes the trailing comma



def str_dna(inp): 
    """
    This function converts a string into a DNA string. These were the last functions created, so they use the previous functions (string to binary and binary to dna) for their action. 
    """
    inp = str_binary(inp)
    return binary_dna(inp)

def dna_str(inp):
    """
    This function converts a DNA string into a string. It uses the previous functions (dna to binary and binary to string) for its action.
    """
    inp = dna_binary(inp)
    return binary_str(inp) 
