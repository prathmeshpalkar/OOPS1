#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Write a Python for loop that prints the numbers from 1 to 10.
for i in range(1, 11):
    print(i)


# In[10]:


#Create a list of fruits (e.g., ["apple", "banana", "cherry"]) and write a for loop to print each fruit in the list
fruits = ['banan', 'mango', 'cherry']
for x in fruits:
    print ('fruits: ', x)


# In[11]:


#Write a Python program that calculates the sum of all even numbers from 1 to 50 using a for loop.
sum = 0

for number in range(1, 51):
    # Check the number is even
    if number % 2 == 0:
        
        sum += number

# Print the final sum
print("The sum of even numbers is:", sum)


# In[13]:


#Create a list of integers, and using a for loop, find and print the largest number in the list.

numbers = [25, 26, 79, 23, 56, 89, 28, 67]

largest = numbers[0] 

for number in numbers:
    if number > largest:
        largest = number 

print("The largest number in the list is:", largest)



# In[2]:


#Write a Python program that takes a list of dictionaries, where each dictionary represents a person with keys "name" and "age." Find and print the average age of all the people in the list.


people = [
    {"name": "ABC", "age": 30},
    {"name": "XYZ", "age": 25},
    {"name": "CDE", "age": 35},
    {"name": "GHI", "age": 40},
]

total_age = sum(person["age"] for person in people)
average_age = total_age / len(people)

# Print the average age
print(f"The average age of the people is {average_age:.2f} years.")


# In[ ]:


#Write a Python program that uses a for loop to find and print all the prime numbers between 1 and 100. A prime number is a positive integer greater than 1 that has no positive integer divisors other than 1 and itself.




# In[2]:


#Create a dictionary representing a simple inventory system for a store. Implement a function that allows you to update the quantity of items in the inventory by specifying the item name and the new quantity.


inventory = {
    "item1": {"name": "ABC", "quantity": 50},
    "item2": {"name": "XYZ", "quantity": 100},
    "item3": {"name": "GHI", "quantity": 75},
}

def Update inventory = ['item1' {'name': "ABC" 'quantity':60}]


# In[ ]:




