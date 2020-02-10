#import package shiny
library(shiny)

# Code for create the ui
ui <- fluidPage(
    #Code here
    titlePanel("My Shiny Apps"),
    
    sidebarLayout(
        sidebarPanel(
            h2("Installation"),
            p("Shiny is available on CRAN, so you can install it in the usual way from your console:"),
            p("install.packages(\"shiny\")", style="color:red"),
            "Shiny is a product of",
            span(),
            p("RStudio", style="color:blue")
            ),
        mainPanel(
            h1("Introducing Shiny"),
            p("Shiny is a new package from RStudio that makes it incredibily easy to build interactive web application with R."),
            br(),
            p("For an introduction and live examples, visit the shiny homepage")
        )
    )
)

#Put your server logic here
server <- function(input, output) {
    #Code here
}

#Run the app
shinyApp(ui=ui, server=server)