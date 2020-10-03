# `Directory Organizer` Package

[![Setup Automated](https://img.shields.io/badge/setup-automated-blue?logo=gitpod)](https://gitpod.io/from-referrer/)
![Test passing](https://img.shields.io/badge/Tests-passing-brightgreen.svg)
![Python Version](https://img.shields.io/badge/python-3.x-brightgreen.svg)
[![PyPI version](https://badge.fury.io/py/directory-organizer.svg)](https://badge.fury.io/py/directory_organizer)
![](https://img.shields.io/github/last-commit/rahulbordoloi/Directory-Organizer?style=flat-square)
[![Open Source Love png2](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

Have a cluttered Folder/Directory? No Worries!

`Directory Organizer` is a simple Python Package that scans your folder directory and moves the specific file types to its type-specific directories.

<b> Currently Available for All Platform.  </b>

## Class Documentation

```python
class directory_organizer.organizer(path = 'Downloads', verbose = False)
```
By default, `path = 'Downloads'` of the Base OS and `verbosity = False` ie no output to the console regarding files moved. <br>

| __Parameters__ | __Description__ |
|      ---       |      ---        |
|     __path__   | Absolute path to the directory when we want to perform our operation. |
|    __verbose__ | Controls the verbosity ie console output during our operations. | 

__Methods__

```python
showHistory(extension_type = None)
```
Returns a Dictionary of the Files that were been Moved.
By default, showHistory() returns dictionary of the all the file types if no argument has been passed. <br>

| __Parameters__ | __Description__ |
|    ---         |       ---       |
| __extension_type__ | Can be anything among these - ['Documents', 'Pictures', 'Musics', 'Videos', 'Others'] |

if __extension_type__ is passed as an argument, then a dictionary containing moved files will be returned having `extension_type` as type.

Sample Output of `showHistory()` :

![Sample JSON](./Test/Snapshots/JSON.png)

## About

Categorise your files into Pictures, Documents, Music, Videos! (Support for more categories will be added if Required).

Pictures will be moved to `/home/$user/Pictures` for Unix-based systems or `c:\user\username\Pictures` for Windows, same goes for Documents, Music, Videos etc to their respective folders.


All the classes/methods will be imported under the package `directory_organizer`.

Further File Types will be added to Existing Types to Widen Support.

<b>Note : </b>
*   By Default, Directory Organizer considers base `Downloads` Directory of your OS.
*   If the File-type doesn't match with either of Pictures/Documents/Videos/Music File extensions, then it'll be moved to `Others` Directory.

This Package has been developed collectively by [@rahulbordoloi](https://github.com/rahulbordoloi) and [@SouravMzdr](https://github.com/SouravMzdr) which has been published to [PyPI](https://pypi.org/project/directory-organizer/).

## Installation

Run the following command on your terminal to install `directory_organizer`: 

1 .  Installing the Package using `pip`:
```python
pip install directory_organizer
```
OR

```python
pip3 install directory_organizer
```

2 . Cloning the Repository:

```
git clone https://github.com/rahulbordoloi/Directory-Organizer/
cd directory_organizer
pip install -e .
```

## Usage

Run this Script in order to move all the Files to their respective type folders! [Default]

![Main](./Test/Snapshots/directory_organizerMain.png)

<!--
```python
# Importing Libraries
from directory_organizer import organizer

# Main Method
if __name__ == '__main__':
    organizer()
```
-->

## Outputs

1 . Selecting Directory and Output as `DEFAULT`

```python
>>> from directory_organizer import organizer
>>> organizer()
Moving Document File Extensions ...
Moving Picture File Extensions ...
Moving Music File Extensions ...
No Videos to Move!
Moving Other File Extensions ...
Time Elapsed :  0.2 seconds
```

2 . Selecting a `Random` Directory with Output `True`.

```python
>>> from directory_organizer import organizer
>>> object = organizer('C:\Personal\Work\Directory Organizer\Test\Random', True)
Moving Document File Extensions ...
7 Files moved to Documents!
5_6084888091904966894.pdf
5_6293939556248977731.pdf
Artemis.pdf
AWS Bucket.csv
certificate.pdf
datasets_1111_2005_kidney_disease.csv
sparsehc-a-memory-efficient-online-hierarchical-clustering-algorithm.pdf
No Pictures to Move!
Moving Music File Extensions ...
1 Files moved to Musics!
In the end - Linkin Park (with).mp3
Moving Video File Extensions ...
1 Files moved to Videos!
Narcos - Main Trailer - Netflix [HD].mp4
Moving Other File Extensions ...
2 Files moved to Others!
ngrok.exe
saved_model.pb
Time Elapsed :  0.13 seconds
```

## Screenshots of Result

Before `Organizing` :

![Before Downloads](./Test/Snapshots/Before_Downloads_Main.PNG) 

After `Organizing` :

![After Downloads](./Test/Snapshots/After_Downloads_Main.PNG) 

## Developing `Directory Organizer`

To install `directory_organizer`, along with the tools you need to develop and run tests, and execute the following in your virtualenv:

```bash
$ pip install -e .[dev]
```

## Security & Bugs

*   As a security measure, this script *WILL NOT* access files located in any subdirectory unless explicitly stated.
*   Files having the same name as in Source and Target will get __Replaced__. [Caution]

## Contact Author(s)

Name : __Rahul Bordoloi__ <br>
Website : https://rahulbordoloi.me <br>
Email : rahulbordoloi24@gmail.com <br>

Name : __Sourav Mazumdar__ <br>
Email : souravmzdr@gmail.com <br>

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/rahulbordoloi/)
