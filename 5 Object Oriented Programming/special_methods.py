# Special Methods


mylist = [1, 2, 3]
len(mylist)


class Sample():
    pass


mysample = Sample()

print(mysample)


class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.title} by {self.author}'

    def __del__(self):
        print('A Book object has been deleted!')

    def __len__(self):
        return self.pages


b = Book('Python Rocks', 'Jose', 200)
print(b)

del b
