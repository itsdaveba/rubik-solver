import random
from enum import IntEnum

N_MOVE = 18
N_MOVE_PER_FACE = 3

class Move(IntEnum):
	U1 = 0
	U2 = 1
	U3 = 2
	R1 = 3
	R2 = 4
	R3 = 5
	F1 = 6
	F2 = 7
	F3 = 8
	D1 = 9
	D2 = 10
	D3 = 11
	L1 = 12
	L2 = 13
	L3 = 14
	B1 = 15
	B2 = 16
	B3 = 17

def generate_random_scramble(num_moves):
	scramble = []
	last_move = None
	for _ in range(num_moves):
		if last_move is None:
			move = random.randrange(N_MOVE)
		else:
			face = last_move // N_MOVE_PER_FACE
			first_range = (face % N_MOVE_PER_FACE) * N_MOVE_PER_FACE
			if last_move < Move.D1:
				second_range = first_range
			else:
				second_range = face * N_MOVE_PER_FACE
			move = random.choice(
				list(range(0, first_range)) + \
				list(range(first_range + N_MOVE_PER_FACE, second_range)) + \
				list(range(second_range + N_MOVE_PER_FACE, N_MOVE)))
		scramble.append(Move(move).name)
		last_move = move
	return ' '.join(scramble).replace('1', '').replace('3', "'")