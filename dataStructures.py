#Learn data Structures and algorithms using Python
#Big 'O" notation
#deals with calculating the time complexity of a program
#Big "O" Notation===Actual Definition cont..
#What does this Big "O" Notation has to do with Data Structures?
#1.certain operations can be more or less costly depending on the data structure used.
#example: accessing an array by index.
#  Problem with using array --- the need to constantly call array with its index is not really effective in case of large arrays
# 2. Companies will always ask you during interviews to get to know if you really understand how scalable an algorithm is,
# 3. knowing the big "O" notation will make you a better developer or software engineer#

def arry():
    intgerList = [1, 2, 3, 4, 5]
    name = "gamegroup"
    print("The First Element in our List is : "+str(intgerList[0]))
    print("The Second Element in our List is : "+str(intgerList[1]))
    print("The Third Element in our List is : "+str(intgerList[2]))
    print("The Fourth Element in our List is : "+str(intgerList[3]))
    
arry()
#Having an algorithm that has a single operation which takes a single time to run ---- has a time complexity of 1

#Printing through an array 
def repeatarr():
    for value in range(0, 100, 2):
        print("Currently Printing....: " + str(value))
        print("\n")
    print("Printing Complete.")

repeatarr()


