# Write a python program to check whether or not the user-provided keys are available in the dictionary( use in operator)
dic={"name":"sandeep","age":15,"place":"NTA"}
i=input()
count=0
for j in dic:
  if i==j:
    print("found! value is ",dic[i]);
    count=1
if count==0:
  print("not found")
    