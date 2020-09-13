#!/usr/bin/env python
# coding: utf-8

# In[314]:


get_ipython().run_cell_magic('writefile', 'finding_prime.py', "'''\nHey this is a module for finding Prime Number\n'''\ndef primeornot(num):\n    '''\n    Hey this is a function to find given number is prime or not\n    '''\n    if num > 1:\n        for i in range(2, num):\n            if num%i == 0:\n                print('NotPrime')\n                break\n        else:\n            print('Prime')")


# In[315]:


primeornot(9)


# In[316]:


get_ipython().system(' pylint finding_prime.py')


# In[285]:


get_ipython().run_cell_magic('writefile', 'finding_prime.py', '\'\'\'\nHey this is a module for finding Prime Number\n\'\'\'\ndef primeornot(num):\n    """  \n    Hey this is a function to find given number is prime or not\n    """\n    if num > 1:\n        for i in range(2, num):\n            if num%i == 0:\n                print(\'NotPrime\')\n                break\n        else:\n            print(\'Prime\')')


# In[264]:


get_ipython().run_cell_magic('writefile', 'testing.py', "import unittest\nimport finding_prime\n\nclass test(unittest.TestCase):\n    def singletest(self):\n        a = 6\n        result = finding_prime.primeornot(a)\n        self.assertEqual(result, 'NotPrime')\n    \n    def bignumber(self):\n        b = 44\n        result = finding_prime.primeornot(b)\n        self.assertEqual(result, 'Prime')\n        \nif __name__ == '__main__':\n    unittest.main()")


# In[265]:


get_ipython().system(' python testing.py')


# In[ ]:





# In[266]:


# there is no Armstong Number from 0 to 100 so i am ranging from 101 to 999  and 1000 is not Armstong Number
def armstrong():
    for j in range(101, 999):
        digits = list(str(j))
        if int(digits[0])**3 + int(digits[1])**3 + int(digits[2])**3 == j:
            yield j 
            
list(armstrong())


# In[ ]:





# In[ ]:




