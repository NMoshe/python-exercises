#mcb.pyw - save and load text to clipboard
#py.exe mcb.pyw save <keyword> - saves clipboard to keyword
#py.exe mcb.pyw <keyword> - loads keyword to clipboard
#py.exe mcb.pyw list <keyword> - Loads all keywords to clipboard

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')
#Save clipboard text
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    #list keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()