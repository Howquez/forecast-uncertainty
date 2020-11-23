You can find the experiment's demo [here](https://forecastsurvey.herokuapp.com/demo/). 

# Structure
### Overview
This oTree experiment consists of two elements: 
- An elicitation of the respondents' ambiguity attitudes 
(using Baillon et al.'s [(2018, Econometrica)]( https://doi.org/10.3982/ECTA14370)  Method)
- An elicitation of the respondent's beliefs

The belief elicitation is either done using a quadratic scoring rule (BSR) for distributions or Eyting & Schmidt's 
[(2020, Working Paper)](https://download.uni-mainz.de/RePEc/pdf/Discussion_Paper_1818.pdf)
Multiple Point Predictions (MPP). Both are implemented in a binarized fashion using Hossain & Okui's 
[(2013, Review of Economic Studies)](https://www.jstor.org/stable/43551453) 
binarized scoring rule.

### App Sequence
As a consequence, there are two different groups of apps. One relying on Baillon+BSR and another one relying on 
Baillon+MPP.

The survey first elicits uncertainty attitudes, then beliefs. Afterwards an information treatment is 
provided. Subsequently, uncertainty attitudes and beliefs are elicited once more. The survey closes with
a payoff calculation and revelation. Because the apps (Baillon, BSR or MPP) are played twice, the structure of this 
survey is a little unusual because it cannot solely rely on rounds but also utilizes clones of these apps.

As a consequence, the survey is based on one of the following app sequences: 
- [[initialize](initialize), [Baillon](Baillon), [MPP](MPP), [postBaillon](postBaillon), [postMPP](postMPP)]
- [initialize, Baillon, [BSR](BSR), postBaillon, [postBSR](postBSR)]

where _initialize_ is an app that initially writes some variables into the participant scope that are 
retrieved later on.

### Page Sequence
I haven't been working on the BSR app recently. For this reason I will explain the Baillon+MPP survey in what follows.
The templates, i.e. the pages the respondents see, are displayed in the following order:
1. [Intro_Welcome](initialize/templates/initialize/Intro_Welcome.html)
2. [Intro_Instructions](initialize/templates/initialize/Intro_Instructions.html)
3. [Baillon_Instructions](Baillon/templates/Baillon/Baillon_Instructions.html)
4. [Baillon_Decision](Baillon/templates/Baillon/Baillon_Instructions.html) (6 rounds)
5. [MPP_Instructions](MPP/templates/MPP/MPP_Instructions.html)
6. [MPP_Decision](MPP/templates/MPP/MPP_Decision.html)
7. [Forecast_Viz](Baillon/templates/Baillon/Forecast_Viz.html)
8. [Baillon_Decision](Baillon/templates/Baillon/Baillon_Decision.html) (6 rounds)
9. [MPP_Decision](MPP/templates/MPP/MPP_Decision.html)
10. [MPP_Revelation](MPP/templates/MPP/MPP_Revelation.html)


