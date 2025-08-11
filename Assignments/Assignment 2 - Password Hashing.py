import bcrypt

def secure_password(password):
  password = password.encode('utf-8')
  hashed = bcrypt.hashpw(password, bcrypt.gensalt())
  return hashed.decode('utf-8')

if "__main__" == __name__:
  password = secure_password(input())
  print(password)