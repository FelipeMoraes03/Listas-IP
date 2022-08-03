nome1 = str(input())
visu1 = int(input())
nome2 = str(input())
visu2 = int(input())
nome3 = str(input())
visu3 = int(input())

if (visu1 >= visu2) and (visu1 >= visu3) and (visu2 >= visu3):
    print(nome1 + " " + str(visu1))
    print(nome2 + " " + str(visu2))
    print(nome3 + " " + str(visu3))

elif (visu1 >= visu2) and (visu1 >= visu3) and (visu3 >= visu2):
    print(nome1 + " " + str(visu1))
    print(nome3 + " " + str(visu3))
    print(nome2 + " " + str(visu2))

elif (visu2 >= visu3) and (visu2 >= visu1) and (visu1 >= visu3):
    print(nome2 + " " + str(visu2))
    print(nome1 + " " + str(visu1))
    print(nome3 + " " + str(visu3))

elif (visu2 >= visu3) and (visu2 >= visu1) and (visu3 >= visu1):
    print(nome2 + " " + str(visu2))
    print(nome3 + " " + str(visu3))
    print(nome1 + " " + str(visu1))

elif (visu3 >= visu1) and (visu3 >= visu2) and (visu1 >= visu2):
    print(nome3 + " " + str(visu3))
    print(nome1 + " " + str(visu1))
    print(nome2 + " " + str(visu2))

else:
    print(nome3 + " " + str(visu3))
    print(nome2 + " " + str(visu2))
    print(nome1 + " " + str(visu1))
