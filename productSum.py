#product sum 
def productsum(arr,depth = 1):
  sum = 0
  for i in arr:
    if isinstance(i,list): # check whether i is list or not
      sum += productsum(i,depth + 1) * depth
    else:
      sum += i * depth
  return sum 


a = [5,2,[7,-1],3,[6,[-13,8],4]]
print("sum is :",productsum(a,1))
    
  
    