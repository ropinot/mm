import sys
from myhtmlgen import *
from lxml import etree, html

if len(sys.argv) < 3:
        print "Indicare il file sorgente per il form come primo argomento e il file destinazione come secondo argomento"
        sys.exit(1)

n = {'1': 'one',        # convert numbers to strings
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

generated_html = []


# def add_cells(row, token, start_from):
#
#         for i in xrange(start_from, len(token), 2):
#                 cell = '{{ form.%s.label }}{{ form.%s }}{%% for e in form.%s.errors %%}<p class="red message">{{ e }}</p>{%% endfor %%}' % (token[i], token[i], token[i])
#                 row <= DIV(cell, Class='{} twelfths'.format(n[token[i+1]]))
#         return row
#

with open(sys.argv[1], 'r') as f:
        for row in f.readlines():

                token = row.lstrip().rstrip().split()

                if token:       # check for empty lines
                        if token[0] == '!':  # ! indicates a new row

                                new_row = DIV(Class='row')

                                for i in xrange(1, len(token), 2):
                                        if token[i] == "$":    # empty cells
                                                cell = ' '
                                        else:           # field cells
                                                cell = '{{ form.%s.label }}{{ form.%s }}{%% for e in form.%s.errors %%}<p class="red message">{{ e }}</p>{%% endfor %%}' % (token[i], token[i], token[i])
                                        new_row <= DIV(cell, Class='{} twelfths'.format(n[token[i+1]]))

                                generated_html.append(new_row)

                        elif token[0] == '#':    # # for comments
                                continue
                        else:
                                print "Carattere non riconosciuto"
                                sys.exit(1)

content = ''

for h in generated_html:
        content += h.__str__()

with open(sys.argv[2], 'w') as f:
        content = html.fromstring(content)
        f.write(etree.tostring(content, encoding='unicode', pretty_print=True))


# f = open('form.html', 'w')
# for h in generated_html:
#         f.write(h.__str__())
#
# with open('form.html', 'r') as f:
#         content = f.read()
#         content = html.fromstring(content)
#         print(etree.tostring(content, encoding='unicode', pretty_print=True))




