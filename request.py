#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
import json
import argparse


def requset_api():
    
    data = {}
    data['check'] = 'okay'
    
    
    headers = { 'Content-Type': 'application/json'}
    url = 'http://127.0.0.1:50022/ping'
    response = requests.post(url, headers=headers, data=json.dumps(data))

    print(response)
    if response.status_code == 200:
        print(response.text)
    elif response.status_code == 404:
        print('test_error')
        
        
        
if __name__ == "__main__":
    requset_api()


# In[ ]:




