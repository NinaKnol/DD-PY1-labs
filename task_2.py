# TODO Найдите количество книг, которое можно разместить на дискете

one_book = 4*25*50*100
total = 1.44*1024*1024

books = int(total // one_book)
print("Количество книг, помещающихся на дискету:", books)