from .defs import available_moves

import numpy as np


MAX_DEPTH = 20

class Solver:
	def __init__(self, cube):
		self.cube = cube
		self.reset()

	def reset(self):
		self.solution = []

	def search(self, position, depth, last_move=None):
		if depth == 0:
			if np.array_equal(position['orientation'], np.zeros(20, dtype=int)) and \
			np.array_equal(position['permutation'], np.arange(20)):
				return True
		else:
			for move in available_moves[last_move]:
				if self.search(self.cube.make_move(move, position), depth - 1, move):
					self.solution.append(move)
					return True
		return False

	def solve(self, max_depth=MAX_DEPTH):
		self.reset()
		for depth in range(max_depth+1):
			if self.search(self.cube.position, depth):
				self.solution.reverse()
				return ' '.join(self.solution)
		return False