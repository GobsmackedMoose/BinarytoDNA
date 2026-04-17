


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


def main():
    
    print(str_binary("h"))
    binput = str_binary("h")

    print(binary_str(binput.encode('utf-8'))) #technically isnt accurate bc everything in the bracelet input would be all caps to make it simpler. 
    #print(dna_binary("Adenine,Thymine,Cytosine,Guanine"))

    #print(binary_dna("0000111101100011"))
    #print(str_dna("hiiiii"))

    print(dna_str("Adenine,Thymine,Cytosine,Guanine"))

if __name__ == "__main__":
    main()