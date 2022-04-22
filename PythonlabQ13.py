# # #QUESTION NO:13
def reverse(string):
    str = ""
    for i in string:
        str = i + str
    yield str


string = "C4E Python LAB!"
gen = reverse(string)
print("Received on next(): ", next(gen))