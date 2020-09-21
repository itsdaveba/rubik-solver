from context import rubik_solver

import unittest

N_SCRAMBLES = 100
N_SCRAMBLE_LENGTH = 100

class TestScrambler(unittest.TestCase):
	def test_scrambler(self):
		good_scramble = True
		for _ in range(N_SCRAMBLES):
			scramble_list = solver.generate_random_scramble(N_SCRAMBLE_LENGTH).split()
			for i in range(len(scramble_list)-1):
				if scramble_list[i][0] == scramble_list[i+1][0]:
					good_scramble = False
				if scramble_list[i][0] == 'D' and scramble_list[i+1][0] == 'U':
					good_scramble = False
				if scramble_list[i][0] == 'L' and scramble_list[i+1][0] == 'R':
					good_scramble = False
				if scramble_list[i][0] == 'B' and scramble_list[i+1][0] == 'F':
					good_scramble = False
		self.assertTrue(good_scramble)

if __name__ == "__main__":
	unittest.main()