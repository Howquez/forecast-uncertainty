# Codebook


| Variable Name | Format | Description |
| --- | --- | --- |
| participant.label | String with 32 characters | used to identify respondents |
| location | string | Treatment variable that takes two values: `Ilomantsi` or `Weiskirchen`. The former is associated to a contradicting forecast. |
| forecast |string | Treatment variable that takes three values: `best_guess`, `interval` or `both`. Indicates the amount of information provided. |
| treated | boolean | Indicates the respondent's status with where pre-treatment is indicated by `FALSE`. |
| ASEP| numeric | Average Single-Event Probabilities |
| ACEP| numeric | Average Compound-Event Probabilities |
| AAI| numeric | Ambiguity Aversion Index (b)|
| AGII| numeric | Ambiguity-Generated Insensitivity (a-insensitivity) Index (a)|
||
| participant.payoff | numeric | The participant's earnings (including the 2 Euro showupfee). Either `12` or `2`.
| participant._index_in_pages | numeric | The latest page a respondent has seen. Ranging from `1` to `20`. |
| participant.time_started_utc | date | Timestamp created when respondent entered the survey. |
| session.code | string | Session identifier. The session comprising the vast majority of subjects is labeled as `t2ciiflg`. A second session was initiated to encounter balance issues. That session is labeled as `vg37et4c`. |
| Intro.1.wrong_answer_1 | numeric | Counts the number of times the first comprehension question was answered incorrectly. |
| Intro.1.wrong_answer_2 | numeric | Counts the number of times the second comprehension question was answered incorrectly. |
||
| Baillon.1.payoff | numeric | Documents if a 10 Euro bonus was earned in this particular round. |
| Baillon.1.review_weather | numeric | Counts the number of times a respondent has reviewed the weather information in this particular round. |
| Baillon.1.review_instructions | numeric | Counts the number of times a respondent has reviewed the instructions in this particular round. |
| Baillon.1.matching_probability | numeric | The respondents only input and our main variable to calculate Baillon et al.'s indices. |
| Baillon.1.event_decision | string | Identifies the events the respondents had to assess. Single events carry only one digit (e.g. `E2`) while compound events have two (e.g. `E13`). 
| Baillon.1.payment_mechanism | string | Indicates which mechanism (`bet` vs. `lottery`) led to the payoff in `Baillon.1.payoff` iff this particular round was randomly chosen to determine the final payoff.|
| Baillon.1.pivotal_lottery | numeric | If this round determines the final payoff, this variable determines the payment mechanism. If this variable is greater or equal to `Baillon.1.matching_probability`, the lottery is pivotal. |
| Baillon.1.pivotal_draw | numeric | If this round determines the final payoff and if the lottery is pivotal, this draw is used to determine the respondent's payoff. If smaller than Baillon.1.pivotal_lottery, the lottery is a success and the respondent earns 10 additional Euros. |
||
| Outro.1.Age | numeric | The respondent's self-reported age. |
| Outro.1.Gender | string | The respondent's self-reported gender. |
| Outro.1.Education | numeric | The respondent's self-reported highest educational degree: 0 = "Schule beendet ohne Abschluss", 1 = "Noch Schüler", 2 = "Volks-, Hauptschulabschluss, Quali ", 3 = "Mittlere Reife, Realschul- oder gleichwertiger Abschluss", 4 = "Abgeschlossene Lehre", 5 = "Fachabitur, Fachhochschulreife", 6 = "Abitur, Hochschulreife", 7 = "Fachhochschul-/Hochschulabschluss", 8 = "Anderer Abschluss" |
| Outro.1.Family | string | The respondent's self-reported marital status. |
| Outro.1.Kids | numeric | The respondent's self-reported number of children.|
| Outro.1.Income | numeric | The respondent's self-reported monthly budget: 99999 = `NA`, 0 = "0-500 €", 1 = "501-1.000 €", 2 = "1.001-2.000 €", 3 = "2.001-3.000 €", 4 = "3.001-4.000 €", 5 = "more than 4.000 €" |
| Outro.1.ZIP | string |  The respondent's self-reported ZIP code. |
| Outro.1.Vac | string | The respondent's self-reported vaccination status: "yes" = "I am vaccinated."], "no" = "I plan to get a vaccination but am not yet vaccinated.", "no interest" = "I don not want a vaccination.", "NA" = NA.
| Outro.1.Comprehension | string | The respondent's self-reported comprehension of the survey and the task at hand. |
| Outro.1.Usage | numeric | Respondent's usage of the weather forecasts: 5 = "several times a day", 4 = "on a daily basis", 3 = "several times a week", 2 = "on a weekly basis", 1 = "less than that", 0 = "never" |
| Outro.1.Temp | numeric | The respondent's location's temperature. |
| Outro.1.Accuracy | numeric | Respondent's assessment of message's accuracy. Ranging from `0` to `4`. The higher the value the more accurate the forecast. |
| Outro.1.Credibility | numeric | Respondent's assessment of message's credibility. Ranging from `0` to `4`. The higher the value the more credible the forecast. |
| Outro.1.CLICCS1 | long string | Answer to "What do you see as the biggest challenge with respect to a changing climate?" |
| Outro.1.CLICCS2 | long string | Answer to "How are youe dealing with it?" |
| Outro.1.Risk_General | numeric | Respondent's general risk self-assessment. Ranging from `0` to `10`. The higher the value the the more risk loving. |
| Outro.1.Risk_Weather | numeric | Respondent's weather related risk self-assessment. Ranging from `0` to `10`. The higher the value the the more risk loving. |