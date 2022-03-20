a=[0]*30
count=0
def place(pos):

  for i in range(1,pos):
    if a[i]==a[pos] or abs(a[i]-a[pos])==abs(i-pos):
      return 0
  return 1
def print_sol(n):
  global count
  count=count+1
  print("\n\nSolution #",count,":\n")
  for i in range(1,n+1):
    for j in range(1,n+1):
      if a[i]==j:
        print("Q\t",end="")
      else:
        print("*\t",end="")
    print("\n")
def queen(n):
  k=1
  a[k]=0
  while k!=0:
    a[k]=a[k]+1
    while a[k]<=n and (not(place(k))):
      a[k]=a[k]+1
    if a[k]<=n:
      if k==n:
        print_sol(n)
      else:
        k=k+1
        a[k]=0
    else:
      k=k-1
n=int(input("Enter the number of Queens: "))
queen(n)
print("\nTotal no. of solutions=",count)
