from .defs import available_moves


def search(cube, depth, last_move=None):
	if depth == 0:
		if cube == 1:
			return True
	else:
		for move in available_moves[last_move]:
			search(cube, depth - 1, move)
	return False