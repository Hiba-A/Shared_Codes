#My Functions
#isyes function check the user input if it's yes or no, return boolean
def isyes (userReply):
  userReply = userReply.casefold()
  replylist=userReply.split()
  for i in replylist:
        if i == "yes":
          return True
          break
        elif i == "no":
          return False
          break
        else:
          pass

#Check the user input if it's is (copy,stamps or envelope!!) // returns string
def isword(userReply):
    userReply = userReply.casefold()
    wordlist=userReply.split()
    for i in wordlist:
        if i == "stamps":
            return "stamps"
        elif i == "envelope":
            return "envelope"
        elif i == "copy":
            return "copy"
        else:
            pass 

#Exercise 1: The if Statement
#print("Exercise 1: The if Statement")
userReply1 = input("Do you need to ship a package? (Type yes or no) ")
userRep= isyes(userReply1)
if userRep:
    print("We can help you ship that package!")

#Exercise 2&3: The elif statement
    userReply2 = input("Would you like to buy stamps, an envelope, or make a copy? (Type stamps, envelope, or copy)")
    Reply=isword(userReply2)

    if Reply == "stamps":
        print("We have plenty of stamp designs to  choose from.")
    elif Reply == "envelope":
        print("We have many envelope sizes to choose from.")
    elif Reply == "copy":
        check = False
#Checking the user's input
        while check == False:
            try:
                copies = int(input("How many copies would you like? (Type a number)"))
                print("Here are {} copies".format(copies))
                check = True
            except: 
             print("Sorry this is not a number")
    elif Reply == None:
        print("Sorry! Wrong Entering")   
    else:
        print("Thank you, please come again.")
else:
   print("Please come back when you do need to  ship a package. Thank you.")