from operator import itemgetter

class Camera:
    """
    A class to represent a Blender camera.

    Attributes
    ----------
    x: float
        camera's x position in meters
    y: float
        camera's y position in meters
    z: float
        camera's z position in meters
    rotation: float
        camera rotation in degrees 
    """
    def __init__(self, desc = {}):
        """
        Constructs all the necessary attributes for the Blender
        camera object.

        Parameters
        -----------
            desc: dict
                dictionary representing Camera's information
        """
        (
        self.x,
        self.y,
        self.z
        ) = itemgetter('x','y','z')(desc['position'])
        self.rotation = desc.get('rotation')

    def __str__(self):
        """
        Returns string with Camera object info.
        """
        return(' Camera\n'
                '\tPosition:\n'
              f'\tX:    {self.x}\n'
              f'\tY:    {self.y}\n'
              f'\tZ:    {self.z}\n'
              f'\tRotation:\n\t{self.rotation}\n'
              )
