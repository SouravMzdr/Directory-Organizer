# `Directory Organiser` Package

[![Setup Automated](https://img.shields.io/badge/setup-automated-blue?logo=gitpod)](https://gitpod.io/from-referrer/)
![Python Version](https://img.shields.io/badge/python-3.x-brightgreen.svg)
[![Open Source Love png2](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

## About

Have a cluttered Folder/Directory? No Worries!

`Directory Organiser` is a Simple Python Package that scans the Folder Directory and moves the specific file types to its type specific directories.

<b> Currently Available for Debian and Windows based Systems. </b>

Categorise your Files into Pictures Documents and Music Videos! (Support for more categories will be added if Required).

Pictures will be moved to `/home/$user/Pictures` for Debian-based systems or `c:\user\username\Pictures` for Windows, Similarly Documents, Music, Videos etc to their respective folders.

This Package is developed collectively by [@rahulbordoloi](https://github.com/rahulbordoloi) and [@SouravMzdr](https://github.com/SouravMzdr) which has been published to [PyPI]().

All the classes/methods will be imported under the package `directory_organiser`.

Further File Types will be added to existing files to widen support.

<b>Note : </b>By default, Directory Organiser considers base `Downloads` Directory.

## Installation

Run the following command on your terminal to install : 

```python
pip install directory_organiser
```
OR

```python
pip3 install directory_organiser
```

## Usage

Run this script in order to move all the Pictures, Documents, Music, Videos etc to their respective folders!

```python
python main.py
```

## Outputs

[OOPS Implementation Output]
```
C:\Personal\Work\Rony\Scripts\python.exe "C:/Personal/Work/Move Files/main.py"

Where do you want to Organise your Files?
1. Downloads
2. Any Other Location
Enter the Full Path to your Directory [Just Type 'Downloads' for Case 2] ->
C:\Personal\Work\Move Files\Test\Downloads
Do you want to Display the File Names? (YES/NO) : no
Moving Documents ...
62 Files moved to Documents!
Moving Pictures ...
6 Files moved to Pictures!
Moving Music Files ...
1 Files moved to Music!
Moving Video Files ...
1 Files moved to Videos!
Moving Other File Extensions ...
13 Files moved to Others!
Time Elapsed :  8.19 seconds
```

## Developing `Directory Organiser`

To install `directory_organiser`, along with the tools you need to develop and run tests, run the following in your virtualenv:

```bash
$ pip install -e .[dev]
```

## Security & Bugs

As a security measure this script *WILL NOT* access files located in any subdirectory unless explicitly stated.
<!--
__Known bugs__ : <br>
Ignores files if extension is not in lowercase standard encoding.
-->
## Contact Author(s)

Name : Rahul Bordoloi <br>
Website : https://rahulbordoloi.me <br>
Email : rahulbordoloi24@gmail.com <br>

Name : Sourav Mazumdar <br>
Email : souravmzdr@gmail.com <br>

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/rahulbordoloi/)

