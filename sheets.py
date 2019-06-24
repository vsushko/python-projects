from tqdm import tqdm_notebook as tqdm 

from time import sleep
from tqdm import tqdm_notebook

for i in tqdm_notebook(range(3)):
    for j in tqdm_notebook(range(5)):
        sleep(0.1)
        #print(i," : ", j)

print("Done!")
