# The unit test framework uses classes and inheritance so to create
#tests we will create a class that inherits from the testcase class in the
#framework and then we write methods inside that class for the actual tests.
import unittest
import boggle

#Create a class that inherits from testcase
class TestBoggle (unittest.TestCase):

#create a method beginning with test_ which is the convention for Python tests.

    def test_can_create_an_empty_grid(self):
        
        grid = boggle.make_grid(0,0)
        #Here we use the method assertequal which is one of many methods inherited from the testcase class.
        self.assertEquals(len(grid),0)
        
    def test_grid_size_is_width_times_height(self):
        # test is to ensure that the total size of the grid is equal to width*heught
        grid = boggle.make_grid(2,3)
        
        self.assertEquals(len(grid),6)
        
        
    def test_grid_coordinates(self):
        # test to ensure that all of the coordinates inside of the grid can be accessed
        grid = boggle.make_grid(2,2)
        # We use the assertin method to check whether zero zero is an a 2x2 grid.
        self.assertIn((0,1), grid)
        self.assertIn((1,0), grid)
        self.assertIn((1,1), grid)
        self.assertIn((0,1), grid)
        #The assertNotIn method is used to check that 2,2 is not in a 2x2 grid.
        self.assertNotIn((2,2), grid)