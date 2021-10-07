# We strongly recommend you to read the docs which you can find here:
# https://github.com/Howquez/forecast-uncertainty/wiki

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

# create_article("reports/data.Rmd")

# install.packages("gridExtra")


rmarkdown::render(input = "admin/HAURO_Ablaufplan.Rmd",
                  output_format = "all")