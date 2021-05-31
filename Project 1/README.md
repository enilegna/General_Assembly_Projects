# Project 1: SAT & ACT Analysis


## Problem Statement
The College Board SATs was the first standardized test created for college admission tests in the United States. 40 years later in 1959, with the introduction of the ACT as a standardized college admission test and increase in the umber of schools accepting both the ACT and SAT, the number of students participating in SATs gradually decreased.  
*[The Olive Book, Do Ivy League Schools Prefer the SAT?](https://theolivebook.com/do-colleges-prefer-the-sat-or-the-act/)*

In 2016, the College Board decided to launch a new version of the SAT with the following updates: less of the tricky vocabulary that was long a hallmark of the test. The new version also dropped the “guessing penalty,” a feature that deducted points for wrong answers.  
[Washington Post, SAT reclaims title most widely used college admission test](https://www.washingtonpost.com/education/2018/10/23/sat-reclaims-title-most-widely-used-college-admission-test/)

Our goal in this project, is to help the College Board find out how best to utilize their resource so as to further increase their market share in the college admission tests market.

Also keeping in mind the company mission of connecting students to college success and opportunity.

### Assumptions and Limitations
Assumptions: 
   - The participation rate of ACT and SAT when added up exceeds 100%. For instance, the participation rate for ACT and ACT in Alabama is 100% and 5% respectively, totalling up to 105%. Since the correlation between ACT participation and SAT participation is greatly inverse (r - -0.84), to draw meaningful conclusions, we will take the assumption that any number exceeding 100% shows students taking up both tests whilst anything below are students who only take up a either ACT or SAT. 
   - Participation rate can be elusive as it does not take into account actual number of students taking the test, A significant increase in the number of students taking SAT in a small populated state may not highly impact the overall SAT participant rate in the US. Work with only percentages without the context of its population amplifies the actual contributions of each state. We will use data we draw online to get a rough understanding of the student population in each state to draw meaningful conclusions.

### Contents:
- [2017 Data Import & Cleaning]
- [2018 Data Import and Cleaning]
- [Exploratory Data Analysis]
- [Data Visualization]
- [Descriptive and Inferential Statistics]
- [Outside Research]
- [Conclusions and Recommendations]

### Data Dictionary:

|Feature|Type|Dataset|Description|
|---|---|---|---|
|state|object|act_2017, act_2018_updated, combined_2017, final|the states in which the tests were taken| 
|year|object|combined_2017, final|the year in which the entry was taken | 
|act_participation|float|act_2017, act_2018_updated, combined_2017, final|Participation rates of ACT tests in| 
|sat_participation|float|act_2017, act_2018_updated, combined_2017, final|Participation rates of SAT tests in 2017| |act_english|float|ACT 2017|The average ACT test score on the English tests of students in the state| 
|act_math|float|act_2017, act_2018_updated, combined_2017, final|The average ACT test score on the Math test of students in the state|  
|act_reading|float|act_2017, act_2018_updated, combined_2017, final|The average ACT test score on the Reading test of students in the state|   
|act_science|float|act_2017, act_2018_updated, combined_2017, final|The average ACT test score on the Science test of students in the state| 
|act_composite|float|act_2017, act_2018_updated, combined_2017, final|The average ACT test score on the Composite test of students in the state| 
|sat_erw|integer|act_2017, act_2018_updated, combined_2017, final|The average SAT test score on the Evidence-Based Reading and Writing test of students in the state| 
|sat_math|integer|act_2017, act_2018_updated, combined_2017, final|The average SAT test score on the Math test of students in the state| 
|sat_total|integer|act_2017, act_2018_updated, combined_2017, final|The average SAT test score on the total (Math + ERW) tests of students in the state| 
|total_participation|float|final|Sum of ACT and SAT participation| 
