# math292-textbook
Rutgers Math 292 (Differential Equations) Textbook using PreTeXt.

To run, use the command (in a terminal or shell)

`xsltproc -xinclude path\to\mathbook\xsl\pretext-html.xsl .\math292-txtbk.xml`

The file `math292-txtbook.html` leads to the chapter list of the PreTeXt file.

The Python file only works if your terminal is in this directory. Once it is, the command

`python moveout.py`

will move all HTML files in this folder that are generated and move them to the folder named `output`.
