import sys
from myhtmlgen import *

if len(sys.argv)< 2:
        print "Indicare il file sorgente per il form"
        sys.exit(1)

html = []

n = {'1': 'one',
     '2': 'two',
     '3': 'three',
     '4': 'four',
     '5': 'five',
     '6': 'six',
     '7': 'seven',
     '8': 'eight',
     '9': 'nine',
     '10': 'ten',
     '11': 'eleven',
     '12': 'twelve'
}


with open(sys.argv[1], 'r') as f:
        for row in f.readlines():

                token = row.lstrip().rstrip().split()
                if token:       # check for empty lines
                        if token[0] == '!':     # ! indicates a new row
                                new_row = DIV(Class='row')
                                for i in xrange(1, len(token), 2):
                                        new_row <= DIV(token[i], Class='{} twelfths'.format(n[token[i+1]]))
                                html.append(new_row)

                        elif token[0] == '#':    # # for comments
                                continue

                        else:
                                for i in xrange(0, len(token), 2):
                                        new_row <= DIV(token[i], Class='{} twelfths'.format(n[token[i+1]]))
                                html.append(new_row)

for h in html:
        print h, '\n'
