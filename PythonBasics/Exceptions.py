ItemsInCart=0
#2 items will be added to cart

# if ItemsInCart != 2:
#     pass   # raise Exception("Products cart count don't match")
#
# assert(ItemsInCart == 2)

# try catch block

# try:
#     with open("test.txt", "r") as reader:
#         print(reader.read())
#
# except:
#     print("some how i reached this block because there is a failure")


try:
    with open("test.txt", "r") as reader:
        print(reader.read())

except Exception as e:
    print(e)

finally:
    print("Cleaning up resources")