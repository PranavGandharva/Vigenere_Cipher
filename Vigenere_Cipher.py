# -*- coding: utf-8 -*-
"""
@author: Pranav
"""


from math import gcd
import string
import numpy as np

'''
Definition for Left shift operation
'''
def left_shift(l1,n1): 
    return l1[n1:] + l1[:n1]
'''
For reverse mapping of number to character
'''
numTochar = dict(zip(range(0,26),string.ascii_lowercase))

'''
Method for first 20 coincidences
'''

def numOfcoincidences(cipher_data, copy_data):
    count=0
    no_of_coincidences=[]
    k=1
    while k<=100: #Loop for finding first 20 coincidences
        copy_data = np.roll(copy_data,1) #logic for shifting the data right
        for i,j in zip(cipher_data,copy_data):# zipping the data(data1,data2) of all elements of both arrays
            if i==j: #comparing the data of two arrays
                count+=1 #Increment counter for the same elements
        print (('Number of coincidences for'),k,('shift is:'),count)

        no_of_coincidences.append(count)
        k+=1
        count=0
        
    return no_of_coincidences

'''
Method for the first six possible lengths of key
'''

def possible_keys(no_of_coincidences):
        
    '''
    List of first highest six coincidences
    '''
    L=max(no_of_coincidences)
    L1=sorted(set(no_of_coincidences))[-2]
    L2=sorted(set(no_of_coincidences))[-3]
    L3=sorted(set(no_of_coincidences))[-4]
    L4=sorted(set(no_of_coincidences))[-5]
    L5=sorted(set(no_of_coincidences))[-6]
    
    print('\n')
    print(('Six highest coincidences are: '),L,L1,L2,L3,L4,L5)
    
    print('\n')
    
    '''
    Six Possible lengths
    ''' 
    L=no_of_coincidences.index(L)
    L+=1
    
    L1=no_of_coincidences.index(L1)
    L1+=1
    
    L2=no_of_coincidences.index(L2)
    L2+=1
    
    L3=no_of_coincidences.index(L3)
    L3+=1
    
    L4=no_of_coincidences.index(L4)
    L4+=1
    
    L5=no_of_coincidences.index(L5)
    L5+=1
    
    possible_lengths=[L,L1,L2,L3,L4,L5]
    print (('Possible key lengths are:'),possible_lengths)
        
    return possible_lengths

'''
Method for finding the final key
'''
def final_key(cipher_data,Length,):
    
    count_alphabets=[[]for i1 in range(0,Length)]
    temp_var=0
    while temp_var<Length: #Loop for deviding data into given length
        for i2 in range(temp_var,len(cipher_data),Length):
           count_alphabets[temp_var].append(cipher_data[i2])
        temp_var+=1
    temp_var=0
    Array=[] #Array for the final key
    while temp_var<Length:
        word_count=[] #Array for storing the count of each alphabet
        for charc in alphabets: #Loop for counting each alphabet in count_alphabets
            count1 = count_alphabets[temp_var].count(charc)
            count1 = count1/26
            count1 = round(count1,7)
            word_count.append(count1)
        probability_loops =24
        cipher_probability=[] #Array for storing probability of each alphabet
        shifts=0
        while probability_loops>=0: #Loop for finding the probability of each alphabet
            temp= left_shift(probability_alpha,shifts)
            temp2 = np.dot(word_count,temp)
            temp2 = round(temp2,6)
            cipher_probability.append(temp2)
            probability_loops -= 1
            shifts+=1
        Max_probability=max(cipher_probability) #For finding highest number
        char_num = [i for i, E in enumerate(cipher_probability) if E==Max_probability]# Loop for finding the index of highest num
        char_num[0]=((26-char_num[0])%26)
        key=numTochar[char_num[0]].upper()
        Array.append(key) #Storing key into final array
        numofchar=[] # Array for the number of deciphered characters
        for character in count_alphabets[temp_var]: #Loop for finding numbers of deciphered characters
            number = ord(character) - 97
            number = ((number - char_num[0])%26)
            numofchar.append(number)
        final_char=[] # Array for storing the alphabets
        for i2 in numofchar:#Loop for converting numbers into char
            final_char.append(numTochar[i2])
        count_alphabets[temp_var]=final_char
        temp_var+=1
        
    return Array,count_alphabets

'''
Method for the decryption of ciphered data
'''
    
def deciphered_data(cipher_data,Length,count_alphabets):
    temp_var=0
    var=0
    deciphered_text=[] #Array for storing deciphered text
    length_part=int(len(cipher_data)/Length) #Finding the length of each devided part
    while var<length_part: #Loop for storing deciphered text in each part
        while temp_var<Length:
            deciphered_text.append(count_alphabets[temp_var][var])
            temp_var+=1
        var+=1
        temp_var=0
    temp_var=0
    while temp_var<(len(cipher_data)%Length):#Loop for combining the parts
        deciphered_text.append(count_alphabets[temp_var][var])
        temp_var+=1
    print('\n')
    print ('Your plain Text:')
    print (''.join(str(elm) for elm in deciphered_text))
    
    
    
    
############################# Main Program ###############################

'''
Alphabets with it probability in vigenere cipher
'''
probability_alpha = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.0236,0.0015,0.01974,0.00074]
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

'''
Reading Data from text file
'''
with open('110040563.txt') as f:
    cipher_data = f.read()
print(cipher_data)
print('\n')
cipher_data=cipher_data.lower()
cipher_data=list(cipher_data)

copy_data=cipher_data

################### First 20 Coincidences #######################
no_coincidences = numOfcoincidences(cipher_data, copy_data)

################### First six possible lengths ##################
possiblelengths = possible_keys(no_coincidences)

'''
GCF of first two possible lengths
'''

gcf_first_two_keys = gcd(possiblelengths[0],possiblelengths[1])
print('\n')
print (('Gcf of First two possible lengths:'),gcf_first_two_keys)
   
Length=gcf_first_two_keys
print('\n')
print (('Length of the key is '),Length)
#####################  Calling method for the encryption key ##########################
print('\n')
print ('The Encryption Key:')
return_val = final_key(cipher_data, Length)
key = ''.join(return_val[0])
print(key)
count_alphabets = return_val[1]
##################### Calling method for the deciphered text #######################
deciphered_data(cipher_data, Length, count_alphabets)
###################### recovering the L parts into deciphered form ################

    