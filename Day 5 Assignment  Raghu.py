#!/usr/bin/env python
# coding: utf-8

# In[161]:


# q2)Make a Function for prime numbers and use Filter to filter out all the prime numbers from 1-2500

def primenumber(num):
    for i in range(2, num):
        if num%i==0:
            break
    else:
        return True
prime_numbers= list(filter(primenumber, range(1, 2500)))
print(prime_numbers)


# In[153]:


# q3)Make a Lambda function for capitalizing the whole sentence passed using arguments.
# And map all the sentences in the List, with the lambda functions

sentences = ['hey this raghu', 'i am learning python with letsupgrade']
capital = map(lambda s: s.upper(), sentences)
print(list(capital))


# In[162]:


# it some time to do


# q1)Write a program to identify sub list [1,1,5] is there in the given list in the same order, if yes print
# “it’s a Match” if no then print “it’s Gone” in function.


# you check the answer by first list and then uncomment second comment the check answer for second list
lst = [1, 5, 6, 4, 1, 2, 3, 5]
# lst = [1, 5, 6, 5, 1, 2, 3, 6]
sublist = [1, 1, 5]
for i in range(0, len(lst)):
    if lst[i]==1:
        for j in range(i+1, len(lst)):
            if lst[j] == 1:
                for k in range(j+1, len(lst)):
                    if lst[k] == 5:
                        print('it\'s a match')
                        break
                else:
                    print('it\'s gone')
                    


# In[ ]:




