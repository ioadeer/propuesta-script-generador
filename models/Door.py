from operator import itemgetter

from .Frame import Frame

class Door:
    """
    A class to represent a door.

    Attributes
    ----------
    position: float
        door's position in meters
    halfDepth: float
        preguntar que es
    width: float
        door's width in meters
    height: float
        door's height in meters
    frame: type Frame 
        represent door frame
    """
    def __init__(self, desc = {}):
        """
        Constructs all the necessary attributes for the door 
        object.
        
        Parameters
        -----------
            desc: dict
                dictionary representing Doors's information
        """
        (
        self.position,
        self.halfDepth,
        self.width,
        self.height
        ) = itemgetter('position','halfDepth','width','height')(desc)
        self.frame = Frame(desc['frame'])

    def __str__(self):
        """
        Returns string with Door object info.
        """
        frame_string = self.frame.__str__()
        return('Door:\n'
              f'\tPosition: {self.position} \n' 
              f'\tPos/2:    {self.halfDepth}\n' 
              f'\tWidth:    {self.width}    \n' 
              f'\tHeight:   {self.height}   \n'
              f'\t{ frame_string }\n'
              )
