library(ggplot2)
library(plotly)

datum <- c(
	3.79, 2.99, 2.77, 2.91, 3.10, 1.84, 2.52, 3.22,
	2.45, 2.14, 2.67, 2.52, 2.71, 2.75, 3.57, 3.85,
	3.36, 2.05, 2.89, 2.83, 3.13, 2.44, 2.10, 3.71,
	3.14, 3.54, 2.37, 2.68, 3.51, 3.37
)

data <- data.frame(Staff_Salaries = datum)
print(head(data))

print(datum)
paste("length of datum : ", length(datum))
summary(data)
paste("std of data : ", sqrt(var(datum)))
print("stem and leaf")
stem(datum)
hist(datum, n = 10, col = 'dark cyan', main = "staff_salaries in US in the early 1970s")
boxplot(datum, col = "blue")

#visualization using ggplot2
ggplot(data = data, mapping = aes(x = c(1:30), y = data$Staff_Salaries)) + geom_point()

#visualization using plotly
p <- plot_ly(data = data, x = ~c(1:30), y = ~data$Staff_Salaries, color = ~data$Staff_Salaries, size = ~data$Staff_Salaries)
p

steam_leaf_plot <- plot_ly(y = ~data$Staff_Salaries, type = "box", boxpoints = "all")
steam_leaf_plot
