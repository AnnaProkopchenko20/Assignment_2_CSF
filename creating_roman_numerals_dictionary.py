
#import pickle

#roman_nums_decimal = {}

#for num_E3,i in enumerate(["","M","MM","MMM"]):
    #for num_E2,j in enumerate(["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]):
        #for num_E1,k in enumerate(["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]):
            #for num_E0,l in enumerate(["","I","II","III","IV","V","VI","VII","VIII","IX"]):
                #roman_nums_decimal[int(num_E3*1E3+num_E2*1E2+num_E1*1E1+num_E0)] = i+j+k+l

#with open("all_roman_numerals_dictionary","wb") as file:
    #pickle.dump(roman_nums_decimal,file)


#print(roman_nums_decimal[923])
#some info:
#you can write 1-3999 in roman numerals,(there is no 0 and nothing bigger than 3999)

