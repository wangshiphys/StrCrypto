"""
Functions to encrypt and decrypt strings
"""


__all__ = [
    "ENCODING",
    "BASE64_ALPHABET",
    "encrypt",
    "decrypt",
    "decrypt_from_file",
]


# The version of this module
__version__ = "1.0"


import base64
import random


# The ceiling of a byte
# Byte should be in the range [0, 255], no larger than 255
_BYTE_CEIL = 256


# The encoding used to convert between strings and bytes
ENCODING = "utf-8"


# URL- and filesystem-safe base64 alphabet which substitutes '-' instead of '+'
# and '_' instead of '/' in the standard base64 alphabet.
_ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
_ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
_DIGITS = "0123456789"
BASE64_ALPHABET = _ASCII_LOWERCASE + _ASCII_UPPERCASE + _DIGITS + "-_"


def _save_to_file(enc_str, key_str, mode, file=None, file1=None):
    if mode.lower() in ('o', "one"):
        file = file or "string_and_key.txt"
        with open(file, 'w', encoding=ENCODING) as fp:
            fp.write("string : " + enc_str + '\n')
            fp.write("key : " + key_str + '\n')
        print(
            "The key and encrypted string has been saved to `{}`.".format(file)
        )
    elif mode.lower() in ('s', "separate"):
        file = file or "string.txt"
        file1 = file1 or "key.txt"
        with open(file, 'w', encoding=ENCODING) as fp:
            fp.write("string : " + enc_str + '\n')
        print("The encrypted string has been saved to `{}`.".format(file))
        with open(file1, 'w', encoding=ENCODING) as fp:
            fp.write("key : " + key_str + '\n')
        print("The key has been saved to `{}`.".format(file1))
    else:
        print("You have chosen not to save the key and encrypted string.")


def encrypt(origin_str, key_str=None, mode='n', file=None, file1=None):
    """
    Encrypt the `origin_str` string using the given `key_str`

    Parameters
    ----------
    origin_str : str
        A string that is to be encrypted
    key_str : str, optional
        A string which is used to encrypt the `origin_str`
        If not given or None, a random string with the same length as
        `origin_str` is generated using the BASE64_ALPHABET.
        default : None
    mode : str, optional
        Specify whether to save the key and encrypted string to text file
        default : 'n'
        ===============      ===================================================
        Character            Meaning
        ---------------      ---------------------------------------------------
        'o', "One"           Save the key and encrypted string to s single file
        's', "Separate"      Save the key and encrypted string to separate file
        'n', "No"            Do not save the key and encrypted string
        ===============      ===================================================
    file, file1 : str, optional
        Path-like object giving the pathname(absolute or relative to the
        current working directory) of the file where the result is stored.

        If `mode` is 'o' or 'one', both the encrypted string and key string
        are saved to this file, and `file1` parameter is not used. The
        default value of `file` is "string_and key.txt".
        If `mode` is 's' or 'separate', the encrypted string is saved to
        `file` and key string is saved to `file1`. `file` defaults to
        "string.txt" and `file1` defaults to "key.txt".
        If `mode` if 'n' or 'No', both `file` and `file1` parameter has no
        effect.


    Returns
    -------
    enc_str : str
        The encrypted version of `origin_str`
        This is the first entry of the returning tuple.
    key_str : str
        The string used to encrypt `origin_str`
        This is the second entry of the returning tuple.

    Examples
    --------
    >>> from strcrypto import encrypt
    >>> encrypt(origin_str="abcde", key_str="edcba")
    ('xsbGxsY=', 'edcba')
    """

    origin_bytes = origin_str.encode(encoding=ENCODING)
    origin_len = len(origin_bytes)

    if key_str is None:
        key_str = "".join(random.sample(BASE64_ALPHABET, origin_len))
    key_bytes = key_str.encode(encoding=ENCODING)
    key_len = len(key_bytes)

    enc_bytes = bytes(
        (origin_bytes[i] + key_bytes[i % key_len]) % _BYTE_CEIL
        for i in range(origin_len)
    )
    enc_str = base64.urlsafe_b64encode(enc_bytes).decode(encoding=ENCODING)

    _save_to_file(enc_str, key_str, mode, file, file1)
    return enc_str, key_str


def decrypt(enc_str, key_str):
    """
    Decrypt the `enc_str` string according to the given `key_str`

    Parameters
    ----------
    enc_str : str
        The string to be decrypted
    key_str : str
        The string used to decrypted the given `enc_str`

    Returns
    -------
    dec_str : str
        The decrypted version of `enc_str`
    Examples
    --------
    >>> from strcrypto import decrypt, encrypt
    >>> decrypt(*encrypt("abcde", "edcba"))
    'abcde'
    """

    key_bytes = key_str.encode(encoding=ENCODING)
    enc_bytes = base64.urlsafe_b64decode(enc_str.encode(encoding=ENCODING))
    key_len = len(key_bytes)
    enc_len = len(enc_bytes)

    dec_bytes = bytes(
        (_BYTE_CEIL + enc_bytes[i] - key_bytes[i % key_len]) % _BYTE_CEIL
        for i in range(enc_len)
    )
    dec_str = dec_bytes.decode(encoding=ENCODING)
    return dec_str


def decrypt_from_file(file0, file1=None):
    """
    Decrypt the message reading from the given text file

    If only `file0` is given, the text file should contain these lines:
        string : `encrypted string`
        key : `key string`
    The first line is  called the `string line` and the second line is called
    `key line`.
    The content of `encrypted string` is interpret as the encrypted string
    and `key string` is interpret as the key.
    If both file0 and file1 are given, the content of file1 is appended to
    file0 before searching for the `string line` and `key line`.

    Parameters
    ----------
    file0 : str
        The path to the file where the key and/or the encrypted string is stored
    file1 : str, optional
        The path to the file where the key and/or the encrypted string is stored
        default : None

    Returns
    -------
    dec_str : str
        The decrypted string
    """

    with open(file0, encoding=ENCODING) as fp:
        buff = fp.read()
    if file1 is not None:
        with open(file1, encoding=ENCODING) as fp:
            buff += fp.read()

    str_line = buff[buff.index("string : "):].splitlines()[0]
    key_line = buff[buff.index("key : "):].splitlines()[0]
    enc_str = str_line.split(": ")[1]
    key_str = key_line.split(": ")[1]
    return decrypt(enc_str, key_str)
