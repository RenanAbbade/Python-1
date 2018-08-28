
# coding: utf-8

# In[17]:

import matplotlib.pyplot as plt

population_ages = [14, 44, 21, 34,65,12,42,122,5,55,43,23,12,10,11]

ids = [x for x in range(len(population_ages))]
plt.bar(ids, population_ages)

plt.xlabel("Eixo x->")
plt.ylabel("Eixo y->")
plt.title("Renan First Graph \n Subline")
plt.legend()

plt.show()


# In[ ]:




# In[ ]:



