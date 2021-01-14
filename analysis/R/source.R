rm(list=ls())

#  RENV 
# if (!requireNamespace("remotes"))
#   install.packages("remotes")
# 
# remotes::install_github("rstudio/renv")
renv::restore()

source("analysis/R/config.R")
source("analysis/R/data.R")
source("analysis/R/analyses.R")
source("analysis/R/visualization.R", echo=TRUE)