def count():
     emails = {}
     d = -1
     for i in range(5):
         #print("earlier   ",d)
         d = d+1
         emails[++d] = d + 5 
         #print("later   ",d)
     print(emails)
count()
