# Studying the Abelian Sandpile As a Self-Organising Criticality



## Intro

The project will investigate the results gained from building a heuristic sandpile model to study self-organising criticality and non-Gaussian statistics. Sandpile simulations are used to build up intuition about the behaviour of complex systems, which are systems that have many components and a lot of modelled energy flow between them. In this report, the basic Abelian Sandpile simulation will be illustrated, with graphs plotting features of avalanche events that are events where sand particles are toppled, affecting the states of the surrounding area. 

## Setup

You can run this simulation in two ways:

1. **iPython notebook**: 
    - Download the code
    - Make sure you have [Jupyter Notbook](https://jupyter.org/install) installed
    - Run the cells in **BTW Sandpile Simulation.ipynb**

2. **Command line** : run the following command to run the sandpile simulation 

<i style='color: green'> default parameters: </i>  
 M = 3, N = 3, show_step = False, time=10000, threshold=4, method='random'

` python BTW_sandpile`

<i style='color: green'>custom parameters:  </i>
    
` python  BTW_sandpile -M 3 -N 3 -show False -t 500 -th 4 -m 'center' `



