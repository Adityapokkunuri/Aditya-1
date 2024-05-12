#creating a set 
set1={10,20,30,40,50}
print(set1)

#adding elements into a set
set1.add(60)
print(set1)

#removing element from the set
set1.remove(50)
print(set1)

#updating the elements in a set
set1.discard(10)
print(set1)

#remove () will raise an error if the element is not present in the set, while discard () will not.