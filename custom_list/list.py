class CustomList(list):
    def __getitem__(self, index):
        if index <= 0:
            raise IndexError("Index out of bounds")
        return super(CustomList, self).__getitem__(index - 1)


l = CustomList()
l.append(2)
l.append(8)
l.append(14)
print(l.__getitem__(2))
print(l[1])
