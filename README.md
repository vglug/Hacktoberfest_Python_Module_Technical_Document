Syntax for a List:
       Listname=[A1,A2,..]
Function in List:
* append():listname.append(new element)
* insert():listname.insert(indexnumber,element)
* Extend():listname.Extend([v1,v2,..])
* remove():listname.remove(element)
* pop():listname.pop(position)

#We can add last element in List
mylist=[10,20,30,40]
mylist=append(50)
print(mylist)

#We can add element in list using index number 
List=[30,48,23,28,40]
List.insert(2,50)
print(List)

#We use extend() to print 2list as 1list
a=['p','r','s']
b=['d','g','i']
a.extend(b)
print(a)

#We use pop() to remove a element using index number 
a=[10,20.6,3,30]
a.pop(3)
print(a)

#remove() is used to remove a element in list using the element 
a=['a','b','c','d']
a.remove('b')
print(a)
