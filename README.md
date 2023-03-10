# Langton-ant
A self implementation of the cellular automaton named the Langton-ant.

#### Inside function :

 * EtapeFourmiBD: Function to update the state of the ant and of the plate. The rule applied by this function is if the ant is on a white cell (equal	to 0) then this cell turn to black (equal to 1), the ant turn on herself 	at 90° to the right and advance one square. Otherwise, if the ant is on a black cell, this on turn to white, the ant turn on herself at 90° to the left and advance one square.
 
 * EtapeFourmiBG: Function to update the state of the ant and of the plate.	The rule applied by this function is if the ant is on a white cell (equal	to 0) then this cell turn to black (equal to 1), the ant turn on herself	at 90° to the left and advance one square. Otherwise, if the ant is on a	black cell, this on turn to white, the ant turn on herself at 90° to the right and advance one square.
 
 * Plot_state: Function to plot the sate of the plate and of the ant.
 
 * Plot_BW_rate: .
 
 * FourmiDeLangton: Function to create and make evolve a Langton ant model.
 
 
