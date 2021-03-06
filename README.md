# OOP_Pokemon

![pokelogo](https://user-images.githubusercontent.com/92685838/148538392-61a17520-a296-4aa5-a2a0-f3e4aa73bcb9.jpg)

## Introduction 👋
This project is the final project of a 5 series projects within OOP course in Ariel University, class of 2021-2022.
on this Project we implement A pokemon game by the implementation of Graph Algorithms and Graph GUI using Python3.  

as mentioned, on this project we will write a Python program that will focus on Graph theory
by implementing the ideas the principles that we learn in the Object oriented programming course.
The program will present a Directed weighted graph using a Json file that speficies it's nodes and edges. The Objective on the project is a Pokemon themed game.

![image](https://user-images.githubusercontent.com/92685838/148546340-53000106-a2b4-470d-8364-fba1246f6738.png)


## About the Program 🗒️
on this project we will write a Python program that will focus on Graph theory
by implementing the ideas the principles that we learn in the Object oriented programming course.  

The program will present a Directed weighted graph using a Json file that speficies it's nodes and edges. The Objective on the project is a Pokemon themed game. the program will implement a Pokemon themed game.  

the game will have Pokemons and Agents. the Agents will seek to 'catch' the Pokemons by being at a proximity within the Pokemon. 
the Pokemons will be found on the edges on the Graph or near them (as far as 'Epsilon' from the edge) while epsilon being as small as we choose it while still being bigger than zero.  

Each Pokemon will have an assigned value, our goal is to allow the agent take the least amount of steps while getting the highest 'Grade' - Grade being the sum of pokemon values.

## Project Structuce 🏗️

on this segment, we will presenet the structuce of the project and how the different classes and server Intreact with each other.  

### Behind the scenes information:
 
The project is a client-side focused program that recives information from a server and retrives it's data as a Json string that that program would parse and process it's information. the Graph Object class is using a Python Dictionary to map with a one-one function between the key to it's value (e.g id to node, node to edge, etc)  

the Program implements some Algorithms that has been studied through the Semester and applies them to create a high performance Poekmon Capture. Here is a list of some of the Key functions that were used: 

##### - Graph elementary functions (add edge/node, get, set, init, size, etc)
##### - Graph to dictionary: this function makes our grapgh into dictionary so we could save it as a json
##### - GraphAlgo elementary functions (init, get, set)
##### - Load from Json: parses and proccesses the json file to a Python Object with the information accordingly.
##### - Save to Json: Essentialy the reverse of Load: Converts a Graph object to a Json file.
##### - Shortest_path_list: returns a list of the shortest path
##### - Shortest_path_distance: returns the weight of the shortest path
##### - shortest_path: returns a distance and a list of the shortest path
##### - DoubleBFS: traverses the Graph twice in a Breadth first search manner, once as the original graph, once as a transposed graph. will return the SCC of the Graph. alot of information is stacked on this specific function so we added sources for reference

BFS: https://en.wikipedia.org/wiki/Breadth-first_search  

Transpose Graph: https://en.wikipedia.org/wiki/Transpose_graph  

Strongly connected component (SCC): https://en.wikipedia.org/wiki/Strongly_connected_component

### General info on Project structuce:

the presentation will be used by a UML Diagram that will visually present the different moving parts in the program.

The Project is Following The Model View Controller (MVC) design pattern

#### MVC: https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller

### MVC Visual Explanation: (Via Youtube) 

![image](https://user-images.githubusercontent.com/92685838/148545815-4136edb9-f714-467b-ba1c-ce5f73ff1938.png)

### UML Diagram:

![image](https://user-images.githubusercontent.com/92685838/148545578-257c5092-1d9f-432d-8b0f-b8c276608187.png)


## How to play

### We have implemented the GUI by using the PyGame library within Python3

#### PyGame: https://www.pygame.org/news

### We will Explain the different 'moving parts' of the program 

![image](https://user-images.githubusercontent.com/92685838/148547653-e452f3c6-7717-4bfd-837c-8b1d2f69735b.png)

- An Agent that will catch the Pokemons. On this case, the ID is 0


![image](https://user-images.githubusercontent.com/92685838/148546737-2bbec1ee-5117-4eba-92dc-6e040d73aae5.png)

- A Node (Vertex) in the Graph, on this case with an ID of 9.

![image](https://user-images.githubusercontent.com/92685838/148546898-b85101d1-e4fa-430b-bdef-fd9b7f7e9900.png) ![image](https://user-images.githubusercontent.com/92685838/148547019-a8bd6f16-7c8e-4d4a-a07c-cb2401e2e847.png)

- A Pokemon. this is the pokemon that we need to catch as the Agents. as we can see one has an assigned value of 10, and the Red Arrow presents that it is laying on a DOWNARD Edge. the other one has an assigned value of 15 and a Green Up Arrow that presents an UPWARD edge


![image](https://user-images.githubusercontent.com/92685838/148547157-9d095cb3-0cbd-4fc4-9afa-fe6340ba516c.png) 
- A Dynamic real time changing screen that presents the Data of the game


![image](https://user-images.githubusercontent.com/92685838/148547197-3a2f365d-2a5f-45cb-8f87-58b95350bea3.png)
- The participants of the Project


![image](https://user-images.githubusercontent.com/92685838/148547222-78188b89-92b9-4ac2-8c93-31f5032f8288.png) 
- Stop button - Stops the game Gracefuly.



