word1="python programming is fantastic"
word2="Awesome python programming "
#word1="Computer science engineering"
#word2="IFET College" 
#word1="panruti"
#word2="Villupuram"
word1=word1.lower()  
word2=word2.lower()    
print("word1=",word1)
print("word2=",word2)
print("--------The word that appears in word1 also appears in word2--------")
for letter in word1:
    if letter in word2:
        print(letter, end=" ")