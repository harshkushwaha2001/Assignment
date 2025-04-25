class Rectangle:
    def __init__(self, length: int, width: int):
        # Initializing Rectangle Class.
        # length (int): Length of the rectangle.
        # width (int): Width of the rectangle.
        self.length = length
        self.width = width

    def __iter__(self):
        # Making Rectangle Class iterable
        yield {'length': self.length} # dict: {'length': <value_of_length>}
        yield {'width': self.width}   # dict: {'width': <value_of_width>}


# Creating instance of Rectangle Class
rect = Rectangle(20, 15)

# Iterating over Rectangle instance to get its length and width
for item in rect:
    print(item)
