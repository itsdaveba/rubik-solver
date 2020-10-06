import rubik_solver as rs
import numpy as np
import time


start_time = time.time()

cube = rs.Cube(7)
solver = rs.Solver(cube)
print('Scramble:', cube.scramble)
print('Solution:', solver.solve())

print("--- %s seconds ---" % (time.time() - start_time))