class library:
   def __init__(self,booklist):
      self.books=booklist
      self.borrowedbooks=[]
   def displaybooks(self):
      for book in self.books:
         print(book)        
   def borrowbooks(self,bookname):
      if bookname in self.books:
        self.books.remove(bookname)
        self.borrowedbooks.append(bookname)
        print("it is borrowed successfully")
      else:
         print("it is not found")
   def returnbooks(self,bookname):
      if bookname in self.borrowedbooks:
         self.books.append(bookname)
         self.borrowedbooks.remove(bookname)
         print("it is returned successfully")
      else:
         print("it is not returned successfully")
borrowedbooks=["python","java","c"]
lib=library(borrowedbooks)
while (True):
   print("library function")
   print("1. displaybooks")
   print("2.borrowedbooks")
   print("3.returnbooks")
   print("4.exit")
   choice=int(input("enter your correct choice:"))
   if choice==1:
      lib.displaybooks()
   elif choice==2:
      borrowedbooks=input("enter your borrowed books:")
      lib.borrowbooks(borrowedbooks)
   elif choice==3:
      returnbook=input("enter your return books:")
      lib.returnbooks(returnbook)
   elif choice==4:
      print("exit")
      break
   else:
      print("invalid")
