# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 21:03:19 2023

@author: Matthieu Nougaret
"""
import numpy as np
import matplotlib.pyplot as plt

def EtapeFourmiBD(Array, X, Y, look):
	"""
	Function to update the state of the ant and of the plate.
	The rule applied by this function is if the ant is on a white cell (equal
	to 0) then this cell turn to black (equal to 1), the ant turn on herself
	at 90° to the right and advance one square. Otherwise, if the ant is on a
	black cell, this on turn to white, the ant turn on herself at 90° to the
	left and advance one square.

	Parameters
	----------
	Array : numpy.ndarray
		The 2d matrix on which the ant walk.
	X : int
		The x position of the ant.
	Y : int
		The y position of the ant.
	look : str
		The direction at which the ant look. It can take the value:
		('N':North, 'E':East, 'S':South or 'O':West).

	Returns
	-------
	Array : numpy.ndarray
		The new state of the 2d matrix on which the ant walk.
	X : int
		The new x position of the ant.
	Y : int
		The new y position of the ant.
	look : str
		The new direction in which the ant look.

	Exemple
	-------
	In [0] : _, x, y, look
	Out [0] : array([[0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0]])
			 3
			 3
			 'N'
	In [1] : EtapeFourmiBD(_, x, y, look)
	0ut [1] : array([[0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 1, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0]])
			 3
			 4
			 'E'

	"""
	if Array[X, Y] == 0:
		Array[X, Y] = 1
		if look == "N":
			look, Y = "E", Y+1
		elif look == "S":
			look, Y = "O", Y-1
		elif look == "E":
			look, X = "S", X+1
		elif look == "O":
			look, X = "N", X-1

	elif Array[X, Y] == 1:
		Array[X, Y] = 0
		if look == "N":
			look, Y = "O", Y-1
		elif look == "S":
			look, Y = "E", Y+1
		elif look == "E":
			look, X = "N", X-1
		elif look == "O":
			look, X = "S", X+1

	return Array, X, Y, look

def EtapeFourmiBG(Array, X, Y, look):
	"""
	Function to update the state of the ant and of the plate.
	The rule applied by this function is if the ant is on a white cell (equal
	to 0) then this cell turn to black (equal to 1), the ant turn on herself
	at 90° to the left and advance one square. Otherwise, if the ant is on a
	black cell, this on turn to white, the ant turn on herself at 90° to the
	right and advance one square.


	Parameters
	----------
	Array : numpy.ndarray
		The 2d matrix on which the ant walk.
	X : int
		The x position of the ant.
	Y : int
		The y position of the ant.
	look : str
		The direction at which the ant look. It can take the value:
		('N':North, 'E':East, 'S':South or 'O':West).

	Returns
	-------
	Array : numpy.ndarray
		The new state of the 2d matrix on which the ant walk.
	X : int
		The new x position of the ant.
	Y : int
		The new y position of the ant.
	look : str
		The new direction in which the ant look.

	Exemple
	-------
	In [0] : _, x, y, look
	Out [0] : array([[0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0]])
			 3
			 3
			 'N'
	In [1] : EtapeFourmiBG(_, x, y, look)
	0ut [1] : array([[0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 1, 0, 0],
					 [0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0]])
			 3
			 2
			 'O'
	"""
	if Array[X, Y] == 0:
		Array[X, Y] = 1
		if look == "N":
			look, Y = "O", Y-1
		elif look == "S":
			look, Y = "E", Y+1
		elif look == "E":
			look, X = "N", X-1
		elif look == "O":
			look, X = "S", X+1

	elif Array[X, Y] == 1:
		Array[X, Y] = 0
		if look == "N":
			look, Y = "E", Y+1
		elif look == "S":
			look, Y = "O", Y-1
		elif look == "E":
			look, X = "S", X+1
		elif look == "O":
			look, X = "N", X-1

	return Array, X, Y, look

def Plot_state(Plate, X, Y, look, step, FS):
	"""
	Function to plot the sate of the plate and of the ant.

	Parameters
	----------
	Plate : numpy.ndarray
		The plate (a square matrix) on which the ant walk and is modified by
		her depending the applied rule.
	X : int
		The x position of the ant on the plate.
	Y : int
		The y position of the ant on the plate.
	look : TYPE
		Direction in which the ant looks.
	step : int
		The number of the current iteration.
	FS : float
		Figure size of the plot.

	Returns
	-------
	None.

	Exemple
	-------
	In [0] :
	Out [0] : 

	"""
	plt.figure(figsize=(FS, FS))
	plt.title("Step : "+str(step)+" ; orientation : "+look)
	plt.imshow(Plate, cmap="binary")
	if look == 'N':
		plt.plot(Y, X, 'r^', label = str(X)+" ; "+str(Y))
	elif look == 'E':
		plt.plot(Y, X, 'r>', label = str(X)+" ; "+str(Y))
	elif look == 'O':
		plt.plot(Y, X, 'r<', label = str(X)+" ; "+str(Y))
	elif look == 'S':
		plt.plot(Y, X, 'rv', label = str(X)+" ; "+str(Y))
	plt.legend()
	plt.show()

def Plot_BW_rate(History, FS):
	"""
	Function to plot the evolution of the filling of the plate by cells equal
	to 0 or to 1.

	Parameters
	----------
	History : numpy.ndarray
		A numpy.ndarray storring the all the step of the evolution of the
		Langton ant's.

	Returns
	-------
	None.

	Exemple
	-------
	In [0] : h, fs
	Out [0] : array([[10, 10, 'N', 1.0, 0.0],
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
			  6
	In [1] : HistVisitCells(h, a, fs)
	Out [1] : matplotlib.pyplot image

	"""
	Steps = np.arange(len(History))
	plt.figure(figsize=(FS*2, FS))
	plt.plot(Steps, History[:, 3], label='cell 0')
	plt.plot(Steps, History[:, 4], label='cell 1')
	plt.legend(title='Proportion of the\nplate filled by:')
	plt.show()

def HistVisitCells(History, arrete, FS):
	"""
	Function to show the frenquentation of the cells of the plate.

	Parameters
	----------
	History : numpy.ndarray
		History of the evolution of the state of the ant.
	arrete : int
		Length os the plate which is a 2d square matrix.
	FS : int
		Figure size of the plot.

	Returns
	-------
	Map : numpy.ndarray
		A 2d histogram which counts the number of time that each cell were
		visited by the ant.

	Exemple
	-------
	In [0] : h, a, fs
	Out [0] : array([[10, 10, 'N', 1.0, 0.0],
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
			  6
	In [1] : HistVisitCells(h, a, fs)
	Out [1] : matplotlib.pyplot image,
			  array([[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
					 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
					 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
					 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
					 [0. 0. 0. 0. 1. 1. 0. 0. 0. 0.]
					 [0. 0. 0. 0. 2. 3. 1. 0. 0. 0.]
					 [0. 0. 0. 0. 1. 1. 1. 0. 0. 0.]
					 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
					 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
					 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]])

	"""
	Map = np.zeros((arrete, arrete))
	values, counts = np.unique(History[:, :2].astype(int), axis=0,
							return_counts=True)
	for i in range(len(values)):
		Map[values[i, 0], values[i, 1]] = counts[i]

	plt.figure(figsize=(FS, FS))
	plt.title('Histogram')
	plt.imshow(Map, cmap='jet', interpolation='Nearest')
	plt.colorbar(shrink=0.7, pad=0.01, label='Number of exploration')
	plt.show()
	return Map

def HistLooks(History):
	"""
	Function to plot the distribution of the direction in which the ant have
	looked during the evolution.

	Parameters
	----------
	History : numpy.ndarray
		History of the evolution of the state of the ant.

	Returns
	-------
	None.

	Exemple
	-------
	In [0] : h, fs
	Out [0] : array([[10, 10, 'N', 1.0, 0.0],
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
			  6
	In [1] : HistLooks(h, a, fs)
	Out [1] : matplotlib.pyplot image

	"""
	values, counts = np.unique(History[:, 2], return_counts=True)
	plt.figure()
	plt.vlines(range(4), 0, counts, lw=6)
	plt.ylabel('count')
	plt.xlabel('Looks directions')
	plt.xticks(range(4), values)
	plt.show()

def FourmiDeLangton(modele, arrete, steps, start_color='white', look='N',
					origin=None, Fill='0', trap=False, FS=6, Plot=True,
					Walk=1):
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
	Fill: str, optional
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
	FS : float, optional
		Figure size of the plot showing the state of the plate and of the ant.
		The default is 6.
	Plot : bool, optional
		If True the plot of the state will be done when (i%Walk) == 0. The
		default is True.
	Walk : int, optional
		Reverse refresh rate of status display. This mean that higher it will
		be, lower will be the refresh rate. IMPORTANT: lower the refresh rate
		does not mean that the plot will be longer to be done, it mean that
		the plot will be done every Walk-th cycle iteration. Also note that a
		high number of plot stacked in the interface product a memory leakage.
		The default is 1.

	Returns
	-------
	History : numpy.ndarray
		Historic variation of the position of the ant, the direction of her
		look, and the ratio of 0 and 1 cells value.

	Exemple
	-------
	# The following exemple will show you the construction of the higway.
	In [0] : FourmiDeLangton('white_right', 400, 15000, Walk=1000)
	
	In [1] : FourmiDeLangton('white_right', 10, 10)
	Out [1] : array([[10, 10, 'N', 1.0, 0.0],
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
	if Fill == '0':
		plateau = np.zeros((arrete, arrete), dtype=int)
	elif Fill == '1':
		plateau = np.ones((arrete, arrete), dtype=int)
	elif Fill == 'rand':
		plateau = np.random.randint(0, 2, (arrete, arrete))
	
	if type(origin) == type(None):
		x, y = [arrete//2, arrete//2]
	elif type(origin) == list:
		x, y = [origin[0]%arrete, origin[1]%arrete]

	L = np.size(plateau)
	if start_color == 'black':
		plateau[x, y] = 1
	elif start_color == 'white':
		plateau[x, y] = 0

	# Proportion of the plate fill by 0 and 1 value
	Whites = len(plateau[plateau == 0])/L
	Blacks  = len(plateau[plateau == 1])/L
	History = [[x, y, look, Whites, Blacks]]
	if modele == "white_right":
		for i in range(steps):
			# updating the state
			plateau, x, y, look = EtapeFourmiBD(plateau, x, y, look)
			Whites = len(plateau[plateau == 0])/L
			Blacks  = len(plateau[plateau == 1])/L

			if trap:
				x = x%arrete ; y = y%arrete
			else:
				if (x < 0)|(y < 0)|(x >= arrete)|(y >= arrete):
					print("The ant ant is out of frame.")
					break

			History.append([x, y, look, Whites, Blacks])
			if Plot == True:
				if (i%Walk) == 0:
					Plot_state(plateau, x, y, look, i+1, FS)

	elif modele == "white_left":
		for i in range(steps):
			# updating the state
			plateau, x, y, look = EtapeFourmiBD(plateau, x, y, look)
			Whites = len(plateau[plateau == 0])/L
			Blacks  = len(plateau[plateau == 1])/L

			if trap:
				x = x%arrete ; y = y%arrete
			else:
				if (x < 0)|(y < 0)|(x >= arrete)|(y >= arrete):
					print("The ant ant is out of frame.")
					break

			History.append([x, y, look, Whites, Blacks])
			if Plot == True:
				if (i%Walk) == 0:
					Plot_state(plateau, x, y, look, i+1, FS)

	History = np.array(History, dtype=object)
	if Plot:
		Plot_state(plateau, x%arrete, y%arrete, look, i, FS)
		Plot_BW_rate(History, FS)
		HistVisitCells(History, arrete, FS)
		HistLooks(History)

	return History
