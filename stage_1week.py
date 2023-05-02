# import math
# x = 8**3 + 4*(2+2)
# print(x)
# namec = input("Enter your name: ")
# # print(namec)
# num_1 = 90
# num_2 = 87
# exampe = f"Simple example {num_1} + {num_2} = {num_1 + num_2}"
# print(exampe)

# name = input("Enter your name: ")
# last_name = input('Enter your last name:')
# full_name = f"{name} {last_name}"
# print(full_name)


#ТИПИ ДАНИХ 'convertation'
# num_1 = str(1) # integer
# num_2 = int(float(str(1.8))) #float
# string_1 = int('3')
# print(type(num_1), type(num_2), type(string_1))
# 

# volume = float(input('Fuel volume: '))
# price = float(input('Fuel price: '))
# bill = f'Your bill is {volume * price}'
# print(bill)
# print(type(volume), type(price))

# length = float('2.75')
# width = float("1.75")
# area = length * width
# print(area)

# length = float("2.75")
# width = float("1.75")
# area = length * width
# show = f"With width {float(2.75)}, and length {float(1.75)} of the room,ow its area is equal to {(length * width)}"
# # show = f"With width {"2.75"}, and length {"1.75"} of the room, its area is equal to {float(length) * float(width)}"
# print(show)


# import math

# RADIUS = 6371.01

# lat1 = 50.45
# lon1 = 30.523

# lat2 = 51.5072
# lon2 = -0.1275

# distance = RADIUS * math.acos(math.sin(math.radians(lat1))) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.cos(math.radians(lon1) - math.radians(lon2))
# print(distance)

# from math import sqrt
# x1 = 50.45
# x2 = 30.523

# y1 = 51.5072
# y2 = -0.1275

# s = sqrt((x2 -x1)**2 + (y2 - y1)**2)

# print(s)

# ---------------=========================-----------------
#                      WHILE LOOP
# count = 1

# while count < 3:
#     print('Hello')
#     count += 1

# num = int(input("Enter the integer (0 to 100): "))
# sum = 0

# while sum < 100:

#     sum += 1



# num = int(input("Enter the integer (0 to 100): "))
# sum = 0

# while num in [0, 20]:
#     sum = sum +1

# print(sum)
    

    
# ---------------=========================-----------------
# #                       FOR loop
# for i in iterative:
#     pass # заглушка

# range(start, stop, step)

# ---------------=========================-----------------
#                   LOOP Interraption
#   break
#   continue
# ---------------=========================-----------------


# i = 0

# while True:
    
#     print(i)
#     i += 1
#     if i ==5:
#         break


# for i in range (10):
#     if i % 2:
#         continue
#     print(i)
# while True:
#     print(1)
#     break
# else:
#     print(2)

# ---------------=========================-----------------
#                   LOOP Interraption
#   break
#   continue
# ---------------=========================-----------------
# ================================================
# VCS - git/ github/ gilub
# Databases - SQL vs NoSQL (MySQL, MongoDB, Redis) 
# WLK stack
# Prometheus + Grafana
# CI / CD
# Test - Unit tests, Integration tests
# Containerization + Docker
# Cloud - AWS / GCP / Azure
# Bash /Unix
# Django / Flask/ /// Fast API / Tornado

# z
# num = int(input("Enter the integer (0 to 100): "))
# sum = 0
# 
# while sum <= num:
    # print(sum)
    # sum += 1
# 
    # sum = sum + 1
# print(sum**num)

# ===============exceptions==============

# while True:
    
#     user_input = input('Enter a number: ')

#     try:
#         x = int(user_input)
#     except ValueError as error:
#         print(error)#'Should be a number. Please try again; ')
#         continue
#     except TypeError:
#         print('tYPE')
#         continue
#     else:#  esli ne nastupilo iskuchenie
#         print("Else")
#     finally:
#         print('finally')

#     break

# =================Raising exeption==========

# raise ValueError('messAGE') zastavljaen interpretator PRINUDITELNO vyzvat' iskluchenie, UKAZYVAEM svoju LOGIKU