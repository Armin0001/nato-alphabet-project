student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas

# f = open("nato_phonetic_alphabet.csv")
# data = f.readlines()
#
# # print(data)
#
# my_dict = {x for x in data}
# print(my_dict)


# letters = [x for x in data]

# my_dict = {key:value for (key, value) in data}
# print(my_dict)






#Loop through rows of a data frame

    #Access index and row
    #Access row.student or row.score
# student_data_frame = pandas.DataFrame(student_dict)


# for (index, row) in data_frame.iterrows():
# 	print(row)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

df = pandas.read_csv (r'nato_phonetic_alphabet.csv')


data_frame = pandas.DataFrame(df)
letters = data_frame["letter"].tolist()
codes = data_frame["code"].tolist()

my_dict = dict(zip(letters, codes))
print(my_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Please enter your word: ")
user_input = user_input.upper()
my_list = []
my_list = list(user_input)
# print(my_list)

my_code = [my_dict[key] for key in user_input if my_dict[key] in codes ]




# my_code=[]
# new_codes=[]
# for (index, row) in data_frame.iterrows():
#     for _ in range(len(user_input)):
#
#         if row.letter in user_input[_]:
#             my_code.append(row.code)
#             new_codes.append(codes[index])

# print(my_dict.codes[2])
#
# for _ in range(len(user_input)):
#     if user_input[_] in letters:
#         print(my_dict.user_input[_])


# my_code = [x for x in codes if x in letters]

            # if row.code in my_code and user_input.count(row.letter) > 1:
            #     my_code.append(row.code)
            #     # print(row.code)
            # else:
            #     my_code.append(row.code)

print(my_code)
# print(new_codes)