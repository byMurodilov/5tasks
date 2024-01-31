# 1
# from collections import namedtuple
# def funcs(pr_1, pr_2):
#     words = namedtuple('Sozlar', 'birinchi ikkinchi')
#     minus_words = pr_1.split()
#     obj_of_words = words(birinchi=minus_words[0], ikkinchi=minus_words[1])
#     jips_sozs = f"{obj_of_words.birinchi}{pr_2}{obj_of_words.ikkinchi}"
#     return jips_sozs
# pr_1 = "Bizni bizkutgankunlar"
# pr_2 = ",kutar "
# result = funcs(pr_1, pr_2)
# print(result)


# 2
# def counter_unli(input_str, unlis):
#     return sum(1 for char in input_str if char in unlis)
# input_str = str(input("So'z kiritng: "))
# unlis = "aeiouAUOEI"
# result = counter_unli(input_str, unlis)
# print(f"{result}ta unli harf mavjud!")


# 3
# def sub_zero(number):
#     permission_num = "0"
#     sub_zero_count = sum(1 for digit in str(number) if digit in permission_num)
#     return sub_zero_count
# nol = int(input("Istalgan raqam kiriting: "))
# result = sub_zero(nol)
# print(f"Bu raqam ichida <<{nol}>> {result}ta /0\ qatnashgan.")


# 4
# str1 = str(input("1-so'zni kiriting:"))
# str2 = str(input("2-so'zni kiriting:"))
# def are_unlis(str1, str2):
#     vowels = "aeiouAEIOU"
#     return all(vowel in str2 for vowel in str1 if vowel in vowels)
#
# if are_unlis(str1,str2):
#     print(f"1- va 2- kiritlgan so'zlar bir xil: (1-'{str1}') va (2-'{str2}')")
# else:
#     print("Something Went WRONG!, try again LATTER!")


# 5
# input_str = str(input("So`zlar kiritng:"))
# def sozs_sanar(input_str):
#     soz_count = 0
#     inside_word = 0
#     for varchar in input_str:
#         if varchar.isalnum():
#             inside_word = True
#         elif inside_word:
#             soz_count+=1
#             inside_word = False
#     if inside_word:
#         soz_count+=1
#     return soz_count
# res = sozs_sanar(input_str)
# print(f"{res}ta so`zdan iborat. [{input_str}]")