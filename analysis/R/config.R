# Packages -----



# ** load -----
listOfPackages <- c("rmarkdown",
                    "knitr",
                    "distill",
                    "glue",          # get some python-like string operations
                    "stringr",       # working with strings
                    "lubridate",     # working with dates
                    "plotly",        # interactive visualizations
                    "highcharter",   # interactive visualizations
                    "ggplot2",       # static visualizations for emails
                    "dplyr",         # select function
                    "magrittr",      # get %>% and %<>% opeartors
                    "DT",            #
                    "data.table",    #
                    # "roperators",  # get the += operator
                    "writexl",       # write xlsx files
                    "openxlsx",      # write xlsx files
                    "readxl")        # read xlsx files

# newPackages <- listOfPackages[!(listOfPackages %in% installed.packages()[, "Package"])]
# 
# if(length(newPackages) > 0){
#   install.packages(newPackages)
# }

for(package in listOfPackages){
  require(package, character.only = TRUE)
}


# Hard coded variables -----
# ** temperatures -----
# temperatures & forecasts in Weiskirchen...
GER_TEMP <- 9
GER_BG   <- 12
GER_LB   <- 8
GER_UB   <- 14
# ...and in Illomantsi
FIN_TEMP <- 3
FIN_BG   <- 4
FIN_LB   <- 2
FIN_UB   <- 8


# ** design -----
style_primary <- "#FF0066"
style_secondary <- "#63FFC1"

