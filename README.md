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






## Performance 💻

we tested different cases and brought an output conclusion. the copyable version is in the Page's Wiki: 
https://github.com/BenZeltser/OOP_Pokemon/wiki


