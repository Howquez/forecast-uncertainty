# identify most recent file
allFiles <- file.info(list.files(path = "data/raw",
                               full.names = TRUE,
                               pattern = ".xlsx$"),
                    extra_cols = FALSE)
recentFile <- allFiles[allFiles$mtime == max(allFiles$mtime), ] %>% row.names()

# read data -----
dt <- read_excel(recentFile) %>% data.table()


# for the time being, ignore the last 11 lines and load the simulated data
dt <- read.csv(file="data/simulation/all_apps_wide.csv",
               stringsAsFactors = FALSE) %>% data.table()

# select relevant columns for main- and control variables separately
mainRegex <- "^participant\\.code$|_index_in_pages|Location$|Information$|matching_probability$|event_decision$|lower_bound$|best_guess$|upper_bound$|Accuracy$|Authenticity$|Credibility$|Comprehension$"
mainVariables <- str_subset(string = names(dt),
                            pattern = mainRegex)
mt <- dt[, ..mainVariables] #"mt" for Main Table (in contrast to "Control Table" oder "Data Table")

controlRegex <- "^participant\\.code$|time_started$|visited$|participant\\.payoff$|^Baillon.1.player.window.*|^Baillon.1.player.browser$|review_|Age$|Gender$|Education$|Income$|Usage$"
controlVariables <- str_subset(string = names(dt),
                               pattern = controlRegex)
ct <- dt[, ..controlVariables]

# rename cols
names(mt) %<>% str_replace_all(pattern = "\\.player", replacement = "")
names(ct) %<>% str_replace_all(pattern = "\\.player", replacement = "")

# manipulate data -----
#..declare single and composite events
for(app in c("Baillon", "postBaillon")){
  for(round in 1:6){
    
    col = glue("{app}.{round}.event_decision")
    
    set(x = mt,
        i = which(mt[[col]] %>% as.character() %>% nchar() > 2),
        j = col,
        value = "composite")
    
    set(x = mt,
        i = which(mt[[col]] %>% as.character() %>% nchar() == 2),
        j = col,
        value = "single")
  }
}

#..calculate Baillons Indices
for(row in 1:NROW(mt)){
  
  for(app in c("Baillon", "postBaillon")){
    #..first get a vector of event types
    vector = c()
    for(round in 1:6){
      col = glue("{app}.{round}.event_decision")
      vector = append(vector, mt[row, get(col)])
    }
    
    # consider composite events first and get the round numbers where composite events were shown
    cEvents = str_which(string = vector,
                         pattern = "composite")
    # now loop over these rounds to add the respective matching_probabilities
    CEPs = NULL # Compound-Event Probabilities
    for(compositeRound in cEvents){
      col <- glue("{app}.{compositeRound}.matching_probability")
      increment <- mt[row, get(col)]
      CEPs <- append(CEPs, increment)
    }
    # average
    ACEP = mean(CEPs, na.rm=TRUE)/100
    
    # do the same for single events
    sEvents <- str_which(string = vector,
                         pattern = "single")
    SEPs = NULL
    for(singleRound in sEvents){
      col <- glue("{app}.{singleRound}.matching_probability")
      increment <- mt[row, get(col)]
      SEPs <- append(SEPs, increment)
    }
    ASEP = mean(SEPs, na.rm=TRUE)/100
    
    # calculate Ambiguity Aversion Index (AAI)
    AAI = 1 - ACEP - ASEP
    
    # calculate  ambiguity-generated insensitivity (a-insensitivity) index (AGII)
    AGII = 3 * (1/3 - (ACEP - ASEP))
    
    # write indices into the table
    if(app == "postBaillon"){
      mt[row, `:=` (post_AAI=AAI)]
      mt[row, `:=` (post_AGII=AGII)]
    }else{
      mt[row, `:=` (prior_AAI=AAI)]
      mt[row, `:=` (prior_AGII=AGII)]
    }
  }
}

# declare the information resulting from treatment
FC_LB <- ifelse(test = mt$initialize.1.Location == "Weiskirchen",
                yes  = GER_LB,
                no   = FIN_LB)
FC_BG <- ifelse(test = mt$initialize.1.Location == "Weiskirchen",
                yes  = GER_BG,
                no   = FIN_BG)
FC_UB <- ifelse(test = mt$initialize.1.Location == "Weiskirchen",
                yes  = GER_UB,
                no   = FIN_UB)
FC_TEMP <- ifelse(test = mt$initialize.1.Location == "Weiskirchen",
                  yes  = GER_TEMP,
                  no   = FIN_TEMP)

# store data -----
# write new data table with the variables of most interest...
main <- mt[terminate.1.Comprehension != "no", 
           .(participant.code,
             location = initialize.1.Location,
             information = initialize.1.Information,
             # variables from round 1
             # temperature guesses (LB, BG, UB) are normalized by the forecasts
             prior_LB = MPP.1.lower_bound - FC_LB, 
             prior_BG = MPP.1.best_guess - FC_BG,
             prior_UB = MPP.1.upper_bound - FC_UB,
             prior_width = MPP.1.lower_bound - MPP.1.upper_bound,
             prior_AAI,
             prior_AGII,
             # variables from round 2
             # temperature guesses (LB, BG, UB) are normalized by the forecasts
             post_LB = postMPP.1.lower_bound - FC_LB,
             post_BG = postMPP.1.best_guess - FC_BG,
             post_UB = postMPP.1.upper_bound - FC_UB,
             post_width = postMPP.1.lower_bound - postMPP.1.upper_bound,
             post_AAI,
             post_AGII,
             # differences between both rounds
             diff_BG = postMPP.1.best_guess - MPP.1.best_guess,
             diff_width = (MPP.1.lower_bound - MPP.1.upper_bound) - (postMPP.1.lower_bound - postMPP.1.upper_bound), # prior_width - post_width,
             diff_AAI = prior_AAI - post_AAI,
             diff_AGII = prior_AGII - post_AGII,
             # stated variables
             stated_accuracy = terminate.1.Accuracy,
             stated_authenticity = terminate.1.Authenticity,
             stated_credibility = terminate.1.Credibility)]

# .. into a csv file
write.csv(x = main,
          file = "data/processed/main_variables.csv")

# similar for control variables
control <- ct[participant.time_started %>% is.na() == FALSE]
write.csv(x = control,
          file = "data/processed/control_variables.csv")

# tidy up -----
keep <- str_subset(string = ls(),
                   pattern = "^[[:upper:]]*_[[:upper:]]*$|^control$|^main$|^style_")
rm(list = ls()[!(ls() %in% keep)])
