# @G4rip - < https://t.me/G4rip >
# Copyright (C) 2022
# Tüm hakları saklıdır.
#
# Bu dosya, < https://github.com/aylak-github/PyFileLock > parçasıdır.
# Lütfen GNU Affero Genel Kamu Lisansını okuyun;
# < https://www.github.com/aylak-github/PyFileLock/blob/master/LICENSE/ >
# ================================================================

from setuptools import setup

classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
]

long_description = """
# **🔐 PyFileLock**
### **🔑 Dosya şifreleyici**
- Python dosyalarını 15 farklı kombinasyonda şifreleyebilir.
<br>

## **🪀 PyPi Kütüphanesi:**
<br>

![PyPI](https://img.shields.io/pypi/v/PyFileLock?color=yellow&logo=python&logoColor=cyan&style=for-the-badge)
<br>

![PyPI - Downloads](https://img.shields.io/pypi/dm/PyFileLock?label=%C4%B0nd%C4%B0rme&logo=python&style=for-the-badge)
<br>

[![Python](https://img.shields.io/badge/Python-ile%20yap%C4%B1ld%C4%B1-yellow?style=for-the-badge&logo=python&logoColor=cyan)](https://python.org)
<br>

<br><a href="https://t.me/G4rip"><img src="https://github.com/aylak-github/PyFileLock/blob/master/ss.png?raw=true" width="350"></a><br>

### **💻 Kurulum:**

#### **Termux**

```sh
bash <(curl -L https://bit.ly/PyFLock)
```

#### **Terminal**

```sh
pip install PyFileLock
python3 -m PyFileLock
```

<br>

📅 ***2022 (c) [GNU Affero General Public License v3.0](https://github.com/aylak-github/PyFileLock/blob/master/LICENSE) ile korunmaktadır.***

<br>

### **📡 İletişim :**
[![Github](https://img.shields.io/badge/Github-525252?style=for-the-badge&logo=github)](https://github.com/aylak-github) [![Opensource](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/G4rip)
"""


setup(
    name="PyFileLock",
    version="1.0.0",
    author="aylak-github",
    description="Python dosyalarını 15 farklı kombinasyonda şifreler.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aylak-github/PyFileLock",
    license="GNU AFFERO GENERAL PUBLIC LICENSE (v3)",
    packages=["PyFileLock"],
    install_requires="rich",
    classifiers=classifiers,
    python_requires=">3",
)