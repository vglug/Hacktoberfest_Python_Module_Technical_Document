#Count the letter b
def countB(word):
    print("The input word is = ",word)
    count=0
    for b in word:
        if(b =='b'):
            count=count+1
    return count
print("Number of 'b' =", countB("abbbabcdefbbghibk"))

#Count the vowels
def countvowels(word):
    print("Word =", word)
    word=word.lower()
    return{
        v:word.count(v) for v in 'aeiou'
        }  
print(countvowels("Currently I am learning about string in python"))
   