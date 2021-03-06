#This is just an appendix a from 
#R-intro by cran.r-project.org

#Generate two pseudo random normarl vectors of
#x and y-coordiates
x <- rnorm(50)
y <- rnorm(x)
print(x)
print(y)
plot(x,y)

#See which R object are now in the R workspace
ls()

#remove objects no longer needed. (Clean up)
rm(x,y)

#Generate a sequence x = {1, 2, 3, ... , 20}
x <- 1:20
w <- 1 + sqrt(x)/2  #A 'weight' vector of standard deviations
print(x)
print(w)

dummy <- data.frame(x=x, y= x + rnorm(x)*w)
print(dummy) #Make a data frame of two columns, x and y
fm <- lm(y~x, data=dummy) #lm stand for linear models

#Fit a simple linear regression and look at the analysis.
#With y to the left of the tilde, we are modelling y dependent on x
print(summary(fm))

#Sice we know the standard deviations, we can do a weighted regression
fm1 <- lm(y~x, data=dummy, weight=1/w^2)
print(summary(fm1))

#Make the columns in the data frame visible as variables
print(attach(dummy))

lrf <- lowess(x, y) #Make a nonparametric local regression function
plot(x,y,pch='+')
print(lrf)
lines(x, lrf$y, col='blue') #Add in the local regression
abline(0, 1, lty=3) #The true regression line (intercept 0, slope 1)
abline(coef(fm1), col='red')
detach() #Remove data frame from the search path

#A standard regression diagnostic plot to check for heteroscedasticity
plot(
	fitted(fm), resid(fm),
	xlab='Fitted values', ylab='Residuals',
	main='Residuals vs Fitted'
)

#A normal scores plot to check for skewness, kurtosis
#and outliers
qqnorm(resid(fm), main='Residuals Rankit Plot')
rm(fm, fm1, lrf, x, dummy) #Cleaning up
