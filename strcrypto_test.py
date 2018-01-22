from strcrypto import *

origin_str = "www.google.com"
key_str = "github.com"
log0 = "The original string: {}".format(origin_str)
log1 = "The key string: {}".format(key_str)
separator = '=' * max(len(log0), len(log1)) + '\n'
print(log0)
print(log1)
print(separator)

enc_str, key_str = encrypt(origin_str, key_str)
dec_str = decrypt(enc_str, key_str)
print("The encrypted string: {}".format(enc_str))
print("The key: {}".format(key_str))
print("The decrypted string: {}".format(dec_str))
assert dec_str == origin_str
print(separator)

encrypt(origin_str, mode='one')
buff = decrypt_from_file("string_and_key.txt")
assert buff == origin_str
print(separator)

encrypt(origin_str, mode='s')
buff = decrypt_from_file("string.txt", "key.txt")
assert buff == origin_str
