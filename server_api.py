#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask, jsonify, request, Response, abort
import json 

app = Flask(__name__)

@app.route('/ping', methods=['POST']) #test api
def hello_world():
    data = json.loads(request.data)

    if data['check'] == 'okay' :
        return jsonify("ping")
    else:
        return abort(404)

if __name__ == "__main__":
    app.run(port=50022)


# In[ ]:




