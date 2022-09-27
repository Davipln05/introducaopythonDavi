#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install googlenews')


# In[7]:


from GoogleNews import GoogleNews
import pandas as pd


# In[9]:


googlenews = GoogleNews()
googlenews.set_lang('pt')
googlenews.set_period('5d')


# In[10]:


googlenews.clear()


# In[11]:


googlenews.search('Bolsonaro')


# In[12]:


googlenews.total_count()


# In[13]:


pesquisa_bolsonaro = googlenews.results()


# In[14]:


df_bolsonaro = pd.DataFrame(pesquisa_bolsonaro)


# In[15]:


display(df_bolsonaro)


# In[16]:


googlenews.clear()


# In[17]:


pesquisa_lula = goolenews.search('Lula')


# In[18]:


pesquisa_lula = googlenews.search('Lula')


# In[19]:


googlenews.total_count()


# In[20]:


pesquisa_lula = googlenews.results()


# In[21]:


df_lula = pd.DataFrame(pesquisa_lula)


# In[22]:


display(df_lula)


# In[23]:


googlenews.clear()


# In[24]:


pesquisa_neymar = googlenews.search('Neymar')


# In[25]:


googlenews.total_count()


# In[26]:


pesquisa_neymar = googlenews.results()


# In[27]:


df_neymar = pd.DataFrame(pesquisa_neymar)


# In[28]:


display(df_neymar)


# In[29]:


googlenews.clear()


# In[30]:


get_ipython().system('pip install pyton-twitter-v2')
get_ipython().system('pip install snscrape')


# In[31]:


get_ipython().system('pip install python-twitter-v2')
get_ipython().system('pip install snscrape')


# In[33]:


import snscrape.modules.twitter as dados
import pandas as pd
import datetime


# In[34]:


lista_twittes_bolsonaro = []


# In[46]:


data_final = datetime.date.today()
data_inicial = '2022-1-1'


# In[52]:


for i, tweet in enumerate(dados.TwitterSearchScraper(f'{"Bolsonaro"} + since:{data_inicial} until:{data_final}').get_items()):
    if i>500:
        break
    lista_twittes_bolsonaro.append([tweet.date, tweet.id, tweet.content, tweet.username])


# In[53]:


df_bolsonaro = pd.DataFrame(lista_twittes_bolsonaro, columns=['Datatime', 'Tweet Id', 'text', 'Username'])


# In[54]:


display(df_bolsonaro)


# In[ ]:




