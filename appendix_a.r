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

