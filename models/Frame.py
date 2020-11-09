from operator import itemgetter

class Frame:
    """
    A class to represent a door frame.

    Attributes
    ----------
    width: float
        door width in meters 
    thickness: float
        door thickness in meters
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
        self.width, self.thickness= itemgetter('width','thickness')(desc)
    def __str__(self):
        """
        Returns string with Door object info.
        """
        return('Frame:\n'
              f'\t Width:    {self.width}    \n' 
              f'\t Thickness:{self.thickness}\n' )
