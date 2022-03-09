#!/usr/bin/env python
# coding: utf-8

# In[28]:


from flask import Flask


# In[29]:


from flask import request, render_template


# In[30]:


from textblob import TextBlob


# In[31]:


app = Flask(__name__)


# In[32]:


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        print(text)
        r = TextBlob(text).sentiment
        return(render_template("index.html", result = r))
    else:
        return(render_template("index.html", result = "2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




