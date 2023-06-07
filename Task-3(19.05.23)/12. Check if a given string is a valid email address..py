import re
def is_valid_email(email):
    pattern =r'^[a-z]+@[a-z]+\.\w+$'
    return re.match(pattern, email)is not None
email_address = 'example@example.com'
if is_valid_email(email_address):
    print(email_address, 'is a valid email address.')
else:
    print(email_address, 'is not a valid email address.')