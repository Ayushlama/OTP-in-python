import random
import string
def random_pass(size):
    generate_pass = ''.join([random.choice( string.ascii_uppercase + string.ascii_lowercase + string.digits) for n in range (size)])
    return generate_pass

password = random_pass(10)
print(password)