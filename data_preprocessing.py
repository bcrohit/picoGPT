"""
A simple script to clean unformatted names of females and males.
"""

import os
import re
import pandas as pd

male_names = pd.read_csv('data\\Indian-Male-Names.csv')
female_names = pd.read_csv('data\\Indian-Female-Names.csv')

namelist = []

pattern = "\s.*"
namelist = [re.sub(pattern, "", str(name)) for name in female_names['name']]
m_namelist = [re.sub(pattern, "", str(name)) for name in male_names['name']]
namelist.extend(m_namelist)


processed_namelist = []

s = 'abcdefghijklmnopqrstuvwxyz'

for i in namelist:
    i = i.split('@')[0]
    i = i.split('.')[-1]
    i = i.split('-')[-1]
    i = i.strip('`').strip()

    if len(i) > 2:
        for j in i:
            if j in s:
                processed_namelist.append(i)
 

# unique names 
unique_names = set(processed_namelist)

# sort names
processed_namelist = sorted(list(unique_names))
processed_names = "\n".join(processed_namelist)

pattern = r'[^a-z\n]'
processed_names = re.sub('0', 'o', processed_names)
processed_names = re.sub(pattern, '', processed_names)

with open(os.path.join("data", "names.txt"), "w") as fp:
    fp.write(processed_names)