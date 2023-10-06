# Q-learning-algorithm
write code to have Robby the Robot use Q-learning to learn to correctly pick up cans and avoid walls in his grid world.  

Robby has five “sensors”:  Current, North, South, East, and West.   At any time step, these each return the “value” of the respective location, where the possible values are Empty, Can, and Wall.  

Robby has five possible actions:  Move-North, Move-South, Move-East, Move-West, and Pick-Up-Can.    Note:  if Robby picks up a can, the can is then gone from the grid.  

Robby receives a reward of 10 for each can he picks up; a “reward” of −5 if he crashes into a wall (after which he immediately bounces back to the square he was in); and a reward of −1 if he tries to pick up a can in an empty square.  

Your Assignment: 

Part 1:  Write a (simple!) simulator for Robby in which he receives sensor input, can perform actions, and receives rewards.    Write a Q-learning method for Robby, using a Q-matrix, in which the rows correspond to states and the columns correspond to actions.   (We will discuss in class how to easily map sensor input to state-index in the Q-matrix.)  The Q-matrix is initialized to all zeros at the beginning of a run.  

During a run, Robby will learn over a series of N episodes, during each of which he will perform M actions.  The initial state of the grid in each episode is a random placement of cans, where each grid square has a probability of 0.5 to contain a can (and 0.5 not to contain a can).   Robby is initially placed in a random grid square.  

At each time step t during an episode, your code should do the following:
Observe Robby’s current state st
Choose an action at, using ε-greedy action selection
Perform the action
Receive reward rt (which is zero except in the cases specified above)
Observe Robby’s new state st+1
Update Qst,at=Qst,at+η(rt+γmaxa'Qst+1,a'-Qst,at) 

At the end of each episode, generate a new distribution of cans and place Robby in a random grid square to start the next episode.  (Don’t reset the Q-matrix — you will keep updating this matrix over the N episodes.    Keep track of the total reward gained per episode.  

To do a run consisting of N episodes of M steps each, use the following parameter values:

N = 5,000 ; M = 200 ; η= 0.2; γ= 0.9

For choosing actions with ε-greedy action selection, set ε = 0.1 initially, and progressively decrease it every 50 epochs or so until it reaches 0 (recall that ε denotes the probability of performing the non-optimal/non-greedy action from the current state).  After that, it stays at 0.  

Run the N episodes of learning, and plot the total sum of rewards per episode (plotting a point every 100 episodes).  This plot—let’s call it the Training Reward plot—indicates the extent to which Robby is learning to improve his cumulative reward.

After training is completed, run N test episodes using your trained Q-matrix, but with ε = 0.1 for all N episodes.  Again, regenerate a grid of randomly placed cans at the beginning of each episode and also place Robby in a random grid location.  Calculate the average over sum-of-rewards-per-episode, and the standard deviation.  For simplicity in this writeup, let’s call these values Test-Average and Test-Standard-Deviation.  These values indicate how a trained agent performs this task in new environments.    

In your report, describe the experiment, give the Training Reward plot described above (plotted every 100 episodes), and Test-Average and Test-Standard-Deviation.  

(Optional) Parts 2-5 are optional

Part 2:  Experiment with Learning Rate.  Choose 4 different values for the learning rate, , approximately evenly spaced in the range [0,1], keeping the other parameters set as in Part 1.  For each value, give the Training Reward plot (plotted every 100 episodes), and the Test-Average and Test-Standard-Deviation.  Discuss how changing the learning rate changes these results. 

Part 3: Experiment with Epsilon.   Try learning with a constant epsilon (choose a value ε in [0,1]).  Give the Training Reward plot and Test-Average and Test-Standard-Deviation. How do your results change when using a constant value of epsilon rather than a decreasing value?  Speculate on why you get these results.  

Part 4:  Experiment with negative reward for each action.   Modify your code so that a negative reward (an  “action tax”) of -0.5 is given in addition to the original rewards for each action.  Run learning and testing with the parameter values of Part 1, and give the Training Reward plot and the Test-Average and Test-Standard-Deviation.    What differences do you see from the results in Part 1?  

Part 5: Devise your own experiment, different from those of Parts 1−4 above.   This can involve a change to a parameter value, a change in the rewards, a modification of the actions or sensors, etc.    Describe your experiment and give plots or values that show the results.  Are the results what you expected?  Why or why not?  One suggestion: use a Neural Network in place of the Q-table. 
