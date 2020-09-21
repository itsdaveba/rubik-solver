import numpy as np

from .defs import Move


class Cube:
	def __init__(self, scramble=None):
		self.reset()
		if scramble is not None:
			for move in scramble.split():
				self.aply_scramble(scramble)

	def reset(self):
		self.corner_orientation = np.zeros(8, dtype=np.int)
		self.corner_permutation = np.arange(8)
		self.edge_orientation = np.zeros(12, dtype=np.int)
		self.edge_permutation = np.arange(8, 20)

	def is_solved(self):
		if self.corner_orientation == 0 and self.corner_permutation == 0 and \
		self.edge_orientation == 0 and self.edge_permutation == 0:
			return True
		return False

	def make_move(move):
		if move[0] == 'U':
			pass