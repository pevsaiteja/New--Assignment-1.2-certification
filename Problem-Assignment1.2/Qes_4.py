my_list = ['Guru', 'Siya', 'Tiya', 'Guru', 'Daksh', 'Riya', 'Guru'] 
all_indexes = [] 
for i in range(0, len(my_list)) : 
    if my_list[i] == 'Guru' : 
        all_indexes.append(i)
print("Originallist ", my_list)
print("Indexes for element Guru : ", all_indexes)