print("Welcome to CrimeDetector!!!")
print("We're going to find out, who stole the ice cream")

dnk = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"


print("We have got DNA, let's get started!")

import time
time.sleep(3)

# barva las
if "CCAGCAATCGC" in dnk:
    print("* Hair color is black!")
    hair_color = "black"

if "GCCAGTGCCG" in dnk:
    print("* Hair color is brown!")
    hair_color = "brown"
    
if "TTAGCTATCGC" in dnk:
    print("* Hair color is blonde!")
    hair_color = "blonde"


import time
time.sleep(3)


#oblika obraza
if "ACCACAA" in dnk:
    print("* Face shape is round!")
    face_shape = "round"

if "GCCACGG" in dnk:
    print("* Face shape is square!")
    face_shape = "square"

if "AGGCCTCA" in dnk:
    print("* Face shape is oval!")
    face_shape = "oval"

import time
time.sleep(3)


#barva oci
if "GGGAGGTGGC" in dnk:
    print("* Eye color is green!")
    eye_color = "green"

if "TTGTGGTGGC" in dnk:
    print("* Eye color is blue!")
    eye_color = "blue"

if "AAGTAGTGAC" in dnk:
    print("* Eye color is brown!")
    eye_color = "brown"



import time
time.sleep(3)


#spol
if "TGAAGGACCTTC" in dnk:
    print("* Gender is female!")
    gender = "female"

if "TGCAGGAACTTC" in dnk:
    print("* Gender is male!")
    gender = "male"



import time
time.sleep(3)


#rasa
if "AAAACCTCA" in dnk:
    print("* Race is white!")
    race = "white"

if "CGACTACAG" in dnk:
    print("* Race is black!")
    race = "black"

if "CGCGGGCCG" in dnk:
    print("* Race is asian!")
    race = "asian"

import time
time.sleep(3)

#ugotovimo, ko je osumljenec
if gender == "female"  and race == "white" and hair_color == "blonde" and eye_color == "blue" and face_shape == "oval":
    print("Eva stole the ice cream!!!")

elif gender == "female" and race == "white" and hair_color == "brown" and eye_color == "brown" and face_shape == "oval":
    print("Larisa stole the ice cream!!!")

elif gender == "male" and race == "white" and hair_color == "brown" and eye_color == "green" and face_shape == "square":
    print("Miha stole the ice cream!!!")

elif gender == "male" and race == "white" and hair_color == "black" and eye_color == "blue" and face_shape == "oval":
    print("Matej stole the ice cream!!!")

while True:
    answer = raw_input("Do you want to exit the program(yes/no) ")
    if answer == "yes":
        break
