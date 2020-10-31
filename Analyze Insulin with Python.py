#first get all lines from file
with open("preproinsulin_seq.txt","r",encoding="utf8") as f:
    lines=f.read()
#Delete “ORIGIN”, “1”, “61”, “//”, and the spaces and return carriages
    lines=lines.replace(' ','')
    lines=lines.replace('61','')
    lines=lines.replace('1','')
    lines=lines.replace('//','')
    lines=lines.replace('\n','')
    lines=lines.replace('\t','')
    lines=lines.replace('ORIGIN','')
#Verify that your file has 110 characters of lowercase letters
    print(len(lines))
    print(lines)
#Open the file lsinsulin_seq_clean.txt to write the 1-24 amino acid preproinsulin_seq_clean.txt and and write the 
with open('preproinsulin_seq_clean.txt', 'w') as f:
    f.writelines(lines)

#Save amino acids 1-24    
    amino1_24=lines[0:24]
#Verify that your file has 24 characters  
    print(len(amino1_24))
    #print(amino1_24)
#Open the file lsinsulin_seq_clean.txt to write the 1-24 amino acid   
with open('lsinsulin_seq_clean.txt', 'w') as f:
    f.writelines(amino1_24)
    
#Save amino acids 25-54    
    amino25_54=lines[24:54]
#Verify that your file has 30 characters
    print(len(amino25_54))
    #print(amino25_54)
with open('binsulin_seq_clean.txt', 'w') as f:
    f.writelines(amino25_54)   
#Save amino acids 55-89    
    amino55_89=lines[54:89]
#Verify that your file has 35 characters
    print(len(amino55_89))
    #print(amino55_89)
with open('cinsulin_seq_clean.txt', 'w') as f:
    f.writelines(amino55_89)    
#Save amino acids 90-110  
    amino90_110=lines[89:110]
#Verify that your file has 21 characters
    print(len(amino90_110))
    #print(amino90_110)
with open('ainsulin_seq_clean.txt', 'w') as f:
    f.writelines(amino90_110)    


print(lines)
print(len(lines))
