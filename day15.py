# try: 
#     f = open("day15_input.txt", "r")
#     print(f.read())
# except FileNotFoundError:
#     print("File not found")

f = open("day.txt", "r+")
f.write("\nHello, jj!")
f.read()
f.close()