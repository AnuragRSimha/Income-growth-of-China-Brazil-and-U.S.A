#Use income_growth.csv to do the following instructions
#a. Load it into a data frame called growth.
#b. Use the appropriate function to calculate the global mean of ‘China’, ‘Brazil’, ‘USA’.
#c. Use the appropriate function to calculate the global median of ‘China’, ‘Brazil’, ‘USA’.
#d. Use the appropriate function to calculate the standard deviation of ‘China’, ‘Brazil’, ‘USA’.

import csv
import pandas as pd
import statistics as s
a=[]
china=[]
brazil=[]
usa=[]
f=open("income_growth.csv",'r')
f1=csv.reader(f)
#a)
growth=pd.DataFrame(f1)
print("Use income_growth.csv to do the following instructions\n"+"a. Load it into a data frame called growth.\n")
print(growth)
#--------------
growth=growth[1:]
for i in range(1,4):
    a.append(str(growth[[i]]).split())
china.extend(a[0])
china=china[2::2]
china=[float(i) for i in china]
brazil.extend(a[1])
brazil=brazil[2::2]
brazil=[float(i) for i in brazil]
usa.extend(a[2])
usa=usa[2::2]
usa=[float(i) for i in usa]
print("--------------------------------------------------------")
#b)
print("b. Use the appropriate function to calculate the global mean of ‘China’, ‘Brazil’, ‘USA’.\n")
print("Global mean of China is :",s.mean(china))
print("Global mean of Brazil is :",s.mean(brazil))
print("Global mean of U.S.A is :",s.mean(usa))
print()
#c)
print("c. Use the appropriate function to calculate the global median of ‘China’, ‘Brazil’, ‘USA’.\n")
print("Global median of China is :",s.median(china))
print("Global median of Brazil is :",s.median(brazil))
print("Global median of U.S.A is :",s.median(usa))
print()
#d)
print("d. Use the appropriate function to calculate the standard deviation of ‘China’, ‘Brazil’, ‘USA’.\n")
print("Standard deviation of China is :",s.stdev(china))
print("Standard deviation of Brazil is :",s.stdev(brazil))
print("Standard deviation of U.S.A is :",s.stdev(usa))
print()
