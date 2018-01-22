# StrCrypto
A simple implementation of the encryption and decryption of strings

Website: https://github.com/wangshiphys/StrCrypto

This project contains a `strcrypto` module as well as a test script
`strcrypto_test.py`

The `strcrypto` module provides implementation of the encryption and
decryption algorithm

The `strcrypto_test.py` script provides test as well as usage examples of
the `strcrypto` module

## Module constants
The constants defined in the `strcrypto` module are:

strcrypto.**ENCODING**

The encoding used to convert between strings and bytes

strcrypto.**BASE64_ALPHABET**

Collection of characters that is used to generate a random string as the *key_str*

strcrypto.\_\_version\_\_

strcrypto version string

## Module functions

The functions defined in the `strcrypto` module are:

strcrypto.**encrypt**(*origin_str, key_str=None, mode='n', file=None, file1=None*)

Encrypt the `origin_str` string using the given `key_str`

strcrypto.**decrypt**(*enc_str, key_str*)

Decrypt the `enc_str` string according to the given `key_str`

strcrypto.**decrypt_from_file**(*file0, file1=None*)

Decrypt the message reading from the given text file

## Install
Download this project from: https://github.com/wangshiphys/StrCrypto
```
python setup.py install
```
