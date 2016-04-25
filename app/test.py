from werkzeug.security import generate_password_hash, check_password_hash

print generate_password_hash("123123")
print check_password_hash("pbkdf2:sha1:1000$vzw9C3DN$1102b3a86fb1084bd976c6460f1abe34915157df", "123123")