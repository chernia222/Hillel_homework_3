# #Homework_7
# #Create a file with numbers (in a few rows)
# # Read this file, and print the sum of all numbers (create a new function for it)
# # Use try\except block to avoid other symbols except numbers in the file
# #
# # try:
# #   f = open("number_test.txt")
# #   try:
# #     f.write("Lorum Ipsum")
# #   except:
# #     print("Something went wrong when writing to the file")
# #   finally:
# #     f.close()
# #     print("Finally")
# # except:
# #   print("Something went wrong when opening the file")
#
# while True:
#     try:
#         result = input(sum_from_number)
#         break
#     except:
#         continue
#
# #   finally:
# #     f.close()
# #     print("Finally")
# # except:
# #   print("Something went wrong when opening the file")
f = open ("number_test_2", "w")

f.write("6666\n")
f.write("пп\n")
f.write("12\n")
f.write("food\n")
f.write("34\n")
f.close()


f = open("number_test_2", "r")
lines = f.readlines()
f.close()

total_sum = 0

for line in lines:
    line = line.strip()

    try:
        num = int(line)
        total_sum += num
    except ValueError:
        pass
if total_sum != 0:
    print("Сумма чисел:", total_sum)
else:
    print("В файле нет чисел")

