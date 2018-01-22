"""
strcrypto setup file, used to install strcrypto
"""


from setuptools import setup


setup_params = dict(
    name="strcrypto",
    version="1.0",
    description="Encrypt and decrypt strings!",
    author="wangshiphys",
    author_email="wangshiphys@gmail.com",
    long_description="Encrypt and decrypt strings!",
    keywords="python, encrypt, decrypt, string",
    url="https://github.com/wangshiphys/StrCrypto",
    python_requires=">=3.6",
    scripts=[
        "strcrypto.py",
    ],
)


if __name__ == "__main__":
    setup(**setup_params)