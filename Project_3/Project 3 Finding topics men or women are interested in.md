
# Finding Topics Men or Women are Interested in
## Background

One of the biggest problems in dating apps is ghosting. One of the biggest drivers of ghosting is that the users are not interested in the topic brought up by the other party, or is dissapointed with the other party's character or moral values.  

In an attempt to improve chat engagement amongst its users, Tinder is planning to launch a new feature to recommend topics for its users and also check the probability that the opposite party is interested in their topic. The idea behind this feature is to create engaging topics so as to reduce ghosting. 

They have hired you to find out topics that men and women are generally interested in and to better understandthe psychology of men and women to ensure the success of this new campaign.


## Problem Statement

Find topics that can create high engagement for men and women respectively for Tinder's new feature.

Stakeholder 1: Tinder       - increase engagement in tinder (reduce ghosting)  
Stakeholder 2: Tinder users - get increased response!


## Methodology

#### Data Source

To find out the most relevant topics that men/women in the US are interested about, we have gone to Reddit: AskWomen and AskMen and extracted the top questions in the year 2021. We extracted top posts as they are the ones with the highest engagement, which is in line with what Tinder wants in its new feature.

The AskMen subreddit, has a large male audience. Hence, the popular topics will give us a sense of what kind of topics men are interested in.

The AskWomen subreddit has a large female audience. Hence, the popular topics will give us a sense of what kind of topics women are interested in.

#### Method

We have tested 3 models and have obtained the following results when addressing the classification problem. 

|                               | Cross-Val Score | Train Score | Test Score |
|:-----------------------------:|:---------------:|:-----------:|------------|
| Logistic Regression(TVEC)     | 0.7619          | 0.96        | 0.736      |
| Random Forest(CVEC)           | 0.7613          | 0.9393      | 0.73       |
| Support Vector Machine (TVEC) | 0.7573          | 0.9487      | 0.724      |

We are 76% accurate when predicting topics that Men or Women are interested in.


## Conclusions

From the study we can see that women are interested in long term relationships, topics addressing emotions and how to cope with them. With that,  when trying to grab the attention of a female audience, we suggest topics that addresses these:
- what are your views on marriage?
- what are your views on having a child?
- when do you feel most lonely and how do you deal with it?
- the most romantic thing you've ever done

These topics are more descriptive and encourages the repondents to be more elaborate. 

When trying to grab the attention of a male audience, we need to note that they are interested to know more about personality and character of the other party, they are also interested in sex and dating. With that we suggest topics such as: 
- multiple choice quiz about sleepwear 
- short answer questions: what do many people find attractive about you?
- your favourite comedy movie/series (identify sense of humour)