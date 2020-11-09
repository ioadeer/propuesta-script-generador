from operator import itemgetter

class Skirting:
    """
    A class to represent a skirting.

    Attributes
    ----------
    height: float
        room skirting's height in meters (Note that to the original value an offset that
        represents the room's wall thicknness is added)
    thickness: float
        room skirting's thickness 

    """
    def __init__(self, offset, desc = {}):
        """
        Constructs all the necessary attributes for the skirting 
        object.
        
        Parameters
        -----------
            desc: dict
                dictionary representing skirting's information
        """
        (
        self.height, 
        self.thickness,
        ) = itemgetter('height', 'thickness')(desc) 
        self.height += offset 

    def __str__(self):
        """
        Returns string with Speaker object info.
        """
        return(' Skirting:\n'
              f'\tHeight:   {self.height} \n' 
              f'\tThickness:{self.thickness}\n' )

