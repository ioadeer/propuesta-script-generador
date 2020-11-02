from operator import itemgetter

class Room:
    def __init__(self, desc = {}):
        self.name = desc['name']
        (
        self.depth, 
        self.width, 
        self.height,
        ) = itemgetter('depth',
                       'width', 
                       'height',
                       )(desc['dimensions'])
        self.wall_thickness = itemgetter('wall_thickness')(desc)
        elements = desc['elements']
        for element in elements: 
            if(element == 'speaker'):
                self.speaker = Speaker(elements[element])
            elif(element == 'door'):
                self.door = Door(elements[element])
            elif(element == 'skirting'):
                self.skirting = Skirting(self.wall_thickness,elements[element]) 

        self.spot = Spot(desc['spot'])
        self.camera = Camera(desc['camera'])

    def __str__(self):
        return('\nRoom:\n'
              f' Name: { self.name }.\n'
               ' Dimensions:\n' 
              f'\tdepth:          { self.depth  }\n'  
              f'\twidth:          { self.width  }\n'  
              f'\theight:         { self.height }\n'
              f'\twall thickness: { self.wall_thickness }\n'
              )

    def dump_room_info(self):
        roomString = self.__str__()
        speakerString = self.speaker.__str__()
        doorString = self.door.__str__()
        skirtingString = self.skirting.__str__()
        spotString = self.spot.__str__()
        cameraString = self.camera.__str__()
        room_info = (
                    f'{roomString}'
                    f'{speakerString} ' 
                    f'{doorString}'
                    f'{skirtingString}'
                    f'{spotString}'
                    f'{cameraString}'
                    )
        return(room_info)

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
class Door:
    def __init__(self, desc = {}):
        (
        self.position,
        self.halfDepth,
        self.width,
        self.height
        ) = itemgetter('position','halfDepth','width','height')(desc)
        self.frame = Frame(desc['frame'])

    def __str__(self):
        frame_string = self.frame.__str__()
        return('Door:\n'
              f'\tPosition: {self.position} \n' 
              f'\tPos/2:    {self.halfDepth}\n' 
              f'\tWidth:    {self.width}    \n' 
              f'\tHeight:   {self.height}   \n'
              f'\t{ frame_string }\n'
              )

class Frame:
    def __init__(self, desc = {}):
        self.x, self.y = itemgetter('x','y')(desc)
    def __str__(self):
        return('Frame:\n'
              f'\t X:    {self.x}    \n' 
              f'\t Y:    {self.y}    \n' )

class Skirting:
    def __init__(self, offset, desc = {}):
        (
        self.height, 
        self.thickness,
        ) = itemgetter('height', 'thickness')(desc) 
        self.height += offset 

    def __str__(self):
        return(' Skirting:\n'
              f'\tHeight:   {self.height} \n' 
              f'\tThickness:{self.thickness}\n' )

class Spot:
    def __init__(self, desc = {}):
        (
        self.posX,
        self.posY,
        self.posZ
        ) = itemgetter('x','y','z')(desc['position'])
        (
        self.rotX,
        self.rotY,
        self.rotZ
        ) = itemgetter('x','y','z')(desc['rotation'])

    def __str__(self):
        return(' Spot\n'
                '\tPosition:\n'
              f'\tX:    {self.posX}\n'
              f'\tY:    {self.posY}\n'
              f'\tZ:    {self.posZ}\n'
               '\tRotation\n'
              f'\tX:    {self.rotX}\n'
              f'\tY:    {self.rotY}\n'
              f'\tZ:    {self.rotZ}\n'
              )

class Camera:
    def __init__(self, desc = {}):
        (
        self.posX,
        self.posY,
        self.posZ
        ) = itemgetter('x','y','z')(desc['position'])
        self.rotation = desc.get('rotation')

    def __str__(self):
        return(' Camera\n'
                '\tPosition:\n'
              f'\tX:    {self.posX}\n'
              f'\tY:    {self.posY}\n'
              f'\tZ:    {self.posZ}\n'
              f'\tRotation:\n\t{self.rotation}\n'
              )
