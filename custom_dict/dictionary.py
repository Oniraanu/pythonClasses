import json


class CustomDictionary(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)

    def __getitem__(self, key):
        if key <= 0:
            return super(CustomDictionary, self).__getitem__(key - 1)


new_dict = CustomDictionary()
new_dict["Name"] = "Wale"
new_dict["Age"] = 12
new_dict["Occupation"] = "Being broke"
with open("my_custom_dict.txt", 'w', encoding='utf-8') as dict_file:
    json.dump(new_dict, dict_file)
