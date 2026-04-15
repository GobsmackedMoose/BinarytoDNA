

# using: https://www.askpython.com/python/examples/binary-to-utf8-conversion for encode and decode



def binary_str(inp):
    return inp.decode('utf-8')

def str_binary(inp):
    out = ''.join(format(ord(char), '08b') for char in inp)
    return out

    #source: https://www.geeksforgeeks.org/python/python-convert-string-to-binary/ 

def main():
    
    print(str_binary("hiiiii"))
    binput = str_binary("hiiiii")
    
    print(binary_str(binput.encode('utf-8')))

if __name__ == "__main__":
    main()