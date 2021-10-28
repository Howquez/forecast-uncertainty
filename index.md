# 🌦 (In)credible Forecasts?

Uncertainty is an inherent quality of forecasts. Yet, many forecasts are communicated as point estimates. 
One may fear that communication of uncertainty, for instance, via confidence intervals, signals some sort of 
incompetency or dispute in the community. In addition, it may simply be too complicated to convey to laypersons.

However, not-acknowledging uncertainty results in forecasts that may seem too precise and therefore incredible. 
Because of this potentially ambiguous and conflicting signals, we want to investigate the acknowledgement of uncertainty.
Doing so, we created an experiment and recruited more than 1.700 participants. This repository contains the experiment's
software, the analysis plans used to evaluate the data as well as some documentation.

___

## 🧐 What the project is about
This repository is the foundation of an economic experiment that exposes respondents to (real) forecasts and manipulates 
the forecasts' communication strategies between subjects. We elicit the respondents' 
ambiguity attitudes before and after exposure to assess forecasts' credibility and its effect on ambiguity attitudes.
The ambiguity attitudes are elicited using Baillon et al.'s [(2018, Econometrica)]( https://doi.org/10.3982/ECTA14370) 
method. 

In these tasks, respondents shall choose winning probabilities of a lottery such that they are indifferent between that 
particular lottery and a bet on temperature outcomes of some location at some time. They do neither know the corresponding 
location nor the exact timing such that they cannot cheat. All they know are historic temperatures measured in the past.

Based on these information, respondents have to choose winning probabilities for six bets that differ with respect to
the temperatures that promise a price if they occur. Subsequently, respondents are exposed to the weather forecast 
(which we manipulate in a between subject design) and have to reconfigure the winning probabilities of the exact same 
six bets once more.

Having a report of historic temperatures measured, we assume respondents to form some prior belief about the future temperature
outcome. Because we want some forecasts to be surprising, we chose the locations and timings the weather data (and 
forecasts) correspond to such that half of the forecasts to match the reported weather trend and half of the forecasts
to be way off (that is, where the prior belief is relatively far away from the weather forecast).

This is why we end uo with 2x3 treatments where forecasts are either surprising or not and where forecasts are either
communicated as a best guess, as an confidence intervall or as a best guess with a confidence intervall.

Read how to access a demo below to get a better and more vivid understanding of the experiment.



## 🚏 How you can access a demo
You can find the experiment's demo [here](https://forecastsurvey.herokuapp.com/demo/). A click on the app will create a 
session and redirect you to a page containing several URLs. Click on the _Session-wide link_ to open the experiment. 
After reading through the instructions (🇩🇪) , you should end up seeing a decision screen looking like this one:

[![Gif displaying the process](figures/Baillon_Decision_Screen.gif)](https://forecastsurvey.herokuapp.com/demo/)


## 📊 How we analyzed the data 
The analysis plan will be pre-registered, which means that we declare what we are analyzing and how we are analyzing it 
before gathering (and thus, seeing) the data. You can find a preliminary report that prepares the data 
[here](https://github.com/Howquez/forecast-uncertainty/blob/Baillon/reports/data.html) (download the html file and open 
it with your browser).
