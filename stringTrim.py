strOut = ""

def stringTrim(str):
    strSplit = str.split("\n")
    global strOut
    for i in strSplit:
        if len(i)!=0:
             strOut= '\t\t'+i+'\n' +strOut

    return strOut
