#Theres Burns and Viviana A
def replace_substring(string, substring, replacement):
    index=0
    output=[]
    while index<len(string):
        if string[index:index+len(substring)]==substring:
            index+=len(substring)
            output.append(replacement)
            index+=1
        else:
            output.append(string[index])
            index+=1
    print("".join(output))        
replace_substring("SPAM!HelloSPAM! worldSPAM!!", "SPAM!", "HI")
