# 🌦 What makes a (weather) forecast credible?
[![Generic badge](https://img.shields.io/badge/Status:-WIP-yellow.svg)](https://shields.io/)
Made with [oTree](https://www.sciencedirect.com/science/article/pii/S2214635016000101) and ❤️

## 🎓 What the project is about
This project is the foundation of an economic experiment that exposes respondents to forecasts and manipulates the 
forecasts' communication strategies between subjects. We elicit the respondents' belief distribution (MPP) and 
ambiguity attitudes (Baillon) before and after exposure to assess forecasts' credibility.

We retrieve the belief distributions using Eyting & Schmidt's 
[(2020, Working Paper)](https://download.uni-mainz.de/RePEc/pdf/Discussion_Paper_1818.pdf)
Multiple Point Predictions (MPP) which is implemented in a binarized fashion using Hossain & Okui's 
[(2013, Review of Economic Studies)](https://www.jstor.org/stable/43551453) 
binarized scoring rule. The ambiguity attitudes are elicited using Baillon et al.'s [(2018, Econometrica)]( https://doi.org/10.3982/ECTA14370) 
Method. 


## 🚏 How you can access a demo
You can find the experiment's demo [here](https://forecastsurvey.herokuapp.com/demo/). The link allows you to open 
three apps
- `Baillon_MPP`,
- `MPP_Standalone`,
- `Baillon_Standalone`.

The two standalone apps are slices of the `Baillon_MPP` app which were created to save time if one is solely interested in one
of the implementations. To get the better user experience, I recommend to click through the complete (i.e. the 
Baillon_MPP) app.

A click on one of the apps will create a session and redirect you to a page containing lots of URLs. Click on the
_Session-wide link_ to open the experiment. After reading through the instructions, you should end up seeing a decision 
screen looking like this one:

[![](figures/Baillon_Decision_Screen.png)](https://forecastsurvey.herokuapp.com/demo/)

## 🧐 How we analyzed it 
The analysis plan will be pre-registered, which means that we declare what we are analyzing and how we are analyzing it 
before seeing the data.

### 📖 Read the docs
I am creating a wiki [over here](https://github.com/Howquez/forecast-uncertainty/wiki). It will contain more detailed 
information needed to understand the resulting data and to replicate the analysis.

## 🛠 How we built it

### Tech stack
The experiment itself is based on [oTree](https://www.sciencedirect.com/science/article/pii/S2214635016000101), 
a Python module designed to build surveys and experiments. It utilizes 
Python, JavaScript, HTML & CSS (mostly bootstrap 4.1.x). The corresponding analysis is done with R.

### App Sequence
The experiment first elicits uncertainty attitudes, then beliefs. Afterwards, an information treatment is 
provided. Subsequently, uncertainty attitudes and beliefs are elicited once more. The experiment closes with
a payoff calculation, a short questionnaire and  the payoff revelation. Because the apps (Baillon and MPP) are played 
twice, the structure of this experiment is a little unusual because it cannot solely rely on rounds but also utilizes 
clones of these apps.

As a consequence, the experiment is based on the following app sequence: 

[[initialize](initialize), [Baillon](Baillon), [MPP](MPP), [postBaillon](postBaillon), [postMPP](postMPP), 
[terminate](terminate)]

where _initialize_ is an app that initially writes some variables into the participant scope that are 
retrieved later on. Similarly, _terminate_ is an app that closes the survey by providing information stored
in the participant.vars. The reason I built these apps was to decouple the other apps easily, if needed.

### Page Sequence 
I haven't been working on the BSR app recently. For this reason I will explain the Baillon+MPP survey in what follows.
The templates, i.e. the pages the respondents see, are displayed in the following order:

| Template                                                                                | Rounds | App         |
|-----------------------------------------------------------------------------------------|--------|-------------|
| [Intro_Welcome](oTree/initialize/templates/initialize/Intro_Welcome.html)               | 1      | initialize  |
| [Intro_Instructions](oTree/initialize/templates/initialize/Intro_Instructions.html)     | 1      | initialize  |
| [Baillon_Instructions](oTree/Baillon/templates/Baillon/Baillon_Instructions.html)       | 1      | Baillon     |
| [Baillon_Confirmation](oTree/Baillon/templates/Baillon/Baillon_Confirmation.html)       | 1      | Baillon     |
| [Baillon_Decision](oTree/Baillon/templates/Baillon/Baillon_Decision.html)               | 6      | Baillon     |
| [Baillon_Direct](oTree/Baillon/templates/Baillon/Baillon_Direct.html)                   | 1      | Baillon     |
| [MPP_Instructions](oTree/MPP/templates/MPP/MPP_Instructions.html)                       | 1      | MPP         |
| [MPP_Confirmation](oTree/MPP/templates/MPP/MPP_Confirmation.html)                       | 1      | MPP         |
| [MPP_Decision](oTree/MPP/templates/MPP/MPP_Decision.html)                               | 1      | MPP         |
| [MPP_Direct](oTree/MPP/templates/MPP/MPP_Direct.html)                                   | 1      | MPP         |
| [Baillon_Decision](oTree/Baillon/templates/Baillon/Baillon_Decision.html)               | 6      | postBaillon |
| [Baillon_Direct](oTree/Baillon/templates/Baillon/Baillon_Direct.html)                   | 1      | postBaillon |
| [MPP_Decision](oTree/MPP/templates/MPP/MPP_Decision.html)                               | 1      | postMPP     |
| [MPP_Direct](oTree/MPP/templates/MPP/MPP_Direct.html)                                   | 1      | postMPP     |
| [Domain_Questions_1](oTree/terminate/templates/terminate/Domain_Questions_1.html)       | 1      | terminate   |
| [Domain_Questions_2](oTree/terminate/templates/terminate/Domain_Questions_2.html)       | 1      | terminate   |
| [CLICCS_Questions](oTree/terminate/templates/terminate/CLICCS_Questions.html)           | 1      | terminate   |
| [Demographic_Questions](oTree/terminate/templates/terminate/Demographic_Questions.html) | 1      | terminate   |
| [Results](oTree/terminate/templates/terminate/Results.html)                             | 1      | terminate   |

These templates utilize variables attached to the models (player, group, subsession, participant,...) as well as
variables passed to the template via `vars_for_template` method or variables passed to the js files via `js_vars` method
(both is done within the respective pages.py files). These variables are then used as arguments in 
[twig(?)](https://twig.symfony.com/doc/2.x/intro.html) logic such as if statements and loops in the templates.

## To do
[Here](https://github.com/Howquez/forecast-uncertainty/projects/1) is the corresponding kanban board.



