# def make_grid (width, height):
#     # make an empty boggle grid
#     return {}



 # this function is for test_grid_coordinates function from test_boggle.py 
 
# def make_grid (width, height):
#     # create a grid that will hold allof the tiles for a boggle game
#     return {(row,col): " " for row in range (height)
#         for col in range (width)}


 # we are modifyed above function for  function #4 test_grid_is_filled_with_letters  from test_boggle.py 
 # and added import
from string import ascii_uppercase
from random import choice


def make_grid (width, height):
    # create a grid that will hold allof the tiles for a boggle game
    return {(row,col): choice(ascii_uppercase) 
        for row in range (height)
        for col in range (width)}
        
        

def neighbors_of_position(coords):

    """
    Get neighbours of a given position
    """

    row = coords[0]
    col = coords[1]

    # Assign each of the neighbours
    # Top-left to top-right

    top_left = (row - 1, col - 1)
    top_center = (row - 1, col)
    top_right = (row - 1, col + 1)

    # Left to right
    left = (row, col - 1)

    # The `(row, col)` coordinates passed to this function are situated here
    right = (row, col + 1)

    # Bottom-left to bottom-right
    bottom_left = (row + 1, col -1)
    bottom_center = (row + 1, col)
    bottom_right = (row + 1, col + 1)

    return [top_left, top_center, top_right, left, right,bottom_left, bottom_center, bottom_right]    


    
def all_grid_neighbors(grid):
    #get all of the poossible neighbors for each position in the grid
    neighbors = {}
    for position in grid:
        position_neighbors = neighbors_of_position(position)
        neighbors[position] = [p for p in position_neighbors if p in grid]
        return neighbors
    
    
def path_to_word(grid,path):
    #add all of the letters on the path to a string
    return ''.join([grid[p] for p in path])
    
    
    
def search(grid, dictionary):
    # Search thrugh the paths to locate words by matching strings to words in a dictionary
    neighbors = all_grid_neighbors(grid)
    paths = []



    def do_search(path):
        word = path_to_word(grid, path)
        if word in dictionary:
            paths.append(path)

        for next_pos in neighbors[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])

    for position in grid:
        do_search([position])

    words = []

    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words)



def get_dictionary(dictionary_file):
  # Load dictionary file

    with open(dictionary_file) as f:
        return [w.strip().upper() for w in f]
        
        
def main():
   # This is the function that will run the whole project

    grid = make_grid(3, 3)
    dictionary = get_dictionary('words.txt')
    words = search(grid, dictionary)

    for word in words:
        print(word)
    print("Found %s words" % len(words))



if __name__ == "__main__":
    main()