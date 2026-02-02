import newapp

# adding the new one record ti the database 
# newapp.add_one('Trisha', 'Sarkar', 'trishasarkar@gmail.com')
# deleting the data from the table
# newapp.delete_one(1)
# # adding many records to the table
# many_customers = [
#     ('Sovan', 'Das', 'sovan.das@gmail.com'),
#     ('Rahul', 'Ghosh', 'rahul.ghosh@gmail.com'),
#     ('Priya', 'Mukherjee', 'priya.mukherjee@gmail.com')
# ]
newapp.email_lookup('trishasarkar@gmail.com')
# newapp.add_many(many_customers)
# newapp.show_all()