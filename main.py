def Convert_to_Unicode():
    unicode = str(input("String:"))
    list1 = list(unicode)
    list2 = []
    list3 = []
    for i in list1:
        item = ord(i)
        item2 = str("U+"+hex(ord(i)))
        list2.append(item)
        list3.append(item2)

    print("Decimal:", list2)
    print("Unicode:",list3)

def Convert_to_ASCII():
    ASCII = int(input("Number (Decimal, > 31):"))
    print("ASCII:", chr(ASCII))

Exit = False
def question():
    global Exit
    q = str(input("Convert to ASCII or Unicode? Type EXIT to leave.\n"))
    if q.upper() == "ASCII":
        Convert_to_ASCII()
    if q.upper() == "UNICODE":
        Convert_to_Unicode()
    if q.upper() == "EXIT":
        print("Exiting...")
        Exit = True

while not Exit:
    question()