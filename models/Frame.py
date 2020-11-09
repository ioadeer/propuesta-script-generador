from operator import itemgetter

class Frame:
    """
    A class to represent a door frame.

    Attributes
    ----------
    x: float
        door frame's x size in meters
    y: float
        door frame's y size in meters
    """
    def __init__(self, desc = {}):
        """
        Constructs all the necessary attributes for the door 
        frame object.
        
        Parameters
        -----------
            desc: dict
                dictionary representing Frame's information
        """
        self.x, self.y = itemgetter('x','y')(desc)
    def __str__(self):
        """
        Returns string with Door object info.
        """
        return('Frame:\n'
              f'\t X:    {self.x}    \n' 
              f'\t Y:    {self.y}    \n' )
