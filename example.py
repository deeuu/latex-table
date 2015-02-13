#! /usr/bin/python

from latex_table import LatexTable

myTable = LatexTable('c|c', num_sig_figs=2)
myTable.add_hline()
myTable.add_row('Header1', 'Header2')
myTable.add_row(0.00000552, 2.562)
myTable.add_row(1.055, 2.562)
myTable.add_row(4.0034, 10.201)
myTable.to_latex()
myTable.write_table('myTable.tex')
