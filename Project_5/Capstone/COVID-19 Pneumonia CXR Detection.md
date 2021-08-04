
## Background

  

The novel coronavirus COVID-19 is a new strain of virus that belongs to the acute respiratory syndromes. The outbreak was first identified in China around November 2019 and have since evolved to a worldwide pandemic.

Amongst medical supplies, many countries facing the brunt of the pandemic are also facing [shortages of healthcare workers]( https://www.abc.net.au/news/2021-07-14/trainee-doctors-on-the-front-line-of-indonesia-covid-disaster/100285804), namely developed countries like Indonesia, India, and Philippines.

The exponential spread of COVID-19, and the increasing number of healthcare workers that has fallen victim to the virus, has led to a demand in technology that can help alleviate the stress this virus has created in the healthcare industry.

## The role of Chest Radiographs (CXR) in treating COVID-19

Chest radiographs (CXR) are widely used for the screening and management of COVID-19.

  

As hospitals has reached maximum capacity, a positive reverse transcription polymerase chain reaction (RT-PCR) test is no longer the deciding factor for doctors to admit patients. Instead, CXR results have now become an essential tool to determine which patients should be prioritised for hospital treatment.

  

Aside from that, patients who have recovered from COVID-19 may still suffer from chronic lung abnormalities that would be fatal if early prevention is not performed.

## Challenges of Diagnosing COVID-19 Pneumonia in CXR

  

Findings of COVID-19 in CXR can be very subtle, in one [study](https://pubs.rsna.org/doi/full/10.1148/radiol.2020200823) that measures the sensitivity of COVID-19 amongst China and US radiologists, it was shown that the average sentivities of radiologists in identifying COVID-19 pneumonia is 80.4%.


We will use this as an industry benchmark when evaluating the model.

## Using AI to help diagnose the presence of COVID-19 Pneumonia

In this project, our aim is to help create an early warning tool for the detection of COVID-19 pneumonia to alleviate some of the load on radiologists. Since we are predicting a fatal and highly contagious virus, we will focus on minimizing false negatives, prioritizing **F1** as an **evaluation metric** and Sensitivity when comparing with the industry benchmark of 80.3%. 

## Dataset
Source: [Kaggle](https://www.kaggle.com/c/csc532-2/)
Data Type: JPEG, JPG, PNG

**Train Dataset**:  5,507 Images
|Classes|Sample Size  | %|
|--|--|--|
| Covid-19 Pneumonia | 363 | 6.5%|
| No Findings | 1,408 | 25.6%|
| Thorax Disease | 3,763 | 67.9%|

**Validation Dataset** : 1,130 Images 
(for Kaggle submission)

## Model 
|Model| Libraries | Kaggle Score |
|--|--|--|
| Resnet-18 | Pytorch |90.4%


Final model used was the Resnet18 Model with 
## Conclusions

The Resnet18 has performed better on the dataset. 

## Limitations

This experiment is highly controlled, where our dataset is only exposed to 3 classifications. In real life, there are many more CXR abnormalities that are outside of these classes. As we have not tested our model to other potential classes, the effectiveness of our model is limited to only 3 classes (COVID, Thorax Disease, Normal). The model may perform poorly when exposed to other classes.

In addition, having looked through the misclassified images, we realize that many misclassifications can be attributed to poor quality CXR. In order to create a decent early warning tool for COVID-19 Pneumonia, we will need to create a model that can also determine the usability of the CXR.

This model should be used in conjunction with clinical findings to form an overall clinical assessment, as  [studies](https://www.bmj.com/content/370/bmj.m2426)  have shown that no single feature on chest radiography is diagnostic of covid-19 pneumonia.

