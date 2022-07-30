import re
st=input("enter the string: ")
x=re.findall('ab{3}',st)
if x:
  print("Matched")
else:
  print("No Match")