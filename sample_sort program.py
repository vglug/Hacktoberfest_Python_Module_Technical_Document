#This is an example program of sort function in list module

list1=(input("Enter the list elements:"))

list1=list1.split()

list2=[int(num) for num in list1]

print("Before sorting :",list2)

list2.sort(key=int)

print("After sorting in ascending order",list2)

list2.sort(reverse=True)

print("After sorting in dscending order",list2)
