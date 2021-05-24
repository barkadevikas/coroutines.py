def searcher():
    import time
    book="this is vikas book"
    time.sleep(3)

    while True:
        text=(yield )
        if text in book:
            print("text available in book")
        else:
            print("text not in book")


search=searcher()
print("start searching")
next(search)
search.send("vikas")
input("press any key")
search.send("harryk")