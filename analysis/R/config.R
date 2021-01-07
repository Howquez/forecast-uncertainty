# Setup -----
# ** Packages -----
listOfPackages <- c("rmarkdown",
                    "knitr",
                    "glue",          # get some python-like string operations
                    "stringr",       # working with strings
                    "lubridate",     # working with dates
                    "plotly",        # interactive visualizations
                    "ggplot2",       # static visualizations for emails
                    "dplyr",         # select function
                    "magrittr",      # get %>% and %<>% opeartors
                    "DT",            #
                    "data.table",    #
                    # "roperators",  # get the += operator
                    "writexl",       # write xlsx files
                    "openxlsx",      # write xlsx files
                    "readxl")        # read xlsx files

newPackages <- listOfPackages[!(listOfPackages %in% installed.packages()[, "Package"])]

if(length(newPackages) > 0){
  install.packages(newPackages)
}

for(package in listOfPackages){
  require(package, character.only = TRUE)
}
