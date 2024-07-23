

# Polygon : feet up tp 4
def pol_p(feet_len,number_of_foot):
    return feet_len * number_of_foot
def pol_a(feet_len,number_of_foot,height):
    return (number_of_foot/2) * feet_len * height

# Trapezium
def tra_p(base,up_feet,left_feet,right_feet):
    return base+up_feet+left_feet+right_feet
def tra_a(base,up_feet,height):
    return (1/2)*(base+up_feet)*height


# Parallelism
def para_p(base, foot):
    return 2 * (base + foot)
def para_a(base, height):
    return base * height


# Triangle
def tri_p(f1, f2, base):
    return f1 + f2 + base
def tri_a(h, base):
    return (1 / 2) * h * base


# Square
def square_p(s_length):
    return 4 * s_length
def square_a(s_length):
    return s_length ** 2


# Circle
def cir_p(radias,angle):
    return 2 * 3.14 * radias * (angle/360)
def cir_a(radias,angle):
    return 3.14 * (radias ** 2) * (angle/360)


# Rectangle
def rec_p(r_length, r_width):
    return 2 * (r_length + r_width)
def rec_a(r_length, r_width):
    return r_length * r_width

#Choose the shape

while (True):
    print("1:                 Exit   : 0 ")
    print("2.            Rectangle   : 1 ")
    print("3.               Circle   : 2 ")
    print("4.               Square   : 3 ")
    print("5.             Triangle   : 4 ")
    print("6.          Parallelism   : 5 ")
    print("7.            Trapezium   : 6 ")
    print("8. Polygon (up to 4 feet) : 7 ")

    print(""""""""

          """""""""""")

    x = int(input("Choose command number : "))

    print(""""""""

          """""""""""")

    # Rectangle operations
    if x == 1:
        l_rec = float(input("Enter length : "))
        w_rec = float(input("Enter width : "))
        a = int(input('If you want Perimeter, enter 0 or If you want Area, enter 1 or If you want both, enter 2 :'))

        print(""""""""""""
    
            """""""")
        
        if a == 0:
            print('Perimeter is ', (rec_p(l_rec, w_rec)))
        elif a == 1:
            print('Area is ', (rec_a(l_rec, w_rec)))
        elif a == 2:
            print('Perimeter is', (rec_p(l_rec, w_rec)), 'and Area is', (rec_a(l_rec, w_rec)))

        else:
            print("Invalid request!! ")


        print(""""""""""""

              """""""")

    # Circle operations
    elif x == 2:
        r_cir = float(input("Enter radius of circle : "))
        angle = float(input("Enter Interior angle of circle : "))
        b = int(input('If you want Perimeter, enter 0 or If you want Area, enter 1 or If you want both, enter 2 :'))

        print(""""""""""""

              """""""")

        if b == 0:
            print('Perimeter is', (cir_p(r_cir,angle)))
            print(""""""""""""

                  """""""")
        elif b == 1:
            print('Area is', (cir_a(r_cir,angle)))
            print(""""""""""""

                  """""""")
        elif b == 2:
            print('Perimeter is', (cir_p(r_cir,angle)), 'and Area is', (cir_a(r_cir,angle)))

            print(""""""""""""

                  """""""")
        else:
            print("Invalid request!! ")

            print(""""""""""""

                  """""""")

    # Square operations
    elif x == 3:
        l_sq = float(input("Enter length of square : "))
        c = int(input('If you want Perimeter, enter 0 or If you want Area, enter 1 or If you want both, enter 2 :'))

        print(""""""""""""

              """""""")

        if c == 0:
            print("Perimeter is", (square_p(l_sq)))

            print(""""""""""""

                  """""""")
        elif c == 1:
            print("Area is", (square_a(l_sq)))

            print(""""""""""""

                  """""""")
        elif c == 2:
            print("Perimeter is", (square_p(l_sq)), "and Area is", (square_a(l_sq)))

            print(""""""""""""

                  """""""")

        else:
            print("Invalid request!! ")

            print(""""""""""""

                  """""""")

    # Triangle operation

    elif x == 4:
        tr_base = float(input("Enter base foot of Triangle : "))
        tr_foot1 = float(input("Enter 1st foot of Triangle : "))
        tr_foot2 = float(input("Enter 2nd foot of Triangle : "))
        tr_h = float(input("Enter height of Triangle : "))
        d = int(input('If you want Perimeter, enter 0 or If you want Area, enter 1 or If you want both, enter 2 :'))

        print(""""""""""""

              """""""")

        if d == 0:
            print("Perimeter is", (tri_p(tr_base, tr_foot1, tr_foot2)))

            print(""""""""""""

                  """""""")

        elif d == 1:
            print("Area is", (tri_a(tr_base, tr_h)))

            print(""""""""""""

                  """""""")



        elif d == 2:
            print("Perimeter is", (tri_p(tr_base, tr_foot1, tr_foot2)), "and Area is", (tri_a(tr_base, tr_h)))

            print(""""""""""""

                  """""""")

        else:
            print("Invalid request!! ")

            print(""""""""""""

                  """""""")

    # Parallelism operation
    elif x == 5:
        para_base = float(input("Enter base of Parallelism : "))
        para_foot = float(input("Enter foot of Parallelism : "))
        para_height = float(input("Enter height of Parallelism : "))
        e = int(input('If you want Perimeter, enter 0 or If you want Area, enter 1 or If you want both, enter 2 :'))

        print(""""""""""""

              """""""")

        if e == 0:
            print("Perimeter is", (para_p(para_base, para_foot)))

            print(""""""""""""

                  """""""")


        elif e == 1:
            print("Area is", (para_a(para_base, para_height)))

            print(""""""""""""

                  """""""")


        elif e == 2:
            print("Perimeter is", (para_p(para_base, para_foot)), "and Area is", (para_a(para_base, para_height)))

            print(""""""""""""

                  """""""")

        else:
            print("Invalid request!! ")

            print(""""""""""""

                  """""""")


    #Trapezium operation
    elif x == 6:
        tra_base = float(input("Enter base of Trapezium : "))
        tra_upft = float(input("Enter up feet of Trapezium : "))
        tra_lftft = float(input("Enter left feet if Trapezium : "))
        tra_rigft = float(input("Enter right feet of Trapezium : "))
        tra_height = float(input("Enter height of Trapezium : "))
        f = int(input('If you want Perimeter, enter 0 or If you want Area, enter 1 or If you want both, enter 2 :'))

        print(""""""""""""

              """""""")

        if f == 0:
            print("Perimeter is", (tra_p(tra_base,tra_upft,tra_lftft,tra_rigft)))

            print(""""""""""""

                  """""""")

        elif f == 1:
            print("Area is",(tra_a(tra_base,tra_upft,tra_height)))

            print(""""""""""""

                  """""""")

        elif f ==2:
            print("Perimeter is", (tra_p(tra_base,tra_upft,tra_lftft,tra_rigft)),"and Area is",(tra_a(tra_base,tra_upft,tra_height)))

            print(""""""""""""

                  """""""")


        else:
            print("Invalid request!! ")

            print(""""""""""""

                  """""""")
    #Polygon operation
    elif x == 7:
        num_ft = int(input("Enter number of feets : "))
        len_ft = float(input("Enter length of feet : "))
        cen_height = float(input("Enter height from mid of foot to center : "))
        g = int(input('If you want Perimeter, enter 0 or If you want Area, enter 1 or If you want both, enter 2 :'))

        print(""""""""""""

              """""""")
        if g == 0:
            print("Perimeter is",(pol_p(num_ft,len_ft)))

            print(""""""""""""

                  """""""")

        elif g == 1:
            print("Area is",(pol_a(num_ft,len_ft,cen_height)))

            print(""""""""""""

                  """""""")

        elif g == 2:
            print("Perimeter is",(pol_p(num_ft,len_ft)),"and Area is",(pol_a(num_ft,len_ft,cen_height)))

            print(""""""""""""

                  """""""")

        else:
            print("Invalid request!! ")

            print(""""""""""""

                  """""""")

    #Exit
    elif x == 0:
        print(""""""""""""

              """""""")
        print("Done. Terminating...............")

        break


    else:

        print("Invalid request!! ")

        print(""""""""""""



              """""""")
        
        print(""""""""""""



              """""""")
