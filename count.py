#Count the letter 
print("-------Count the letter-------")
def countB(word):
    print("Word = ",word)
    count=0
    for b in word:
        if(b =='b'):
            count=count+1
    return count
print("Number of 'b' =", countB("abbbabcdefbbghibka"))

  

#Count the vowels
print("-------Count the Vowels in a string-------")
def countvowels(word):
    print("Word =", word)
    word=word.lower()
    return{
        v:word.count(v) for v in 'aeiou'
        }  
print(countvowels(" Python string is a data type used to represent a sequence of characters"))
   