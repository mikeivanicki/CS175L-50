#restaurant.py
#CS175-50L
#Michael Ivanicki
vegetarian=False
vegan=False
gluten_free=False

input_1=input('Is anyone in your party vegetarian? ')
if input_1=='yes':
    vegetarian=True
input_2=input('Is anyone in your party vegan? ')
if input_2=='yes':
    vegan=True
input_3=input('Is anyone in your party gluten free? ')
if input_3=='yes':
    gluten_free=True
    
print('Here are your restaurant choices:')
if vegetarian==True and vegan==False and gluten_free==False \
   or vegetarian==False and vegan==False and gluten_free==False:
    print('Mama\'s Fine Italian')
if vegetarian==True and gluten_free==True and vegan==False \
   or vegetarian==False and gluten_free==False and vegan==False \
   or vegetarian==True and gluten_free==False and vegan==False \
   or vegetarian==False and gluten_free==True and vegan==False:
    print('Main Street Pizza')
if vegetarian==False and vegan==False and gluten_free==False: 
    print ('Joe\'s Gourmet Burgers')
print ('Corner Cafe \nChef\'s Kitchen')

X=True
UI=input('Would you like to do another restaurant search?: ')
if UI=='no':
    X=False
while X == True:
    vegetarian=False
    vegan=False
    gluten_free=False

    input_1=input('Is anyone in your party vegetarian? ')
    if input_1=='yes':
        vegetarian=True
    input_2=input('Is anyone in your party vegan? ')
    if input_2=='yes':
        vegan=True
    input_3=input('Is anyone in your party gluten free? ')
    if input_3=='yes':
        gluten_free=True
    
    print('Here are your restaurant choices:')
    if vegetarian==True and vegan==False and gluten_free==False \
       or vegetarian==False and vegan==False and gluten_free==False:
        print('Mama\'s Fine Italian')
    if vegetarian==True and gluten_free==True and vegan==False \
       or vegetarian==False and gluten_free==False and vegan==False \
       or vegetarian==True and gluten_free==False and vegan==False \
       or vegetarian==False and gluten_free==True and vegan==False:
        print('Main Street Pizza')
    if vegetarian==False and vegan==False and gluten_free==False: 
        print ('Joe\'s Gourmet Burgers')
        print ('Corner Cafe \nChef\'s Kitchen')
    UI=input('Would you like to do another restaurant search?: ')
    if UI=='no':
        X=False
