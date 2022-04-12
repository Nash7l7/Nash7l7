n=5
for i in range (n):
 for j in range (n):
  if (j==0 or j==n-1):
   print ('*',end=' ')
  else:
   print (' ',end=' ')
 print ()

for i in range (n):
 for j in range (n):
  if (j==n//2 or i==n//2):
   print ('*',end=' ')
  else:
   print (' ',end=' ')
 print ()

for i in range (n):
 for j in range (n):
  if (i==j or i+j==n-1):
   print ('*',end=' ')
  else:
   print (' ',end=' ')
 print ()

for i in range (n):
 for j in range (i,n):
  if (i==0 or j==n-1 or j==i):
   print ('*',end=' ')
  else:
   print (' ',end=' ')
 print ()

