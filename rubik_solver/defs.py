from enum import IntEnum


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


keys_values = [
[(Move.U1, Move.U2, Move.U3),
(Move.R1, Move.R2, Move.R3, Move.F1, Move.F2, Move.F3,
	Move.D1, Move.D2, Move.D3, Move.L1, Move.L2, Move.L3,
	Move.B1, Move.B2, Move.B3)],
[(Move.R1, Move.R2, Move.R3),
(Move.U1, Move.U2, Move.U3, Move.F1, Move.F2, Move.F3,
	Move.D1, Move.D2, Move.D3, Move.L1, Move.L2, Move.L3,
	Move.B1, Move.B2, Move.B3)],
[(Move.F1, Move.F2, Move.F3),
(Move.U1, Move.U2, Move.U3, Move.R1, Move.R2, Move.R3,
	Move.D1, Move.D2, Move.D3, Move.L1, Move.L2, Move.L3,
	Move.B1, Move.B2, Move.B3)],
[(Move.D1, Move.D2, Move.D3),
(Move.R1, Move.R2, Move.R3, Move.F1, Move.F2, Move.F3,
	Move.L1, Move.L2, Move.L3, Move.B1, Move.B2, Move.B3)],
[(Move.L1, Move.L2, Move.L3),
(Move.U1, Move.U2, Move.U3, Move.F1, Move.F2, Move.F3,
	Move.D1, Move.D2, Move.D3, Move.B1, Move.B2, Move.B3)],
[(Move.B1, Move.B2, Move.B3),
(Move.U1, Move.U2, Move.U3, Move.R1, Move.R2, Move.R3,
	Move.D1, Move.D2, Move.D3, Move.L1, Move.L2, Move.L3)]]

available_moves = {key: value for keys, value in keys_values for key in keys}
available_moves.update({None:
	(Move.U1, Move.U2, Move.U3, Move.R1, Move.R2, Move.R3,
		Move.F1, Move.F2, Move.F3, Move.D1, Move.D2, Move.D3,
		Move.L1, Move.L2, Move.L3, Move.B1, Move.B2, Move.B3)})