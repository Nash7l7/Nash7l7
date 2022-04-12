n = int(input ("Enter: " ))
for i in range (1,n+1):
 for j in range (1,i+1):
  if (i==0 or j==i or j==n-1):
   print ('*',end=' ')
  else:
   print (' ',end=' ')
 print ()

for i in range (0,n):
 for j in range (0,n):
  if (i==0 or j==n-1 or i==j):
   print ('*',end=' ')
  else:
   print (' ',end=' ')
 print ()
