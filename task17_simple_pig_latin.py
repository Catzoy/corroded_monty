# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

import re
import string
def pig_it(text):
    list = re.findall(r"[\w']+|[.,!?;]",text)
    a = []
    for i in list:
        if i in string.punctuation:
            a.append(i)
            continue
        a.append(i[1:] + i[0] + "ay")
        str = " "
    return str.join(a)
