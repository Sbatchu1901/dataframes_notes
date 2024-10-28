import pandas as pd #alias
import functions
adict = {'column1': [1, 2, 3], 'column2': [4, 5, 6],'column3':[7,8,9]}
df2 = pd.DataFrame(adict)
functions.print_it('original dictionary', adict)
functions.print_it('Created from a dictionary', df2)
# create another dataframe from a dictionary and print it <<< TO DO
dictionary2={'productnames':['apple','banana','cherry'],
             'price':[2.99,3.99,4.99]}
df3 = pd.DataFrame(dictionary2)
functions.print_it('mypandaslist', df3)