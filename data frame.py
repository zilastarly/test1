import pandas as pd
import numpy as np
d=pd.date_range('20200301',periods=10)
#rint(d)
df=pd.DataFrame(np.random.randn(10,4),index=d,columns=['A','B','C','D'])
print(df)