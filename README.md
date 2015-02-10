PySLOC
---

PySLOC is a basic source lines of code counter, written for python3.
To install, first install the dependencies with:

```
pip install tabulate
```

Then download the file and move it to an appropriate directory.Note
that it won't count itself among the source of any project it's added to.
To use it, simply follow the usage guidelines:

```
usage: pysloc.py [-h] --dir DIR --exts EXTS

Count the source lines of code in a given project

optional arguments:
  -h, --help   show this help message and exit
  --dir DIR    The top level directory for your project
  --exts EXTS  A comma-separated list of file extensions to use.
```

Note that the dir and exts arguments are required. A sample usage for
a Flask or Django project might be:

```
python3 pysloc.py --dir ../ --exts html,py,css
```
