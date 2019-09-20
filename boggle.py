# def make_grid (width, height):
#     # make an empty boggle grid
#     return {}



        
def make_grid (width, height):
    # create a grid that will hold allof the tiles for a boggle game
    return {(row,col): " " for row in range (height)
        for col in range (width)}
