#create a vector

st_vector <- c(2,4,1)
nd_vector <- c(2,2,4,2)

#indexing of vector
print(st_vector[c(1,2)]) #display only index 1 and 2
print(nd_vector[-c(1,2)]) #exclude index 1 and 2

fruit <- c('Anggur', 'nanas', 'jeruk')
print(fruit)
print(mode(fruit))
print(typeof(fruit))

thrd_vector <- c(-2, -4, 10, 2)
print(which(thrd_vector > 0))  #return as the index
print(length(thrd_vector))

#List data type
print("The list")
names <- c("Andi", "Budi", "Bidoof")
fruit <- c("Anggur", "Apple", "Banana")
ages <- c(1, 2, 4)

my_data <- list(names, fruit, ages)
print(my_data)

#Given names of each list
names(my_data) <- c('Names', 'Fruits', 'Ages')

print(my_data)

#Data frame
print("data frames")
names <- c("Andi", "Budi", "Rini")
age <- c(22, 23, 24)
my_data <- data.frame(names, age)
print(my_data[,c(1)])