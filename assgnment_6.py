# ASSIGNMENT 6

""" Q.1. What are keywords in python? Using the keyword library, print all the python keywords.
ANS - keywords are reserved words in python. we cant use them as variable names, function names or class names
ex - True,False,default, break etc
"""

import keyword
print(keyword.kwlist)

"""
Q.2. What are the rules to create variables in python?
ANS --rules to create variables in python
1. variables should always start with an alphabet or an underscore
2. the variable name should contain only alphanumeric and underscore
3. variables can not start with a number
4. variable names are case sensitive 
"""

"""
Q.3. What are the standards and conventions followed for the nomenclature of variables in
python to improve code readability and maintainability?
ANS --standards followed are 
1. the names should be clear and concise
2. names should be written in english words
3. they should not collide with any python keywords
"""

"""Q.4. What will happen if a keyword is used as a variable name?
ANS -- it will give syntax error.
"""

#break = 1234
#print(break)

"""
Q.5. For what purpose def keyword is used?
ANS --  def keyword is used to define the function in python. by using def keyword, we can define or instruct
the computer the task that function is supposed to perform
"""

"""
Q.6. What is the operation of this special character ‘\’?
ANS -- \ is used along with another character as a unicode for different purpose
ex: \n - here it is used as one character string indicating  new line
"""

"""
Q.7. Give an example of the following conditions:
(i) Homogeneous list -- l1 = [12,23,34,45,23,34]
(ii) Heterogeneous set -- s1 = {23,"hello",True,56}
(iii) Homogeneous tuple -- s3 = ("hello","hi","good day")

"""

"""
Q.8. Explain the mutable and immutable data types with proper explanation & examples.
ANS -- mutable datatypes are those entities whose values of the elements can be modified in the run time.
       ex: list is a mutable data type. because we can modify the values stored in the elements of the list.
         l1 = [12,23,"hello",False]
         l2[1] = 100
         in the above case one can modify the value of elements of the list
         
     on the other hand immutable datatypes are those entities whose values  can not be changed or modified
      ex: tuple 
      we can not modify the values in tuples.
"""

"""
Q.9. Write a code to create the given structure using only for loop.
*
***
*****
*******
*********
"""

n=5
k = n*2
for i in range(0, k):
    for j in range(0, k):
        print(end=" ")

    k = k - 1

    for j in range(0, i + 1):
        if (i+1)%2 ==0:
            pass
        else:
             print("* ", end="")

    print("\r")

"""
Q.10. Write a code to create the given structure using while loop.
|||||||||
|||||||
|||||
|||
|
"""

n= 5
k = n*2
m = 1

while k>=1:
    j=1
    while j<=m:
        print(end=" ")
        j = j+1

    j = 1
    while j <= k:
        if k%2 ==0:
            pass
        else:
            print("|",end="")
        j = j +1

    k=k-1

    n+=1
    m=m+0.5


    print("\r")

















