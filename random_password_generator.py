import random
import string
def gen_password(length=12,use_upper=True,use_lower=True,use_digits=True,use_special=True):
    if length<4:
        return 'length must should be atleast 4 characters.'
    set_char=''
    if use_upper:
        set_char=string.ascii_uppercase
    if use_lower:
        set_char+=string.ascii_lowercase
    if use_digits:
        set_char+=string.digits
    if use_special:
        set_char+=string.punctuation
    if not set_char:
        return "Error atleast one character type must be selected" 
    password=' '.join(random.choice(set_char) for i in range(length))
    return password
print(gen_password(12))