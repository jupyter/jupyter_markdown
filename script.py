import json
import nbformat
import nbconvert
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook, new_output
from nbconvert.preprocessors import ExecutePreprocessor
kernel_name = 'python3' # set it programmatically so that you only need to change it in one place
display_name = 'Python 3'
output_path = '../'
timeout_amount = 60 # none of these should take too long
metadata = {'kernelspec': {
    'name': kernel_name
    }}
format_version = 4.0
with open('../spec.json') as data_file:    
    data = json.load(data_file) # json file stored in data
r = int(len(data)/100)+1  # r is the Number of notebooks to be made, each of 100 entries.
for k in range(1,r+1):
    cells=[]
    start=100*(k-1)
    end=100*k
    if k==r: # for last notebook, it might have less than 100 entries, eg. if there are 643 entries, last notebook will only have(643-600)=43 entries.
        end=len(data)
    for i in range(start,end):
        cells += [new_markdown_cell('## Example ' + str(i+1))]
        cells += [new_markdown_cell(data[i]['markdown'])]
        cells += [new_code_cell('%%html\n'+data[i]['html'])]

    nb=new_notebook(cells=cells,metadata={'kernelspec': {
            'name': kernel_name,
            'display_name': display_name
        }})
    executor = ExecutePreprocessor(timeout=60, kernel_name=kernel_name)
    executor.preprocess(nb, metadata)
    nbformat.write(nb,output_path+'nb'+str(k)+'.ipynb',format_version) # Notebook written to directory, named nb1,nb2,nb3,etc.
