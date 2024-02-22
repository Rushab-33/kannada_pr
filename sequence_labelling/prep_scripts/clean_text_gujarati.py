# import re
# import sys
# from tqdm import tqdm

# def filter_line(line):
#     '''
#     replace foreign characters not punctuation and numerals with space
#     '''
    
#     if re.search(punc,line):     
#         clean_line = ' '.join(re.sub(pattern, ' ', line).split())
#         if clean_line and (clean_line[0] in ['.', ',', '?']):
#             clean_line = clean_line[1:]
#         temp_line = clean_line.replace(" ","")
#         if regex.search(temp_line):
#             return ''
#         return ' '.join(clean_line.split())
#     return ''
# file_path = r'C:\Users\rusha\projects\kannada_punct\kannada_1m_clean.txt'
# if __name__ == '__main__':
#     fpath = file_path
#     dest = 'cleaned_kananda.txt'
#     with open(file_path, mode = 'r', encoding='mac_roman') as file:
#         dictionary = file.readlines()
#     char = [i.split(' ')[0] for i in dictionary] 
#     pattern = '[^ '+''.join(char)+'.,?]'
#     punc = '[.,?]+'
#     regex = re.compile(r'[.?,]{2,}')
#     #line_list = open(fpath).read().splitlines()
#     line_list = open(fpath, encoding='mac_roman').read().splitlines()

# #    
# ## pattern = '[^ ઁ-ઃઅ-ઋઍએ-ઑઓ-નપ-રલ-ળવ-હા-ૅે-ૉો-્.,?]+'
    
#     cleaned_line_list = [filter_line(line) for line in tqdm(line_list)]
#     cleaned_line_list = [i for i in cleaned_line_list if i != '']  

#     with open(dest, 'w') as f:
#         f.write('\n'.join(cleaned_line_list))
#     print("\tcompleted")

import re
import sys
from tqdm import tqdm

def filter_line(line):
    '''
    replace foreign characters not punctuation and numerals with space
    '''
    
    if re.search(punc, line):     
        clean_line = ' '.join(re.sub(pattern, ' ', line).split())
        if clean_line and (clean_line[0] in ['.', ',', '?']):
            clean_line = clean_line[1:]
        temp_line = clean_line.replace(" ","")
        if regex.search(temp_line):
            return ''
        return ' '.join(clean_line.split())
    return ''

file_path = r'C:\Users\rusha\projects\kannada_punct\kannada_1m_clean.txt'
if __name__ == '__main__':
    fpath = file_path
    dest = 'cleaned_kananda.txt'
    with open(file_path, mode = 'r', encoding='mac_roman') as file:
        dictionary = file.readlines()
    char = [i.split(' ')[0] for i in dictionary] 
    pattern = '[^ '+''.join(char)+'.,?]'
    punc = '[.,?]+'
    regex = re.compile(r'[.?,]{2,}')
    #line_list = open(fpath).read().splitlines()
    line_list = open(fpath, encoding='mac_roman').read().splitlines()

    for line_number, line in enumerate(line_list, start=1):
        try:
            # Process the line
            cleaned_line = filter_line(line)
        except UnicodeDecodeError as e:
            print(f"Decoding error at line {line_number}: {e}")
            print("Problematic line:")
            print(line)  # Print the problematic line
            print("Problematic bytes:")
            # Iterate over characters and print their byte values
            for char in line:
                try:
                    char.encode('utf-8')
                except UnicodeEncodeError:
                    print(f"Problematic byte: {char.encode('utf-8')}")
            continue  # Continue to the next line after printing problematic bytes

    print("\tcompleted")

# Print the current working directory
import os
print("Current Working Directory:", os.getcwd())
