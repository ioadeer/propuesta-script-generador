import unittest
import json

"""
Room destructuring tests call from this dir
python3 TestRoomModel.py
"""

from models.Room import Room 
from models.Speaker import Speaker
from models.Door import Door
from models.Skirting import Skirting
from models.Frame import Frame
from models.Spot import Spot
from models.Camera import Camera

class TestRoomModel(unittest.TestCase):

    def setUp(self):
        with open('input.json') as json_file:
            try:
                input = json.load(json_file)
            except json.JSONDecodeError as exc:
                print(exc)

        self.room = Room(input['room'])

    def test_room_fields(self):
        """
        Room fields should equal input
        """
        self.assertEqual(self.room.name, 'Sala de Lapso')
        self.assertEqual(self.room.depth, 12.1, 'Room depth should equal input room depth')
        self.assertEqual(self.room.width, 7.1)
        self.assertEqual(self.room.height, 3.0)
        self.assertEqual(self.room.wall_thickness, 0.15)

    def test_door_fields(self):
        """
        Door fields should equal input
        """
        self.assertEqual(self.room.door.position, 3)
        self.assertEqual(self.room.door.halfDepth, -2.5)
        self.assertEqual(self.room.door.width, 1.2)
        self.assertEqual(self.room.door.height, 2.2)
        self.assertEqual(self.room.door.frame.x, 0.08)
        self.assertEqual(self.room.door.frame.y, 0.03)

    def test_skirting_fields(self):
        """
        Skirting thickness should equal input
        Skirting  height should equal input + wall_thickness
        """
        self.assertEqual(self.room.skirting.thickness, 0.025)
        self.assertEqual(self.room.skirting.height, 0.12+self.room.wall_thickness)

    def test_speaker_fields(self):
        """
        Speaker fields should equal input
        """
        self.assertEqual(self.room.speaker.x, 2)
        self.assertEqual(self.room.speaker.y, 0)
        self.assertEqual(self.room.speaker.z, 0)
        self.assertEqual(self.room.speaker.rotation,0)

    def test_spot_fields(self):
        """
        Spot fields should equal input
        """
        self.assertEqual(self.room.spot.x, -5)
        self.assertEqual(self.room.spot.y, 1)
        self.assertEqual(self.room.spot.z, 2)
        self.assertEqual(self.room.spot.rotX, 50)
        self.assertEqual(self.room.spot.rotY, -60)
        self.assertEqual(self.room.spot.rotZ, 0)

    def test_camera_fields(self):
        """
        Camera fields should equal input
        """
        self.assertEqual(self.room.camera.x, -3)
        self.assertEqual(self.room.camera.y, 0)
        self.assertEqual(self.room.camera.z, 1.5)
        self.assertEqual(self.room.camera.rotation, -90)

    def test_room_camera(self):
        self.assertIsInstance(self.room.camera, Camera)

    def test_spot_camera(self):
        self.assertIsInstance(self.room.spot, Spot)

    def test_room_elements(self):
        """
        Room elements should be skirting, speaker and door
        """
        self.assertIsInstance(self.room.door, Door)
        self.assertIsInstance(self.room.speaker, Speaker)
        self.assertIsInstance(self.room.skirting, Skirting)

    def test_door_element(self):
        """
        Frame element should belong to door 
        """
        self.assertIsInstance(self.room.door.frame, Frame)

    def test_spot_element(self):
        """
        Test Spot element
        """
        self.assertIsInstance(self.room.spot, Spot)

if __name__ == '__main__':
    unittest.main()

