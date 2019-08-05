from werkzeug.security import generate_password_hash,check_password_hash

hash_pass = generate_password_hash('mypassword')

print(hash_pass)

check = check_password_hash(hash_pass,'mypassword')

print(check)