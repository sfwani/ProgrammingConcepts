'''
Description:
The user controls the names of both input and output files for this program, which encrypts the contents of a specified file using a dictionary and writes the encrypted result to a separate output file.
'''
Encrypt_Code = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
'@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
'%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
'*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
"'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
'{':'[','[':'{','}':']',']':'}'}

input_file_name = input('What is the name of the file you want to encrypt (type the file name without the .txt extension)?\n')
output_file_name = input('What do you want the output file to be named? (do not write the extension)\n')

output_file = str(output_file_name + '.txt')
input_f = open(input_file_name + '.txt')
content = input_f.read()

def Encrypt(content):
    encrypted_string = ''
    for character in content:
        if character.isspace():
            encrypted_string += ' '
            continue
        encrypted_string += Encrypt_Code[character]
    
    return encrypted_string

output_f = open(output_file, mode='w')
output_f.write(Encrypt(content))
output_f.close()