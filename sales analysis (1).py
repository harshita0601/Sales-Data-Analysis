#!/usr/bin/env python
# coding: utf-8

# # Aludecor Sales Analysis
# 
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# 

# In[1]:


pip install fpdf

pip install Pyppeteer
# In[2]:


pip install nbconvert


# In[3]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from fpdf import FPDF


# In[4]:


df=pd.read_csv("Important sheets - Customer_Masters.csv")
df2=pd.read_csv("Important sheets - InvoiceRegister.csv")
df3=pd.read_csv("Important sheets - SalesActiveEmpList.csv")


# In[5]:


df2.head()


# In[6]:


df2.tail()


# In[7]:


df2.shape


# In[8]:


df2.columns


# In[9]:


df2.info()


# In[10]:


df2.isnull().sum()


# In[11]:


df2=df2.dropna()
df2.isnull().sum()


# In[12]:


df2.describe()


# In[13]:


df2['Month']=df2[" INV CREATION DT"].str[3:5]
df2['Month']=df2['Month'].astype('int32')
df2.head()


# In[14]:


#Which was the best month for sales? 


df2["Qty"]=df2["Qty in SQM"].astype("int32")
df2["Sales"]=df2["NET VAL (LC)"].astype("int32")


# In[15]:


results=df2.groupby('Month').sum()


# In[16]:


df2.groupby('Month').sum()['Sales']


# In[17]:


#which Team has the highest number of sales?


results=df2.groupby('Team_Name').sum()
results


# In[18]:


import matplotlib.pyplot as plt

Team_Name = [Team_Name for Team_Name, df in df2.groupby('Team_Name')]

plt.bar(Team_Name, results['Sales'])
plt.xticks(Team_Name, rotation ='vertical', size=12)
plt.xlabel('City Name')
plt.ylabel('Sales in SQM')
plt.show()


# In[19]:


# Where was the most supply ?


plt.figure(figsize=(50,30.5))
sns.countplot(df2['Team_Name'])
plt.xticks(rotation='vertical',size=60)
plt.yticks(rotation='horizontal',size=55)
plt.show()


# In[20]:


#Best Selling Products


# In[21]:


#Inserting Product Column

df2["Product"]=df2["MATERIAL DESCRIPTION"].str[0:4]
df2["Product"]=df2["Product"].astype(str)
df2


# In[22]:


#grouping product name
prod_sales=pd.DataFrame(df2.groupby('Product').sum()['Inv Qty'])


# In[23]:


#sorting Prod sales column
prod_sales=prod_sales.sort_values('Inv Qty',ascending=False)


# In[24]:


# top 10 products by sales


prod_sales[:10]


# In[25]:



plt.figure(figsize=(30,20.5))
sns.countplot(df2['Product'])
plt.xticks(rotation='vertical',size=30)
plt.yticks(rotation='horizontal',size=25)
plt.xlabel('Product',size=50)
plt.ylabel('Quantity Ordered',size=50)
plt.show()


# In[28]:


prices = df2.groupby('Product').mean()

fig, ax1 = plt.subplots()

##ax2 = ax1.twinx()
ax1.bar(df2['Product'],df2['Inv Qty'], color='g')
ax2.plot(df2['Product'],df2['Sales'], color='b')

ax1.set_xlabel('Product Name')
ax1.set_ylabel('Quantity Ordered', color='g')
ax2.set_ylabel('Price ($)', color='b')
ax1.set_xticklabels(df2['Product'], rotation='vertical', size=8)

fig.show()


# In[ ]:





# In[ ]:




