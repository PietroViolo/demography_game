#---------------------------------------------------------------------------#
# Nom : demography_game.R                                  			            #
# Description : Faire un jeu de démographie pour les portes ouvertes        #
# Auteur : Pietro Violo                                                     #
# Date : Jan 22 2023                                                        #
# Modifications :                                                           #
#---------------------------------------------------------------------------#

options(scipen=999)

#---------------------------------------------------------------------------#
# Library and data                                                          #
#---------------------------------------------------------------------------#
library(tidyverse)
library(shiny)
library(gapminder)
library(shinyjs)
library(countrycode)
library(plotly)

countries <- read.csv('./Data/demogle_data.csv') %>% 
  rename(Population_size = Population)

#---------------------------------------------------------------------------#
#  Make interactive bubble chart                                            #
#---------------------------------------------------------------------------#

ui <- fluidPage(
  plotlyOutput("bubble_chart"),
  selectInput("x_var", "X-axis variable:", names(countries), selected = "Migration"),
  selectInput("y_var", "Y-axis variable:", names(countries), selected = "Female.E0"),
  selectInput("size_var", "Size variable:", names(countries), selected = "Population_size"),
  selectInput("color_var", "Color variable:", names(countries), selected = "Country"),
  textInput("search_bar", "Search for a country:"),
  actionButton("search", "Search")
)

server <- function(input, output) {
  
  filtered_data <- reactive({
    if(input$search_bar == "") return(countries)
    countries %>% 
      filter(Country == input$search_bar)
  })
  
  output$bubble_chart <- renderPlotly({
    plot_ly(data = filtered_data(), x = ~get(input$x_var), y = ~get(input$y_var),
            size = ~get(input$size_var), color = ~get(input$color_var),
            type = "scatter", mode = "markers", 
            marker = list(sizemode = "diameter", 
                          text = ~Country)) %>%
      layout(hoverlabel = list(namelength = -1, bgcolor = "white", font = list(family = "Arial", size = 14, color = "black")))
  })
}

shinyApp(ui = ui, server = server)





#---------------------------------------------------------------------------#
#  Make the game through shiny                                              #
#---------------------------------------------------------------------------#
