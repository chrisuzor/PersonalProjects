import pandas as pd
import numpy as np

students_classes = {
    'Alice':'Physics',
    'Jack': 'Chemistry',
    'Molly': 'English',
    'Sam': 'History'
}

s = pd.Series(students_classes)
#print(s.iloc[3])
#print(s.loc['Molly'])

numbers = pd.Series(np.random.randint(0,1000,10000))
