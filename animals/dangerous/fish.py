class Fish:
    def __init__(self):
        ''' Constructor '''
        # Some member fishies
        self.members = ['Perch', 'Pike', 'Herring']

    def printMembers(self):
        print('Printing members of the Fish class')
        for member in self.members:
            print(f'\t{member} ') 

