# -*- coding: utf-8 -*-

from StringIO import StringIO

escape_mapping = {
    '&': '\\&',
    '%': '\\%',
    '$': '\\$',
    '#': '\\#',
    '_': '\\_',
    '{': '\\{',
    '}': '\\}',
    '~': '\\textasciitilde',
    '^': '\\textasciicircum',
    '\\': '\\textbackslash'
}

def escape(input_string):
    if input_string:
        input_string = unicode(input_string)
        for value, escaped in escape_mapping.items():
            input_string.replace(value, escaped)
        return input_string
    else:
        return None

def round_sig_figs(value, num_sig_figs):
    try:
        value = float(value)
    except:
        return value
    form = '%0.' + str(num_sig_figs) + 'g'
    return form % value
    
class LatexTable(object):

    row_strings = []

    def __init__(self, table_spec, position=None, centering=False,
                 caption=None, label=None, auto_hline=True, num_sig_figs=2):
        self.table = None
        self.table_spec = table_spec
        self.position = position
        self.centering = centering
        self.caption = escape(caption)
        self.label = escape(label)
        self.num_sig_figs = num_sig_figs
        self.auto_hline = auto_hline

    def add_row(self, *args):
        columns = []
        for column in args:
            #Try rounding if not string
            column = round_sig_figs(column, self.num_sig_figs)
            columns.append(escape(unicode(column)))
        self.row_strings.append(u" & ".join(columns) + " \\\\")
        if self.auto_hline:
            self.add_hline()

    def add_hline(self):
        self.row_strings.append(u"\\hline")

    def to_latex(self):
        self.table = u""
        self.table += u"\\begin{table}"
        if self.position:
            self.table += u'[' + self.position + ']'
        self.table += u"\n"

        if self.centering:
            self.table += u"  \\centering\n"

        self.table += u'  \\begin{tabular}{' + self.table_spec + '}\n'

        for row in self.row_strings:
            self.table += "    " + row + u" \n"
        self.table += u'  \\end{tabular}\n'

        if self.caption:
            self.table += u'  \caption{' + self.caption + '}\n'

        if self.label:
            self.table += u'  \label{' + self.label + '}\n'

        self.table += u'\\end{table}\n'

    def write_table(self, file_name = ''):
        if file_name and self.table:
            f = open(file_name, 'w')
            f.write(self.table)
            f.close()
