import re
text_to_search = '''
 abcdefghijklmnopqrstuvwxyz
 ABCDEFGHIJKLMNOPQRSTUVWXYZ
 1234567890
 
 Ha HaHa
 
 MetaCharacters (Need to be escaped):
 . ^ $ * + ? { } [ ] \ | ( )
 
 coreyms.com
 321-555-4321
 123.555.1234
 
 Mr. Schafer 
 Mr Smoth
 Ms Davis
 Mrs. Robinson
 Mr. T
'''

sentence = 'Start a sentennce and bring it to end'

#pattern = re.compile(r'abc')
#pattern = re.compile(r'coreyms\.com')
#pattern = re.compile(r'\d')
#pattern = re.compile(r'end$')
#pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
#pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')    #grouping in regEX

pattern = re.compile(r'Start')
matches = pattern.match(sentence)
print(matches)

#for match in matches:
    #print(match)

#with open('data.txt','r') as f:
    #content = f.read()
    #matches = pattern.finditer(content)
    #for match in matches:
        #print(match)
    
