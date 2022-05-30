# temp_file = open("temp.txt", "w")
# print("Don't stop me now", file = temp_file)
# print("Cause i'm having a good time, having a good time", file = temp_file)
# temp_file.close()
#
# temp_file = open("temp.txt", mode = "r")
# for line in temp_file.readlines():
#     for word in line.split(" "):
#         print(word)
#
import  json
config_dict = {
    "name" : "Bunmi",
    "age" : "20",
    "hobby" : [1,2,3,4],
    "bool" : True,
}

with open("config.json", mode = "w") as file_obj:
    json.dump(config_dict, file_obj, indent = 4, separators = (",", ":"))

with open("config.json", mode = "r+") as file_obj:
    con = json.load(file_obj)
    print(con)


