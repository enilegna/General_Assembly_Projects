# Project 1: SAT & ACT Analysis


## Problem Statement
The College Board SATs was the first standardized test created for college admission tests in the United States. 40 years later in 1959, with the introduction of the ACT as a standardized college admission test and increase in the umber of schools accepting both the ACT and SAT, the number of students participating in SATs gradually decreased.  
*[The Olive Book, Do Ivy League Schools Prefer the SAT?](https://theolivebook.com/do-colleges-prefer-the-sat-or-the-act/)*

In 2016, the College Board decided to launch a new version of the SAT with the following updates: less of the tricky vocabulary that was long a hallmark of the test. The new version also dropped the “guessing penalty,” a feature that deducted points for wrong answers.  
[Washington Post, SAT reclaims title most widely used college admission test](https://www.washingtonpost.com/education/2018/10/23/sat-reclaims-title-most-widely-used-college-admission-test/)

Our goal in this project, is to help the College Board find out how best to utilize their resource so as to further increase their market share in the college admission tests market.

Also keeping in mind the company mission of connecting students to college success and opportunity. 

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
|state|object|ACT 2017|the states in which the tests were taken| 
|state|object|SAT 2017|the states in which the tests were taken| 
|act_participation|float|ACT 2017|Participation rates of ACT tests in 2017| |sat_participation|float|SAT 2017|Participation rates of SAT tests in 2017| |act_english|float|ACT 2017|The average ACT test score on the English tests of students in the state| 
|act_math|float|ACT 2017|The average ACT test score on the Math test of students in the state|  
|act_reading|float|ACT 2017|The average ACT test score on the Reading test of students in the state|   
|act_science|float|ACT 2017|The average ACT test score on the Science test of students in the state| 
|act_composite|float|ACT 2017|The average ACT test score on the Composite test of students in the state| 
|sat_erw|integer|SAT 2017|The average SAT test score on the Evidence-Based Reading and Writing test of students in the state| 
|sat_math|integer|SAT 2017|The average SAT test score on the Math test of students in the state| 
|sat_total|integer|ACT 2017|The average SAT test score on the total (Math + ERW) tests of students in the state| 