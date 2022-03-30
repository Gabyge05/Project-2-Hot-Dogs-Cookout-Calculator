#Hot Dog Cookout.project

number_of_people = int(input('Enter the number of people attending:'))
number_of_hotdogs_per_person = int(input('Enter the number of hotdogs given per person:'))

amount_of_hotdogs_per_package = 10
amount_of_buns_per_package = 8

total_amount_of_hotdogs = number_of_people * number_of_hotdogs_per_person

amount_of_hotdogs_packages_required = total_amount_of_hotdogs //amount_of_hotdogs_per_package
amount_of_buns_packages_required = total_amount_of_hotdogs // amount_of_buns_per_package
amount_of_hotdogs_leftover = total_amount_of_hotdogs % amount_of_hotdogs_per_package
amount_of_buns_leftover = total_amount_of_hotdogs % amount_of_buns_per_package

print('The minimum number of packages of hot dogs required is :', amount_of_hotdogs_packages_required)
print('The minimum number of packages of buns required is :',amount_of_buns_packages_required)
print('The number of hot dogs that will be leftover is :',amount_of_hotdogs_leftover)
print('The number of hot dogs buns that will be leftover is :',amount_of_buns_leftover)

