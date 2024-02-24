import fileinput

def conv(file_name):
    list1=[]
    word=''
    
    # Using fileinput.input() method 
    for line in fileinput.input(files = file_name):
        list1.append(line)
    word=''.join(list1)
    return(word)