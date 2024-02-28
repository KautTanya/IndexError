"""IndexError"""
try:
    new_list = ["a", "b", "c", "d"]
    print(new_list[2])
except IndexError:
    print("No such index exists")
