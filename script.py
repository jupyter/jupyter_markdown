import json
import nbformat
from pprint import pprint
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook
with open('spec.json') as data_file:    
    data = json.load(data_file)
cells=[]
for i in range(len(data)):
    cells +=[new_markdown_cell(data[i]["markdown"])]
nb=new_notebook(cells=cells,metadata={'kernelspec': {
            'name': 'python2',
            'display_name': 'Python 2'
        }})


nbformat.write(nb,"/Users/ashu/github/ans.ipynb",4.0)
