# py2exe

py2exe is a Python Distutils extension which converts Python scripts into executable Windows programs, able to run without requiring a Python installation.Spice

## Installation

```
# py2exe
conda install -c https://conda.anaconda.org/clinicalgraphics cg-py2exe
```

## Build [^1]

```
python setup.py py2exe
# build PyQT
python setup.py py2exe --includes sip
```

## Known Issues

**Error: Microsoft Visual C++ 10.0 is required (Unable to find vcvarsall.bat) ([link](https://stackoverflow.com/questions/28251314/error-microsoft-visual-c-10-0-is-required-unable-to-find-vcvarsall-bat))**

How to fix

Step 1: Install Visual Studio 2015

Step 2:

```python
set VS100COMNTOOLS=%VS140COMNTOOLS%
```


[^1]: [http://www.py2exe.org/index.cgi/Py2exeAndPyQt](http://www.py2exe.org/index.cgi/Py2exeAndPyQt)