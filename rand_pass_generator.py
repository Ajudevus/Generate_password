import numpy as np
def create_password():
    pass_length=np.random.randint(10,13)
    password=""
    for i in range(pass_length):
        password=password+chr(np.random.randint(33,123))
    return password
pass_w=create_password()

print(pass_w)
