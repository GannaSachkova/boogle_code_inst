# The unit test framework uses classes and inheritance so to create
#tests we will create a class that inherits from the testcase class in the
#framework and then we write methods inside that class for the actual tests.
import unittest
import boggle
from string import ascii_uppercase


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
        
        
    #The test will then assert that every letter in the grid is an uppercase letter.
    def test_grid_is_filled_with_letters(self):
        #ensure that each of th e coordinates in the grid contains letters
        grid=boggle.make_grid(2,3)
        for letter in grid.values():
            self.assertIn(letter, ascii_uppercase)
            
            
    def test_neighbours_of_a_position(self):

        #Ensure that a position has 8 neighbours
        coords = (1, 2)
        neighbors = boggle.neighbors_of_position(coords)

        self.assertIn((0, 1), neighbors)
        self.assertIn((0, 2), neighbors)
        self.assertIn((0, 3), neighbors)
        self.assertIn((1, 1), neighbors)
        self.assertIn((1, 3), neighbors)
        self.assertIn((2, 1), neighbors)
        self.assertIn((2, 2), neighbors)
        self.assertIn((2, 3), neighbors)
   
   
       
def test_all_grid_neighbors(self):
    # ensure that all of the grid position have neighbors
    grid =  boggle.make_grid(2,2)
    neighbors = boggle.all_grid_neighbors(grid)
    #this line can assert the correct length of the neighbors dictionary
    self.assertEquals(len(neighbors), len(grid))
    #for loop will iterate through the positions in the grid 
    
    for pos in grid:
        #for each position the neighbors are the other three positions on the grid 
        #so we create the others list which is a full grid 'MINUS" the positioning question 
        #then in the next line it asserts that the positions are the neighbors of the position being checked 
        others = list(grid)
        others.remove(pos)
        self.asserListEqual(sorted(neighbors[pos]), sorted(others))
    
    
def test_converting_a_path_to_a_word(self):
    #ensure that paths can be converted to words
    grid = boggle.make_grid(2,2)
    oneLetterWord = boggle.path_to_word(grid, [(0.0)])
    twoLetterWord = boggle.path_to_word(grid, [(0.0),(1,1)])
    
    self.assertEquals(oneLetterWord, grid[(0,0)])
    self.assertEquals(twoLetterWord, grid[(0,0)] + grid [(1,1)])
    
    
def test_search_grid_for_words(self):
    # Ensure that certain patterns can be found in a `path_to_word`

        grid = {(0, 0): 'A', (0, 1): 'B', (1, 0): 'C', (1, 1): 'D'}
        twoLetterWord = 'AB'
        threeLetterWord = 'ABC'
        notThereWord = 'EEE'
        dictionary = [twoLetterWord, threeLetterWord, notThereWord]


        foundWords = boggle.search(grid, dictionary)

        self.assertTrue(twoLetterWord in foundWords)
        self.assertTrue(threeLetterWord in foundWords)
        self.assertTrue(notThereWord not in foundWords)

    

def test_load_dictionary(self):
        # Test that the `get_dictionary` function returns a dictionary that has a length greater than 0

        dictionary = boggle.get_dictionary('words.txt')

        self.assertGreater(len(dictionary), 0)