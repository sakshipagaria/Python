
# Python program to search a word in a puzzle
class WordSearch:
	
	def __init__(self):
		self.Row = None
		self.Col = None
		self.dir = [[-1, 0], [1, 0], [1, 1],
			   [1, -1], [-1, -1], [-1, 1],
			   [0, 1], [0, -1]]
					
	# This function searches in all 8-direction
	# from point(row, col) in grid[][]
	def search2D(self, grid, row, col, word):
		
		# If first character of word doesn't match
		# with the given starting point in grid.
		if grid[row][col] != word[0]:
			return False
			
		# Search word in all 8 directions
		# starting from (row, col)
		for x, y in self.dir:
			
			# Initialize starting point
			# for current direction
			rd, cd = row + x, col + y
			flag = True
			
			# First character is already checked,
			# match remaining characters
			for k in range(1, len(word)):
				
				# If out of bound or not matched, break
				if (0 <= rd <self.Row and
					0 <= cd < self.Col and
					word[k] == grid[rd][cd]):
					
					# Moving in particular direction
					rd += x
					cd += y
				else:
					flag = False
					break
			
			# If all character matched, then
			# value of flag must be false	
			if flag:
				return True
		return False
		
	# Searches given word in a given matrix
	# in all 8 directions
	def patternSearch(self, grid, word):
		
		# Rows and columns in given grid
		self.Row = len(grid)
		self.Col = len(grid[0])
		
		# Consider every point as starting point
		# and search given word
		for row in range(self.Row):
			for col in range(self.Col):
				if self.search2D(grid, row, col, word):
					print("pattern found at " +
						str(row +1) + ', ' + str(col+1))
					
# Driver Code
if __name__=='__main__':
	grid = ["AWPFE",
		"XIILZ",
		"NCRAF",
	        "CEGGU",
	        "MQSTN"]
	w_search = WordSearch()
	w_search .patternSearch(grid, 'EGG')
	print('')
	w_search .patternSearch(grid, 'FUN')
