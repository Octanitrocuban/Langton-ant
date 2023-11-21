# -*- coding: utf-8 -*-
"""
module containing function to create show and analyse the Langton ant
algorithm.
"""
import numpy as np
import matplotlib.pyplot as plt
#=============================================================================
def white_right_step(array, x, y, look):
	"""
	Function to update the state of the ant and of the plate.
	The rule applied by this function is if the ant is on a white cell (equal
	to 0) then this cell turn to black (equal to 1), the ant turn on herself
	at 90° to the right and advance one square. Otherwise, if the ant is on a
	black cell, this on turn to white, the ant turn on herself at 90° to the
	left and advance one square.

	Parameters
	----------
	array : numpy.ndarray
		The 2d matrix on which the ant walk.
	x : int
		The x position of the ant.
	y : int
		The y position of the ant.
	look : str
		The direction at which the ant look. It can take the value:
		('N':North, 'E':East, 'S':South or 'O':West).

	Returns
	-------
	array : numpy.ndarray
		The new state of the 2d matrix on which the ant walk.
	x : int
		The new x position of the ant.
	y : int
		The new y position of the ant.
	look : str
		The new direction in which the ant look.

	Example
	-------
	In [0] : _, x, y, look
	Out [0]: (array([[0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0]]),
			  3,
			  3,
			  'N')
	In [1] : white_right_step(_, x, y, look)
	0ut [1]: (array([[0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 1, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0]]),
			  3,
			  4,
			  'E')

	"""
	if array[x, y] == 0:
		array[x, y] = 1
		if look == "N":
			look, y = "E", y+1
		elif look == "S":
			look, y = "O", y-1
		elif look == "E":
			look, x = "S", x+1
		elif look == "O":
			look, x = "N", x-1

	elif array[x, y] == 1:
		array[x, y] = 0
		if look == "N":
			look, y = "O", y-1
		elif look == "S":
			look, y = "E", y+1
		elif look == "E":
			look, x = "N", x-1
		elif look == "O":
			look, x = "S", x+1

	return array, x, y, look

def white_left_step(array, x, y, look):
	"""
	Function to update the state of the ant and of the plate.
	The rule applied by this function is if the ant is on a white cell (equal
	to 0) then this cell turn to black (equal to 1), the ant turn on herself
	at 90° to the left and advance one square. Otherwise, if the ant is on a
	black cell, this on turn to white, the ant turn on herself at 90° to the
	right and advance one square.

	Parameters
	----------
	array : numpy.ndarray
		The 2d matrix on which the ant walk.
	x : int
		The x position of the ant.
	y : int
		The y position of the ant.
	look : str
		The direction at which the ant look. It can take the value:
		('N':North, 'E':East, 'S':South or 'O':West).

	Returns
	-------
	array : numpy.ndarray
		The new state of the 2d matrix on which the ant walk.
	x : int
		The new x position of the ant.
	y : int
		The new y position of the ant.
	look : str
		The new direction in which the ant look.

	Example
	-------
	In [0] : _, x, y, look
	Out [0]: (array([[0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0]]),
			  3,
			  3,
			  'N')
	In [1] : white_left_step(_, x, y, look)
	0ut [1]: (array([[0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 1, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0]]),
			  3,
			  2,
			  'O')

	"""
	if array[x, y] == 0:
		array[x, y] = 1
		if look == "N":
			look, y = "O", y-1
		elif look == "S":
			look, y = "E", y+1
		elif look == "E":
			look, x = "N", x-1
		elif look == "O":
			look, x = "S", x+1

	elif array[x, y] == 1:
		array[x, y] = 0
		if look == "N":
			look, y = "E", y+1
		elif look == "S":
			look, y = "O", y-1
		elif look == "E":
			look, x = "S", x+1
		elif look == "O":
			look, x = "N", x-1

	return array, x, y, look

def plot_state(board, x, y, look, step, figsz):
	"""
	Function to plot the sate of the board and of the ant.

	Parameters
	----------
	board : numpy.ndarray
		The plate (a square matrix) on which the ant walk and is modified by
		her depending the applied rule.
	x : int
		The x position of the ant on the plate.
	y : int
		The y position of the ant on the plate.
	look : str
		Direction in which the ant looks.
	step : int
		The number of the current iteration.
	figsz : float
		Figure size of the plot.

	Returns
	-------
	None.

	Example
	-------
	In [0] : board, x, y, look, step, figsz
	Out [0]: (array([[0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0]]),
			  3, 3, 'N', 0, 11.5)
	In [1] : plot_state(board, x, y, look, step, figsz):
	Out [1]: matplotlib.figure.Figure

	"""
	plt.figure(figsize=(figsz, figsz))
	plt.title("Step : "+str(step)+" ; orientation : "+look)
	plt.imshow(board, cmap="binary")
	if look == 'N':
		plt.plot(y, x, 'r^', label=str(x)+" ; "+str(y))
	elif look == 'E':
		plt.plot(y, x, 'r>', label=str(x)+" ; "+str(y))
	elif look == 'O':
		plt.plot(y, x, 'r<', label=str(x)+" ; "+str(y))
	elif look == 'S':
		plt.plot(y, x, 'rv', label=str(x)+" ; "+str(y))

	plt.legend()
	plt.show()

def plot_black_white_rate(history, figsz):
	"""
	Function to plot the evolution of the filling of the plate by cells equal
	to 0 or to 1.

	Parameters
	----------
	history : numpy.ndarray
		A numpy.ndarray storring the all the step of the evolution of the
		Langton ant's.

	Returns
	-------
	None.

	Example
	-------
	In [0] : h, fs
	Out [0]: (array([[10, 10, 'N', 1.0, 0.0],
					 [10, 11, 'E', 0.9975, 0.0025],
					 [11, 11, 'S', 0.995, 0.005],
					 [11, 10, 'O', 0.9925, 0.0075],
					 [10, 10, 'N', 0.99, 0.01],
					 [10, 9, 'O', 0.9925, 0.0075],
					 [9, 9, 'N', 0.99, 0.01],
					 [9, 10, 'E', 0.9875, 0.0125],
					 [10, 10, 'S', 0.985, 0.015],
					 [10, 9, 'O', 0.9825, 0.0175],
					 [11, 9, 'S', 0.985, 0.015]], dtype=object),
			  6)
	In [1] : plot_black_white_rate(h, a, fs)
	Out [1]: matplotlib.pyplot image

	"""
	steps = np.arange(len(history))
	plt.figure(figsize=(figsz*2, figsz))
	plt.plot(steps, history[:, 3], label='cell 0')
	plt.plot(steps, history[:, 4], label='cell 1')
	plt.legend(title='Proportion of the\nplate filled by:')
	plt.show()

def hist_visit_cells(history, arrete, figsz):
	"""
	Function to show the frenquentation of the cells of the plate.

	Parameters
	----------
	history : numpy.ndarray
		History of the evolution of the state of the ant.
	arrete : int
		Length os the plate which is a 2d square matrix.
	figsz : int
		Figure size of the plot.

	Returns
	-------
	dense_map : numpy.ndarray
		A 2d histogram which counts the number of time that each cell were
		visited by the ant.

	Example
	-------
	In [0] : h, a, fs
	Out [0]: (array([[10, 10, 'N', 1.0, 0.0],
					 [10, 11, 'E', 0.9975, 0.0025],
					 [11, 11, 'S', 0.995, 0.005],
					 [11, 10, 'O', 0.9925, 0.0075],
					 [10, 10, 'N', 0.99, 0.01],
					 [10, 9, 'O', 0.9925, 0.0075],
					 [9, 9, 'N', 0.99, 0.01],
					 [9, 10, 'E', 0.9875, 0.0125],
					 [10, 10, 'S', 0.985, 0.015],
					 [10, 9, 'O', 0.9825, 0.0175],
					 [11, 9, 'S', 0.985, 0.015]], dtype=object),
			  10,
			  6)
	In [1] : hist_visit_cells(h, a, fs)
	Out [1]: (matplotlib.pyplot image,
			  array([[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
					 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
					 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
					 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
					 [0. 0. 0. 0. 1. 1. 0. 0. 0. 0.]
					 [0. 0. 0. 0. 2. 3. 1. 0. 0. 0.]
					 [0. 0. 0. 0. 1. 1. 1. 0. 0. 0.]
					 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
					 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
					 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]))

	"""
	dense_map = np.zeros((arrete, arrete))
	values, counts = np.unique(history[:, :2].astype(int), axis=0,
							   return_counts=True)

	for i in range(len(values)):
		dense_map[values[i, 0], values[i, 1]] = counts[i]

	plt.figure(figsize=(figsz, figsz))
	plt.title('Histogram')
	plt.imshow(dense_map, cmap='jet', interpolation='Nearest')
	plt.colorbar(shrink=0.7, pad=0.01, label='Number of exploration')
	plt.show()

	return dense_map

def hist_looks(history):
	"""
	Function to plot the distribution of the direction in which the ant have
	looked during the evolution.

	Parameters
	----------
	history : numpy.ndarray
		History of the evolution of the state of the ant.

	Returns
	-------
	None.

	Example
	-------
	In [0] : h, fs
	Out [0]: (array([[10, 10, 'N', 1.0, 0.0],
					 [10, 11, 'E', 0.9975, 0.0025],
					 [11, 11, 'S', 0.995, 0.005],
					 [11, 10, 'O', 0.9925, 0.0075],
					 [10, 10, 'N', 0.99, 0.01],
					 [10, 9, 'O', 0.9925, 0.0075],
					 [9, 9, 'N', 0.99, 0.01],
					 [9, 10, 'E', 0.9875, 0.0125],
					 [10, 10, 'S', 0.985, 0.015],
					 [10, 9, 'O', 0.9825, 0.0175],
					 [11, 9, 'S', 0.985, 0.015]], dtype=object),
			  6)
	In [1] : hist_looks(h, a, fs)
	Out [1]: matplotlib.pyplot image

	"""
	values, counts = np.unique(history[:, 2], return_counts=True)

	plt.figure()
	plt.vlines(range(4), 0, counts, lw=6)
	plt.ylabel('count')
	plt.xlabel('Looks directions')
	plt.xticks(range(4), values)
	plt.show()

def langton_ant(modele, arrete, steps, start_color='white', look='N',
					origin=None, fill='0', trap=False, figsz=6, plot=True,
					walk=1):
	"""
	Function to create and make evolve a Langton ant model.

	Parameters
	----------
	modele : str
		It is the applied rule to uptdate the satate of the ant and of the
		plate. There are two possible choice: 'white_right' or 'white_left'.
	arrete : int
		Length of the square matrix on which the ant will walk.
	steps : int
		Number of iteration during which the ant will be walking on the plate.
		It have to be in the range [0, +inf[. Note that the iteration is quite
		fast, but with a great number of steps (> 100 000) the computation
		will take some time.
	start_color : str, optional
		Color of the cell on which the ant will start. It can be either
		'white' (equal to 0) or 'black' (equal to 1). The default is 'white'.
	look : str, optional
		Direction in which the ant look at the start. The default is 'N'.
	origin: list, optional
		Starting x and y position of the ant. These position have to be ints.
		If it is equal to None, then the starting position of the ant will be
		define as follow: x, y = [arrete//2, arrete//2]. The default is None.
	fill: str, optional
		Color that originally fill the plate. If it is equal to '0' then the
		plate will be filled with 0 (at the exception of the starting position
		of the ant if start_color='black'). If it is equal to '1' then the
		plate will be filled with 1 (at the exception of the starting position
		of the ant if start_color='white'). Lastly, if it is equal to 'rand'
		then the plante will be randomly filled with 0 and 1 by using
		numpy.random.randint (at the exception of the starting position
		of the ant where start_color may re-define the color of this cell).
	trap : bool, optional
		If True then the ant is in torroid space (as in game paccman). If
		False then the loop will be break if the ant reach a shelf edge. The
		default is False.
	figsz : float, optional
		Figure size of the plot showing the state of the plate and of the ant.
		The default is 6.
	plot : bool, optional
		If True the plot of the state will be done when (i%walk) == 0. The
		default is True.
	walk : int, optional
		Reverse refresh rate of status display. This mean that higher it will
		be, lower will be the refresh rate. IMPORTANT: lower the refresh rate
		does not mean that the plot will be longer to be done, it mean that
		the plot will be done every walk-th cycle iteration. Also note that a
		high number of plot stacked in the interface product a memory leakage.
		The default is 1.

	Returns
	-------
	history : numpy.ndarray
		Historic variation of the position of the ant, the direction of her
		look, and the ratio of 0 and 1 cells value.

	Example
	-------
	# The following example will show you the construction of the higway, but
	# the ouput is to big to be show here
	In [0] : langton_ant('white_right', 400, 15000, walk=1000)

	In [1] : langton_ant('white_right', 10, 10)
	Out [1]: array([[10, 10, 'N', 1.0, 0.0],
					[10, 11, 'E', 0.9975, 0.0025],
					[11, 11, 'S', 0.995, 0.005],
					[11, 10, 'O', 0.9925, 0.0075],
					[10, 10, 'N', 0.99, 0.01],
					[10, 9, 'O', 0.9925, 0.0075],
					[9, 9, 'N', 0.99, 0.01],
					[9, 10, 'E', 0.9875, 0.0125],
					[10, 10, 'S', 0.985, 0.015],
					[10, 9, 'O', 0.9825, 0.0175],
					[11, 9, 'S', 0.985, 0.015]], dtype=object)

	"""
	if fill == '0':
		plateau = np.zeros((arrete, arrete), dtype=int)
	elif fill == '1':
		plateau = np.ones((arrete, arrete), dtype=int)
	elif fill == 'rand':
		plateau = np.random.randint(0, 2, (arrete, arrete))
	
	if type(origin) == type(None):
		x, y = [arrete//2, arrete//2]
	elif type(origin) == list:
		x, y = [origin[0]%arrete, origin[1]%arrete]

	length = np.size(plateau)
	if start_color == 'black':
		plateau[x, y] = 1
	elif start_color == 'white':
		plateau[x, y] = 0

	# Proportion of the plate fill by 0 and 1 value
	white_r = len(plateau[plateau == 0])/length
	black_r  = len(plateau[plateau == 1])/length
	history = [[x, y, look, white_r, black_r]]
	if modele == "white_right":
		for i in range(steps):
			# updating the state
			plateau, x, y, look = white_right_step(plateau, x, y, look)
			white_r = len(plateau[plateau == 0])/length
			black_r  = len(plateau[plateau == 1])/length

			if trap:
				x = x%arrete
				y = y%arrete
			else:
				if (x < 0)|(y < 0)|(x >= arrete)|(y >= arrete):
					print("The ant ant is out of frame.")
					break

			history.append([x, y, look, white_r, black_r])
			if plot == True:
				if (i%walk) == 0:
					plot_state(plateau, x, y, look, i+1, figsz)

	elif modele == "white_left":
		for i in range(steps):
			# updating the state
			plateau, x, y, look = white_left_step(plateau, x, y, look)
			white_r = len(plateau[plateau == 0])/length
			black_r  = len(plateau[plateau == 1])/length

			if trap:
				x = x%arrete
				y = y%arrete
			else:
				if (x < 0)|(y < 0)|(x >= arrete)|(y >= arrete):
					print("The ant ant is out of frame.")
					break

			history.append([x, y, look, white_r, black_r])
			if plot == True:
				if (i%walk) == 0:
					plot_state(plateau, x, y, look, i+1, figsz)

	history = np.array(history, dtype=object)
	if plot:
		plot_state(plateau, x%arrete, y%arrete, look, i, figsz)
		plot_black_white_rate(history, figsz)
		hist_visit_cells(history, arrete, figsz)
		hist_looks(history)

	return history
