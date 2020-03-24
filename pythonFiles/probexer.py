letters = "STATISTICS"
print(letters.split("ST"))
print("\n")

#Create a function factorial, permutation, and combination
def _factorial_(number):
    if (number == 0): return 1
    else: number = number*_factorial_(int(number-1))
    
    return number

def _permutation_(number, r_taken):
    if (number - r_taken == 0): return None
    else:
        return _factorial_(number)/_factorial_(number - r_taken)

def _permutation_improved_(number, r_object):
    if (number - len(r_object) == 0): return None
    else:
        temp = 1
        for items in r_object:
            temp = temp*_factorial_(items)

        return _factorial_(number)/temp

def _combination_(number, r_taken):
    return (1/_factorial_(r_taken))*_permutation_(number, r_taken)

print(_factorial_(10))
print(_permutation_(6, 3))


the_items = [3,2,2]
print(_permutation_improved_(sum(the_items), the_items))

blood_type = ["AB+", "AB-", "A+", "A-", "B+", "B-", "O+", "O-"]
blood_pressure = ["low", "normal", "high"]
print(blood_type, end = "\nlength of list : {}\n".format(len(blood_type)))
print(blood_pressure, end = "\nlength of list: {}\n".format(len(blood_pressure)))
print("\nThe number of passien can be classified : \n")

print(8*3)
print("Brute force way")
pasien = []
[[pasien.append([i,j]) for j in blood_pressure] for i in blood_type]
print([i for i in pasien])
print(len(pasien))

dice = [1, 2, 3, 4, 5, 6]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(dice)
print(alphabet)
print(6*26)
print("brute force way")
sample = []
[[sample.append([i,j]) for j in alphabet] for i in dice]
print(sample, end = "\n length of list : {}\n".format(len(sample)))

students = ["freshman", "sophomores", "juniors", "seniors"]
gender = ["male", "female"]
print(4*2)
print("brute force way")
student = []
[[student.append([i,j]) for j in gender] for i in students]
print(student, end = "\nlength of list : {}\n".format(len(student)))

"""
A certain she comes in 5 different styles with each style available in 4 disctinct colors.
"""
styles = ["s1", "s2", "s3", "s4", "s5"]
colors = ["c1", "c2", "c3", "c4"]
print(5*4)
print("brute force way")
style = []
[[style.append([i,j]) for j in colors] for i in styles]
print(style, end = "\nlength of list : {}\n".format(len(style)))

"""
7 simple health rules:
no smoking, 
regular exercise, 
use alohol moderately, 
get 7 to 8 hoiurs of sleep, 
maintain proper weight,
eat breakfast, 
and do not eat between meals.

In how many ways can a person adopt five of these rules to follow
"""
print(f"When the person violet all 7 rules : {_combination_(7,5)}")
print(f"When the person never drinks and always eats breakfast : {_combination_(5,3)}")

"""
4 designs, 3 different heating system, a garage or carport, and a patio or screened porch.
How many different plans are available to this buyer.

Available slot = [design, heating_system, option1, option2]
"""
print(4*3*2*2)
print()

the_condition = [7,3,5,2]
print(_permutation_improved_(sum(the_condition), the_condition))
