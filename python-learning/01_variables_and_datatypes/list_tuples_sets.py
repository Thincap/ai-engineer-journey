courses = ['Computer Networks', 'Data Structures', 'Operating Systems', 'Database Management Systems']

# Accessing elements in a list
print(courses[0])  # Output: Computer Networks
print(courses[1])  # Output: Data Structures
print(courses[2])  # Output: Operating Systems
print(courses[3])  # Output: Database Management Systems

# Accessing elements using negative indexing
print(courses[-1])  # Output: Database Management Systems
print(courses[-2])  # Output: Operating Systems
print(courses[-3])  # Output: Data Structures
print(courses[-4])  # Output: Computer Networks

# Accessing a range of elements in a list  (here the first index is inclusive and the second index is exclusive)
print(courses[0:2])  # Output: ['Computer Networks', 'Data Structures']
print(courses[1:3])  # Output: ['Data Structures', 'Operating Systems']


# How to add an element to a list
courses.append('Artificial Intelligence')
print(courses)  # Output: ['Computer Networks', 'Data Structures', 'Operating Systems', 'Database Management Systems', 'Artificial Intelligence']


# how to insert an element at a specific index in a list
courses.insert(2, 'Machine Learning')
print(courses)  # Output: ['Computer Networks', 'Data Structures', 'Machine Learning', 'Operating Systems', 'Database Management Systems', 'Artificial Intelligence']


# When to use extend() in Python lists

courses1 = ['History', 'Maths']
courses.append(courses1)
print(courses)  # Output: ['Computer Networks', 'Data Structures', 'Machine Learning', 'Operating Systems', 'Database Management Systems', 'Artificial Intelligence', ['History', 'Maths']]

print(courses[6])  # Output: ['History', 'Maths']


# now let's use extend() to add the elements of courses1 to courses as individual elements
courses2 = ['Physics', 'Chemistry']
courses.extend(courses2)
print(courses)  # Output: ['Computer Networks', 'Data Structures', 'Machine Learning', 'Operating Systems', 'Database Management Systems', 'Artificial Intelligence', ['History', 'Maths'], 'Physics', 'Chemistry']

# how to remove an element from a list
courses.remove('Computer Networks')
print(courses)  # Output: ['Data Structures', 'Machine Learning', 'Operating Systems', 'Database Management Systems', 'Artificial Intelligence', ['History', 'Maths'], 'Physics', 'Chemistry']

 # how to remove an element from a list using pop() method
popped_element = courses.pop() # it removes the last element from the list
print(popped_element)  # Output: Chemistry
print(courses)  # Output: ['Data Structures', 'Machine Learning', 'Operating Systems', 'Database Management Systems', 'Artificial Intelligence', ['History', 'Maths'], 'Physics']


# Sorting a list 
courses.remove(['History', 'Maths']) # it removes the list ['History', 'Maths'] from the courses list
courses.sort() # it sorts the list in ascending order
print(courses)  # Output: ['Artificial Intelligence', 'Data Structures', 'Database Management Systems', 'Machine Learning', 'Operating Systems', 'Physics']

nums = [4,6,1,3,45,9,60]
nums.sort() # it sorts the list in ascending order
print(nums)  # Output: [1, 3, 4, 6, 6, 9, 45, 60]


courses.sort(reverse=True) # it sorts the list in descending order
print(courses)  # Output: ['Physics', 'Operating Systems', 'Machine Learning', 'Database Management Systems', 'Data Structures', 'Artificial Intelligence']

nums.sort(reverse=True) # it sorts the list in descending order
print(nums)  # Output: [60, 45, 9, 6, 6, 4, 3, 1]

# when to use sorted() in Python lists (when you want to sort a list without modifying the original list)
courses = ['Computer Networks', 'Data Structures', 'Operating Systems', 'Database Management Systems']
sorted_courses = sorted(courses) # it returns a new list with the elements sorted in ascending order
print(sorted_courses)  # Output: ['Computer Networks', 'Data Structures', 'Database Management Systems', 'Operating Systems']
print(courses)  # Output: ['Computer Networks', 'Data Structures', 'Operating Systems', 'Database Management Systems'] (original list is not modified)


# min() and max() and sum() functions in Python lists
nums = [4, 6, 1, 3, 45, 9, 60]
print(min(nums))  # Output: 1
print(max(nums))  # Output: 60
print(sum(nums))  # Output: 134

# Finding the index of an element in a list using index() method
courses = ['Computer Networks', 'Data Structures', 'Operating Systems', 'Database Management Systems']
print(courses.index('Data Structures'))  # Output: 1
# print(courses.index('Machine Learning'))  # Output: ValueError: 'Machine Learning' is not in list (if the element is not found in the list)



# Tuples in Python
# Tuples are immutable (cannot be changed) and ordered collection of elements whereas lists are mutable (can be changed) and ordered collection of elements. Tuples are defined using parentheses () whereas lists are defined using square brackets [].

# Mutable
list1 = ['History', 'Maths', 'Physics']
list2 = list1

print(list1)  # Output: ['History', 'Maths', 'Physics']
print(list2)  # Output: ['History', 'Maths', 'Physics']

list1[0] = 'Biology'  # it changes the first element of the list1 to 'Biology'
print(list1)  # Output: ['Biology', 'Maths', 'Physics']
print(list2)  # Output: ['Biology', 'Maths', 'Physics']

# Immutable
tuple1 = ('History', 'Maths', 'Physics')
tuple2 = tuple1

print(tuple1)  # Output: ('History', 'Maths', 'Physics')
print(tuple2)  # Output: ('History', 'Maths', 'Physics')

# tuple1[0] = 'Biology'  # it raises TypeError: 'tuple' object does not support item assignment (tuples are immutable)
# print(tuple1)  # Output: ('History', 'Maths', 'Physics')
# print(tuple2)  # Output: ('History', 'Maths', 'Physics')

# Sets in Python
# Sets are unordered collection of unique elements(No duplicates). Sets are defined using curly braces {}.

courses_set = {'CN', 'DSA', 'OS', 'DBMS', 'CN'}  # it removes the duplicate element 'CN' from the set
print(courses_set)  # Output: {'CN', 'DSA', 'OS', 'DBMS'} (the order of the elements may vary as sets are unordered)    

# intersection(), Difference(), union() methods in Python sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.intersection(set2))  # Output: {4, 5} (returns the common elements in both sets)
print(set1.difference(set2))  # Output: {1, 2, 3} (returns the elements in set1 that are not in set2)
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5, 6, 7, 8} (returns all the unique elements in both sets)

# how to create an empty list, tuple and set in Python
empty_list = []
empty_list = list()  # it creates an empty list

empty_tuple = ()
empty_tuple = tuple()  # it creates an empty tuple

empty_set = set()  # it creates an empty set
# empty_set = {} (This is not correct , as it will create empty Dictonary and not an empty set)