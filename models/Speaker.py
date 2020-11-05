from operator import itemgetter

class Speaker:                
    def __init__(self, desc = {}):
        (
        self.x,
        self.y,
        self.z,
        ) = itemgetter('x','y','z')(desc['position']) 
        self.rotation = desc.get('rotation')

    def __str__(self):
        return(' Speaker:\n'
               f'\tPos x:    {self.x}\n'
               f'\tPos y:    {self.y}\n'
               f'\tPos z:    {self.z}\n'
               f'\tRotation: {self.rotation}\n')
