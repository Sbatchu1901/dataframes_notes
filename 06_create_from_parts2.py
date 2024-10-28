import pandas as pd #alias
import functions
grades_dict = {'Wally': [87, 96, 70],
               'Eva': [100, 87, 90],
               'Sam': [94, 77, 90],
               'Katie': [100, 81, 82],
               'Bob': [83, 65, 85]}
grades_df = pd.DataFrame(grades_dict)
grades_df.index = ['test1', 'test2', 'test3']
functions.print_it('Dictionary entries', grades_df)
# create a dataframe with 3-digit student numbers as index, 
# and data that stores three quiz grades  <<< TO DO
grades2_dict = {'name':['sak','vam','har'],
                'quiz1':[90,87,51],
                'quiz2':[89,98,78],
                'quiz3':[98,98,98]}
grades1_df = pd.DataFrame(grades2_dict)
grades1_df.index = [111,222,333]
functions.print_it('Dictionary entries', grades1_df)