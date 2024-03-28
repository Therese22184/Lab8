#Therese Burns and Viviana A
string="SPAM!HelloSPAM! worldSPAM!!"
output=[]
index=0
while index<len(string):
    if string[index:index+5]=="SPAM!":
        index+=5
    else:
        output.append(string[index])
        index+=1
print("".join(output))
def remove_substring(string, substring):
    index=0
    output=[]
    while index<len(string):
        if string[index:index+len(substring)]==substring:
            index+=len(substring)
        else:
            output.append(string[index])
            index+=1
    print("".join(output))        
remove_substring("SPAM!HelloSPAM! worldSPAM!!", "SPAM!")

        
