
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo

myGraph = GraphAlgo()
algo = GraphAlgo(myGraph)
algo.load_from_json('src/data/A1.json')
algo.save_to_json()
