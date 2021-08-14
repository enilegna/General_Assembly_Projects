#!/usr/bin/env python
# coding: utf-8

# In[2]:


import gradio as gr
import torch
import torchvision
from torchvision import transforms
import numpy as np
import pandas as pd
import os
from PIL import Image

# Images
torch.hub.download_url_to_file('https://github.com/enilegna/General_Assembly_Projects/blob/main/Project_5/Capstone/Examples/covid1.png', 'covid1.png')
torch.hub.download_url_to_file('https://github.com/enilegna/General_Assembly_Projects/blob/main/Project_5/Capstone/Examples/thorax1.jpeg', 'thorax1.jpeg')
torch.hub.download_url_to_file('https://github.com/enilegna/General_Assembly_Projects/blob/main/Project_5/Capstone/Examples/normal1.jpg', 'normal1.jpg')


# In[3]:


resnet18 = torchvision.models.resnet18()
#change output features from pretrain 1000 to 3 as we only have 3 classes
resnet18.fc = torch.nn.Linear(in_features=512, out_features=3)

checkpoint = 'https://github.com/enilegna/General_Assembly_Projects/blob/main/Project_5/Capstone/Models/Resnet18-6/resnet18_epoch8.pth'
resnet18.load_state_dict(torch.hub.load_state_dict_from_url(checkpoint))


# In[4]:


#set learning rate as 3e-4
lr = 3e-4
#Declare criterion
loss_fn = torch.nn.CrossEntropyLoss()
#Declare adam optimizer with a learning rate of lr
optimizer = torch.optim.Adam(resnet18.parameters(), lr=lr)


# In[5]:


resnet18.eval()


# In[6]:


labels = ['normal','thoraxdisease', 'covid']


# In[7]:


def test(inp):
    inp = Image.fromarray(inp, 'RGB')
    inp = transforms.Resize(size=(224, 224))(inp)
    inp = transforms.ToTensor()(inp).unsqueeze(0)
    inp = transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])(inp)
    with torch.no_grad():
        prediction = torch.nn.functional.softmax(resnet18(inp)[0], dim=0)
    return {labels[i]: float(prediction[i]) for i in range(3)}


# In[8]:


inputs = gr.inputs.Image()
outputs = gr.outputs.Label(num_top_classes=3)

examples=[["covid1.png"],["normal1.jpg"], ["thorax1.jpeg"]]

gr.Interface(fn=test, inputs=inputs, outputs=outputs, examples=examples, title="Identifying COVID-19 Pneumonia", 
                  description="Predicts whether COVID-19 Penumonia is present in CXR. This model is EXPERIMENTAL and should only be used for research purposes. Please see a doctor for any diagnostic reasons. Please upload a Chest X-Ray image in JPG, JPEG  or PNG.").launch()

