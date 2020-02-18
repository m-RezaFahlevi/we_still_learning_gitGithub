library(shiny)

ui <- fluidPage(
	titlePanel("Bidoof here"),
	sidebarLayout(
		sidebarPanel(
			p("learning some r-widget"),

			textInput(
				"text",
				h3("text_input"),
				value = "Enter your text"
			),

			numericInput(
				"num",
				h3("Numeric input"),
				value = 1
			),

			sliderInput(
				"range",
				label = "Range of interest : ",
				min = 0, max = 100, value = c(0,100)
			),
		),

		mainPanel(
			h1("learning a widget"),
			textOutput("input_text"),
			textOutput("input_numeric"),
			textOutput("selected_var")
		)
	),	
)

server <- function(input, output) {
	output$input_text <- renderText({
		paste("Output : ", input$text) 
	})

	output$input_numeric <- renderText({
		paste("Output : ", input$num)
	})

	output$selected_var <- renderText({
		paste("you have selected from", input$range[1], " to ", input$range[2])
	})
}

shinyApp(ui=ui, server=server)
