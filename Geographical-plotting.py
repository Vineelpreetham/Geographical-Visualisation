#!/usr/bin/env python
# coding: utf-8

# In[1]:


import chart_studio.plotly as py
import plotly.graph_objs as go
import pandas as pd


# In[2]:


from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot


# In[3]:


init_notebook_mode(connected = True)


# In[4]:


data = dict(type = "choropleth",
           locations = ['AZ','CA','NY'],
           locationmode = 'USA-states',
           colorscale = 'portland',
           text = ['ARIZONA','CALI','NEWYORK'],
           z = [1.0,2.0,3.0],
           colorbar = {'title':"colorbar title"}
           )


# In[5]:


layout = dict(geo = {'scope':'usa'})


# In[6]:


choromap = go.Figure(data=[data],layout = layout)


# In[7]:


iplot(choromap)


# In[8]:


df = pd.read_csv('2011_US_AGRI_Exports')


# In[9]:


df.head()


# In[10]:


data = dict(type = 'choropleth',
           colorscale = 'greys',
           locations = df['code'],
           locationmode = 'USA-states',
           z = df['total exports'],
           text =df['state'],
           marker = dict(line =dict(color = 'rgb(255,255,255)',width = 2)),
           colorbar = {'title':'Millions-USD'})


# In[11]:


layout = dict(title ='2011 agriculture exports by states',
              geo = dict(scope ='usa',showlakes =True,
                        lakecolor ='rgb(85,173,240)'))


# In[12]:


choromap = go.Figure(data = [data ], layout = layout)


# In[13]:


iplot(choromap)


# In[14]:


df1= pd.read_csv('2014_World_GDP')


# In[15]:


df1.head()


# In[16]:


data = dict(type = 'choropleth',
           locations = df1['CODE'],
           z = df1['GDP (BILLIONS)'],
           text = df1['COUNTRY'],
           colorbar = {'title':'GDP billons us}'},
           )


# In[17]:


layout =dict(title = ' 2014 GDP',
            geo = dict(showframe = False,
                      projection = {'type':'orthographic'}))


# In[128]:


coromap2 = go.Figure(data =[data],layout = layout)
iplot(coromap2)


# In[ ]:




