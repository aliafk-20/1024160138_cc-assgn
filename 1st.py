#1 i)
roll_no = (input("roll no. "))
L = [int(digit) * 10 for digit in roll_no]
print("L:", L)

#ii)
L.append(100)
print("after append:", L) 

L.insert(2, 25)
print("after insert:", L)  # 25 is inserted at index 2

#iii)
L.pop(0)
print("after pop: ", L)

L.remove(25)
print('after removal:', L)

#iv)
L.sort()
print("ascending order:", L)

L.sort(reverse=True)
print("descending order:", L)

#v)
print("first three elements:", L[:3])
print("last three elements:", L[-3:])

#vi)
avg= sum(L)/len(L)
new_list = [x for x in L if x > avg]
print("average:", avg)
print("elements greater than average:", new_list)

#2nd)
scores = tuple(L[:8])
print("Scores tuple:", scores)

#i)
highest = max(scores)
highest_index = scores.index(highest)

lowest = min(scores)
lowest_count = scores.count(lowest)

print("highest score:", highest)
print("index of highest score:", highest_index)
print("lowest score:", lowest)
print("number of times lowest score appears:", lowest_count)

#ii)
#tuples can not be reversed as they are immutable.
reversed_scores = list(reversed(scores))

print("Reversed tuple as a list:", reversed_scores)

#iii)
user_score = int(input("Enter a score to search: "))

if user_score in scores:
    print("First occurrence index:", scores.index(user_score))
else:
    print("Score is not present in the tuple.")


#iv)
# scores[0] = 100

#v)
first_score, second_score, *remaining_scores = scores

print("First score:", first_score)
print("Second score:", second_score)
print("Remaining scores:", remaining_scores)

import random

roll_no = int(input("enter your roll number: "))
random.seed(roll_no)


#3)

# i)
numbers = [random.randint(100, 900) for _ in range(100)]
print("random numbers:", numbers)

# ii)
odd_numbers = [num for num in numbers if num % 2 != 0]
print("odd numbers:", odd_numbers)
print("count of odd numbers:", len(odd_numbers))

# iii)
even_numbers = [num for num in numbers if num % 2 == 0]
print("even numbers:", even_numbers)
print("count of even numbers:", len(even_numbers))

# iv)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = [num for num in numbers if is_prime(num)]
print("prime numbers:", prime_numbers)
print("count of prime numbers:", len(prime_numbers))

# v)
most_frequent = max(set(numbers), key=numbers.count)
frequency = numbers.count(most_frequent)

print("most frequent number:", most_frequent)
print("number of times it occurs:", frequency)

# Q4

roll_no = input("enter your roll number: ")
digits = [int(digit) for digit in roll_no[:8]]

A = {digit * 7 for digit in digits}
B = {digit * 9 for digit in digits}

print("set A:", A)
print("set B:", B)

# vi)
union = A.union(B)
print("union:", union)

# vii)
intersection = A.intersection(B)
print("intersection:", intersection)

# viii)
A_difference_B = A.difference(B)
B_difference_A = B.difference(A)

print("A - B:", A_difference_B)
print("B - A:", B_difference_A)
print("difference() gives one-sided differences, while symmetric_difference() gives values unique to either set.")

# ix)
symmetric_difference = A.symmetric_difference(B)
print("symmetric difference:", symmetric_difference)

# x)
print("A is subset of B:", A.issubset(B))
print("B is superset of A:", B.issuperset(A))

# xi)
X = int(input("enter a value to remove from A: "))
A.discard(X)
print("set A after discard:", A)
print("discard() is safer because it does not raise an error if the value does not exist.")

my_dict = {
    "name": "your name",
    "roll_no": "your roll number",
    "branch": "your branch",
    "age": 20,
    "city": "your city"
}

# i)
my_dict["location"] = my_dict.pop("city")
print("dictionary after renaming city:", my_dict)

# ii)
my_dict["cgpa"] = 8.5
print("dictionary after adding cgpa:", my_dict)

# iii)
my_dict["age"] += 1
print("dictionary after updating age:", my_dict)

# iv)
dict_pop = my_dict.copy()
dict_del = my_dict.copy()

removed_value = dict_pop.pop("branch")
del dict_del["branch"]

print("dictionary after pop:", dict_pop)
print("dictionary after del:", dict_del)
print("pop() returns the removed value while del only deletes the key.")

# v)
for key, value in my_dict.items():
    print(f"{key} → {value}")

# vi)
if "email" in my_dict:
    print("email →", my_dict["email"])
else:
    print("email is not present in the dictionary.")

# vii)
friend_dict = {
    "name": "rahul",
    "roll_no": "12345678",
    "branch": "cse",
    "age": 21,
    "city": "delhi"
}

merged_dict = {**my_dict, **friend_dict}
print("merged dictionary:", merged_dict)
print("when both dictionaries have the same key the value from the second dictionary wins.")

# viii)
string_values = {key: value for key, value in my_dict.items() if isinstance(value, str)}
print("dictionary containing only string values:", string_values)