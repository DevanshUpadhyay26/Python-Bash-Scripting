
import random
lower_case="abcdefgijklmnopqerstuvwxyz"
upper_case="ABCDEFGIJKLMNOPQERSTUVWYZ"
num="012345666789"
sym="[]#()*;,_-"
ans=lower_case+upper_case+num
length=6
password="".join(random.sample(ans,length))
print("Password Generated is: ",password)

#THIS SCRIPT GENERATE RANDOM PASSWORD OF SPECIFIC LENGTH USING RANDOM MODULE AND USES JOIN METHOD FOR MERGING THE COMBINATION OF STRINGS
