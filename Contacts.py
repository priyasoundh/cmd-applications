def search(name,dict1):
  count=0
  for x in dict1.keys():
    if(name.lower()==x.lower()):
      return x
      count=count+1
  print("contact not found")
  print("suggestionns are")
  for x in dict1.keys():
    if x.__contains__(name) :
        print(x)
  return 0

def count(dict1):
  s=0
  for x in dict1.keys():
    s=s+1
  return s

def searchnum(name,dict1):
  if name in dict1:
    return dict1[name]

def create(di,dict1):
  l=0
  name=input("enter the name:")
  while(l!=10):
    number=input("enter the number:")
    l=len(number)
    if(l!=10):
      print("enter a valid number")
  count=0
  while(count!=1):
    mail=input("enter the mailid:")
    for x in mail:
      if(x=='@'):
        count=count+1
    if(count!=1):
      print("enter a valid mail")
      count=0
  di={"number":number,"mail":mail}
  dict1[name.lower()]=di
  return dict1

print("Welcome to contacts")
dict1={}
di={}
while(1):
  print("1--> create a contact")
  print("2--> delete a contact")
  print("3--> edit a contact")
  print("4--> search a contact")
  print("5--> display contact")
  print("6--> exit")
  x=int(input())

  if(x==1):
    dict1=create(di,dict1)
    print("successfully created a contact")

  elif(x==2):
    s=count(dict1)
    if(s==0):
      print("contact list is empty")
    else:
      name=input("enter the name to delete:")
      x=search(name,dict1)
      if(x==1):
        dict1.pop(name)
        print("successfully deleted a contact")
      elif(x==0):
        print("contact doesn't exist")

  elif(x==3):
    s=count(dict1)
    if(s==0):
      print("contact list is empty")
    else:
      print("1--> edit number")
      print("2--> edit Name")
      print("3--> edit mail")
      d=int(input())

      if(d==1):
        name=input("enter the name to edit:")
        x=search(name,dict1)
        if(x==1):
          num1,mail1=searchnum(name,dict1)
          mail=dict1[name][mail1]
          number=input("enter the number:")
          di={"number":number,"mail":mail}
          dict1[name]=di
          print("successfully edited a contact")
        elif(x==0):
          print("contact doesn't exist")

      elif(d==2):
        name=input("enter name to edit:")
        x=search(name,dict1)
        if(x==1):
          num1,mail1=searchnum(name,dict1)
          num=dict1[name][num1]
          mail=dict1[name][mail1]
          dict1.pop(name)
          name=input("enter the name:")
          di={"number":num,"mail":mail}
          dict1[name]=di
          print("successfully edited a contact")
        elif(x==0):
          print("contact doesn't exist")
      
      elif(d==3):
        name=input("enter the name to edit:")
        x=search(name,dict1)
        if(x==1):
          num1,mail1=searchnum(name,dict1)
          num=dict1[name][num1]
          dict1.pop(name)
          mail=input("enter the mail:")
          di={"number":num,"mail":mail}
          dict1[name]=di
          print("successfully edited a contact")
        elif(x==0):
          print("contact doesn't exist")

  elif(x==4):
    s=count(dict1)
    if(s==0):
      print("contact list is empty")
    else:
      name=input("enter the name to search:")
      x=search(name,dict1)
      if(x!=0):
        print(dict1[x])
  
  elif(x==5):
    s=count(dict1)
    print("you have ",s," contacts")
    print(dict1)

  elif(x==6):
    print("thank you")
    break

  print("****************************************************")
