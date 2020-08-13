# booking

In the begining you import your files with the list of all students of the school and the list of people who already paid from the bank statement, both as csv files. You also create a file, which notes all the mistakes that were made by people who paid, with the sturucture of the input files. 
 
(It also creates a row in the list of all students, that wasnt there before)

Next, the code creates the variable for the Students ID, with the format of one s and four numbers. 

Next, it searches the list of people who have paid for all of the student IDs and assigns them to the students. 

After that if everything went normal up to that point, the respective student will be marked in the list of students, so you can easily check, if that student has already paid together with the amount, that has been paid. As well as the date on wich the payment happened.

Finally, if no or multiple student IDs have been submitted, if the person had paid or if the wrong student ID has been submitted, these errors, with the respective error message are noted in a seperate file.

The final lines convert the files, wich have been created during the progress to csv
