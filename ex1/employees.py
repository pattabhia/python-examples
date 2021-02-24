list = ["ram", "rahim", 'akbar', 'amar']
try:
    print(list);
    print(list[0]);
    print(list[1]);
    print(list[2]);
    print(list[3]);
    print(list[4]);
    print(list[5]);
    print(list[6]);
    print(list[7]);
    print(list[8]);
except BaseException:
    print("ERROR OCCURRED");
    #raise BaseException('ERROR TO CALLER');
#Exception Handling
#Loop List
list[3] = 'Sunil';
print(list*3)
print(list[2][1])
if("akbar" in list) :
    print('yes')
else :
    print('no')
tuple = ("ram", "rahim", 'akbar', 'amar')
print(tuple[0])
for tup in tuple:
    print('========>'+tup);
for index in range(len(tuple)) :
    print("::"+tuple[index])
#Dictionaries - > Object value
print ('test');