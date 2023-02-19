# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 17:05:09 2022

@author: xxLifexx
"""
import collections
import matplotlib.pyplot as plt
from pycipher import ColTrans
import re

def crack_b2():
    plain_text = []
    cipher_text = []
    declaration_text = []
     
    with open("b2.txt", "r") as file:
        for line in file:
            cipher_text = line.rstrip().replace(" ", "").split(',')
        
    with open("declaration.txt", "r") as file2:
        declaration_text = [word for line in file2 for word in line.split()]
    
    for i in range(len(cipher_text)):
        j = int(cipher_text[i])
        
        if j >= 480:
            shift = j + 10
            plain_text.insert(i, declaration_text[int(shift)][0])
            
            if j == 811:
                plain_text.insert(i, 'y')
            
            if j == 1005:
                plain_text.insert(i, 'x')              
        else:
            plain_text.insert(i, declaration_text[j][0])
            
        """elif int(j) == 84:
            j = 85
            plain_text.insert(i, declaration_text[j][0])
            
        elif int(j) == 53:
            j = 54
            plain_text.insert(i, declaration_text[j][0])
            
        elif int(j) == 96:
            j = 95
            plain_text.insert(i, declaration_text[j][0])"""   
            
    trim_plain_text = plain_text[:-13]        
    return trim_plain_text 
    
def solve_without_four_digits():
    plain_text = []
    cipher_text = []
    declaration_text = []
    updated_cipher = []
     
    with open("b3b1.txt", "r") as file:
        for line in file:
            cipher_text = line.rstrip().replace(" ", "").split(',')
        
    with open("declaration.txt", "r") as file2:
        declaration_text = [word for line in file2 for word in line.split()]
        
    updated_cipher = [value for value in cipher_text if int(value) < 1431] 

    for i in range(len(updated_cipher)):
        j = int(updated_cipher[i])
        
        if int(j) >= 480:
            shift = j + 10

            if j == 1317:
                shift = 1317
            
            if j == 811:
                plain_text.insert(i, 'y')
            
            if j == 1005:
                plain_text.insert(i, 'x') 

            plain_text.insert(i, declaration_text[int(shift)][0])

        else:
            plain_text.insert(i, declaration_text[j][0])
   
    return plain_text

def solve_with_four_digits():
    plain_text = []
    cipher_text = []
    declaration_text = []
    num_to_big = []
     
    with open("b3b1.txt", "r") as file:
        for line in file:
            cipher_text = line.rstrip().replace(" ", "").split(',')
        
    with open("declaration.txt", "r") as file2:
        declaration_text = [word for line in file2 for word in line.split()]
    
    for x in cipher_text:
        if int(x) > 1322:
            num_to_big.append(int(x))
            cipher_text = replace_values(cipher_text, x, '0')

    for i in range(len(cipher_text)):
        j = int(cipher_text[i])
        #print (j)
        
        if int(j) >= 480:
            shift = j + 10

            if j == 1317:
                shift = 1317
            
            if j == 811:
                plain_text.insert(i, 'y')
            
            if j == 1005:
                plain_text.insert(i, 'x') 

            plain_text.insert(i, declaration_text[int(shift)][0])
  
        else:
            plain_text.insert(i, declaration_text[j][0])
   
    return plain_text, num_to_big

def split_columns(method, size, name):
        plain_text = method()
        i = 0
        value = int(1128 / int(size))
        value_two = 1128
        with open(size + "_" + name +  "_" + "column_b3b1.txt", "w") as file:
            for x in plain_text:
                file.writelines(x + "\n")
                i += 1
                if i == int(size):
                    file.write("-------------NEXT COLUMN STARTS HERE!-------------\n")
                    i=0
            file.write("First letter in each columns:")
            while value_two != 0:
                file.write(plain_text[abs(value_two-1128)])
                value_two -= int(size)

            value_two = 1128
            file.write("\nSecond letter in each columns:")
            while value_two != 0:
                file.write(plain_text[(abs(value_two-1128)+1)])
                value_two -= int(size)

                 
def read_file_and_seperate():
    with open("b3b1.txt", "r") as file:
        for line in file:
            nums = line.rstrip().replace(" ", "").split(',')
    return nums

def get_duplicates():
    read_in_values = read_file_and_seperate()
    values = collections.Counter(read_in_values)
    
    duplicate_values = [i for i in values if values[i]>1]
    return duplicate_values

def get_no_duplicates():
    read_in_values = read_file_and_seperate()
    values = collections.Counter(read_in_values)
    
    no_duplicate_values = [i for i in values if values[i]==1]
    return no_duplicate_values

def search(value, clist):
    return ('%s : %d' % (value, clist[value]))

def replace_values(list_to_replace, item_to_replace, item_to_replace_with):
    return [item_to_replace_with if item == item_to_replace else item for item in list_to_replace]

def graph(gname):
    plt.bar(gname.keys(), gname.values())
    plt.show()
    
def get_caps(method, txtfile):
    cap_letters = []
    
    if txtfile == "b3b1":
        plain_text_load = method()
        
    elif txtfile == "b2":
        plain_text_load = crack_b2()
        
    else:
        print ("NOT FOUND !")
   
    for x in plain_text_load:
        if x.isupper() == True:
           cap_letters.append(x)
           
    return cap_letters

def decrypt_columns(key, use_list):
    joined_d_text = ""
    
    encrypted_text = use_list
    
    for element in encrypted_text:
        joined_d_text += element
        
    decrypted_text = ColTrans(key).decipher(joined_d_text)
    return decrypted_text

def delete_duplicate_words():
    result = []
    no_result = []
    p = ""
    with open('all_words_english_language.txt', "r") as word_file:
        alpha = set(word_file.read().split())

    for string in alpha:
        p = ""
        for char in string:
            if char not in p:
                p = p+char
            if p == string:
                result.append(string)
            else:
                no_result.append(string)

    with open('alpha_words_NDL.txt', "w") as word_file2:
        for word in result:
            word_file2.write(word + "\n")

def split_columns_print(list_to_use):
    list_to_return_one = []
    list_to_return_two = []
    list_to_return_three = []
    list_to_return_four = []
    list_to_return_five = []
    list_to_return_six = []
    #list_to_return_seven = []
    #list_to_return_eight = []

    for x in list_to_use[:187]:
        list_to_return_one.append(x)

    for x in list_to_use[188:375]:
        list_to_return_two.append(x)

    for x in list_to_use[376:563]:
        list_to_return_three.append(x)

    for x in list_to_use[564:751]:
        list_to_return_four.append(x)

    for x in list_to_use[752:939]:
        list_to_return_five.append(x)

    for x in list_to_use[940:1127]:
        list_to_return_six.append(x)

    #for x in list_to_use[846:986]:
    #    list_to_return_seven.append(x)

    #for x in list_to_use[987:1127]:
    #    list_to_return_eight.append(x)

    return list_to_return_one, list_to_return_two, list_to_return_three, list_to_return_four, list_to_return_five, list_to_return_six



def main():
    user_input = ""
    search_input = ""
    total_nums = read_file_and_seperate()
    dup_vals = collections.Counter(get_duplicates())
    no_dup_vals = collections.Counter(get_no_duplicates())
    total_values = collections.Counter(total_nums)
    alpha_map = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 
                9:'I', 10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 
                17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X',
                25:'Y', 26:'Z'}

    while user_input != "ex":
        user_input = input("Enter [columns], [decryptColumn], [search], [replace], [crackB2], [solve], [graph], [showCaps] or [ex]: \n")
        
        if user_input == "duplicate":
            print (dup_vals)
            print ("-----------------------------------------------------------------------------------------------------------------------------")
        
        elif user_input == "decryptColumn":
            use_this_list, nums = solve_with_four_digits()
            key = input("Enter the key or [ex]: ")

            #key2 = ''

            #for i in key:
            #    #print(alpha_map.get(int(i)))
            #    key2 += alpha_map.get(int(i))

            #print("Key used", key2)
            if key == "ex":
                print ("-----------------------------------------------------------------------------------------------------------------------------")
            else:
                with open('alpha_words_NDL.txt', "r") as word_file2:
                    for word in word_file2:
                        text = decrypt_columns(word, use_this_list)
                        print(text)
                        print ("-----------------------------------------------------------------------------------------------------------------------------")
            
            second_round = input("Decrypt again? [y] or [n]: ")
            if second_round == "y":
                second_text = decrypt_columns(key, text)
                print(second_text)
                print ("-----------------------------------------------------------------------------------------------------------------------------")

            elif second_round == 'n':
                break

            else:
                print ("Enter 'y' or 'n' !")
                break

            third_round = input("Decrypt again? [y] or [n]: ")
            if third_round == "y":
                second_text = decrypt_columns(key, second_text)
                print(second_text)
                print ("-----------------------------------------------------------------------------------------------------------------------------")

            elif third_round == 'n':
                break

            else:
                print ("Enter 'y' or 'n' !")
                break
                   
        elif user_input == "delete":
            delete_duplicate_words()
            print("Deleted all words wth duplicate letters!")
            print ("-----------------------------------------------------------------------------------------------------------------------------")
        
        elif user_input == "search":
            search_input = input("Enter number to search for or [ex]: ")
            if search_input == "ex":
                print ("-----------------------------------------------------------------------------------------------------------------------------")
                break
            else:
                search_list = input("Enter list to search through [t,d,n] or [ex]: ")
                if search_list == "t":
                    s = search(search_input, total_values)
                    print (s)
                elif search_list == "d":
                    s = search(search_input, dup_vals)
                    print (s)
                elif search_list == "n":
                    s = search(search_input, no_dup_vals)
                    print (s)
                elif search_list == "ex":
                    print ("-----------------------------------------------------------------------------------------------------------------------------")                  
    
        elif user_input == "replace":
            replace_input = input("Enter number to replace or [ex]: ")
            if replace_input == "ex":
                print ("-----------------------------------------------------------------------------------------------------------------------------")
                
            else:
                replace_new_value = input("Enter new number: ")
                replaced_list = replace_values(total_nums, replace_input, replace_new_value)
                total_nums = replaced_list
                print ("-----------------------------------------------------------------------------------------------------------------------------")

        elif user_input == "crackB2":
            print ("-----------------------------------------------------------------------------------------------------------------------------")
            print ("Cracking .........")
            plain_text_dis = crack_b2()
            print (*plain_text_dis)
            print ("Charachters of plaintext: " , len(plain_text_dis))
            i = 0
            with open("crackedB2.txt", "w") as file:
                for x in plain_text_dis:
                    file.writelines(x + " ")
                    i += 1
                    if i == 7:
                        file.write("\n")
                        i=0
            print ("-----------------------------------------------------------------------------------------------------------------------------")

        elif user_input == "solve":
            print ("-----------------------------------------------------------------------------------------------------------------------------")
            list_to_use = input("Enter [w4], [w/4] or [ex]: ")
            
            if list_to_use == "ex":
                break
            
            elif list_to_use == "w4":
                plain_text_dis, digits = solve_with_four_digits()
                digits.sort()

            elif list_to_use == "w/4":
                plain_text_dis = solve_without_four_digits()  
                digits = []        
            else:
                print ("Enter one if the above to solve with or without four digit values!")    
 
            print (*plain_text_dis , "\n")
            lower_case = [x.lower() for x in plain_text_dis]
            frequency = collections.Counter(lower_case)
            print (frequency)

            print ("\nDigits out of range: ", digits)
            print ("\nCharachters of plaintext: " , len(plain_text_dis))
            column_one, column_two, column_three, column_four, column_five, column_six = split_columns_print(plain_text_dis)

            '''print ("\n", *column_one)
            print ("\n", *column_two)
            print ("\n", *column_three)
            print ("\n", *column_four)
            print ("\n", *column_five)
            print ("\n", *column_six)'''
            print ("-----------------------------------------------------------------------------------------------------------------------------")
  
        elif user_input == "graph":
            print ("-----------------------------------------------------------------------------------------------------------------------------")
            graph(total_values)
            print ("-----------------------------------------------------------------------------------------------------------------------------")

        elif user_input == "showCaps":
            print ("-----------------------------------------------------------------------------------------------------------------------------")
            txtfile = input("Enter file to get caps from [b3b1] or [b2]: ")
            list_to_use = input("Enter [w4], [w/4] or [ex]: ")
            
            if list_to_use == "ex":
                break
            
            elif list_to_use == "w4":
                show_caps = get_caps(solve_with_four_digits, txtfile)
                
            elif list_to_use == "w/4":
                show_caps = get_caps(solve_without_four_digits, txtfile)
            
            else:
                print ("Enter one if the above to solve with or without four digit values!")
                
            print (*show_caps)
            print ("Number of caps: " , len(show_caps))
            print ("-----------------------------------------------------------------------------------------------------------------------------")

        elif user_input == "columns":
            print ("-----------------------------------------------------------------------------------------------------------------------------")
            size = input("Enter size of column: ")
            list_to_use = input("Enter [w4], [w/4] or [ex]: ")
            
            if list_to_use == "ex":
                break
            
            elif list_to_use == "w4":
                split_columns(solve_with_four_digits, size, "w4")
                
            elif list_to_use == "w/4":
                split_columns(solve_without_four_digits, size, "wo4")
            
            else:
                print ("Enter one if the above to solve with or without four digit values!")

            print ("-----------------------------------------------------------------------------------------------------------------------------")
        elif user_input == "ex":
            print ("-----------------------------------------------------------------------------------------------------------------------------")
            print ("Exitting")
            print ("-----------------------------------------------------------------------------------------------------------------------------")
        else:
            print ("-----------------------------------------------------------------------------------------------------------------------------")
            print ("Enter Valid List Option!")
            print ("-----------------------------------------------------------------------------------------------------------------------------")

main()

