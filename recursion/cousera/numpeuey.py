import math
import re

import numpy as np

d = np.zeros([2, 3])
b = np.arange(1, 16, 1).reshape(3, 5)
# print(b)
wiki = "Mia[edit] fir jsj is hghg pala[edit]"
print(re.findall("[a-zA-Z]{1,100}\[edit\]", wiki))
for title in re.findall("[\w]*\[edit\]", wiki):
    print(re.findall("[\w]*\[edit\]", title))

pattern = """
(?P<title>.*)      #the university title
(-\ located\ in\ ) #an indicator of the location
(?P<city>\w*)      #city the university is in
(,\ )              #separator for the state
(?P<state>\w*)     #the state the city is located in"""

for item in re.finditer(pattern, wiki, re.VERBOSE):
    print(item.groupdict())
