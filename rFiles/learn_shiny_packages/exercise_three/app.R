library(shiny)

ui <- fluidPage(
    titlePanel(h1(size=12,"censusVis")),
    
    sidebarLayout(
        sidebarPanel(
            p("Create demographic maps with information form the 2010 US Census."),
            
            selectInput(
                "select", 
                strong("Choose variable to display"),
                choices = list(
                    "st_variable" = 1, 
                    "second_variable" = 2, 
                    "third_variable" = 3, 
                    "fourth_variable" = 4, 
                    "fifth_variable" = 5
                    )
            ),
            
            sliderInput(
                "range_of_interest", 
                strong("Range of interest:"), 
                min = 0, max = 100, value = c(5,95)
            ),
            
            selectInput(
                "variable_choosing",
                strong("Choose variable to display"),
                choices = list(
                    "Percent White" = 1,
                    "Percent Black" = 2,
                    "Percent Hispanic" = 3,
                    "Percent Asian" = 4
                    )
            )
        ),
        
        mainPanel(
            h1("Shiny exercise"),
            textOutput("selected_var"),
            textOutput("nd_selected_var"),
            textOutput("the_slider")
        )
    )
)

server <- function(input, output) {
    #import the library
    library(maps)
    library(mapproj)
    
    source("helpers.R")
    counties <- readRDS("counties.rds")
    
    #output for counties.rds
    output$map <- renderPlot({
        
    })
    
    #code here
    output$selected_var <- renderText({
        paste("You have selected", input$select)
    })
    
    output$nd_selected_var <- renderText({
        paste("You have selected", input$variable_choosing)
    })
    
    output$the_slider <- renderText({
        paste("you have choosen a range from ",input$range_of_interest[1], " to ", input$range_of_interest[2])
    })
}

#Running the app
shinyApp(ui=ui, server = server)