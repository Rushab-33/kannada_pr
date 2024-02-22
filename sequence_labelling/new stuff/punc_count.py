txt_file_path = r'c:\users\rusha\projects\kannada_punct\sequence_labelling\new stuff\kannada_1m_clean1.txt'
import re
import pandas as pd
from tqdm import tqdm
import re
import sys
import os

csv_path = r'punct_count.csv'

lines = open(txt_file_path, encoding='utf-8').read().splitlines()

print(os.pwd)


viram_count = []
comma_count = []
qm_count = []

def find_punctuation_count(line):
    punc = re.findall('[.,?]+', line)
    viram_count.append(punc.count('.'))
    comma_count.append(punc.count(','))
    qm_count.append(punc.count('?'))

for line in tqdm(lines):
    find_punctuation_count(line)

df = pd.DataFrame({'sentence': lines, 'viram_count': viram_count, 'comma_count': comma_count, 'qm_count': qm_count})

df.to_csv(csv_path, index=False)
