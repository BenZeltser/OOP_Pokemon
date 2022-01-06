from unittest import TestCase

from src import DiGraph

class TestDiGraph(TestCase):


    def testPre(self):
        myGraph = DiGraph.DiGraph()
        print("Test0")
        myGraph.add_node(0)
        myGraph.add_node(1)
        myGraph.add_node(2)
        myGraph.add_node(3)
        myGraph.add_node(4)
        myGraph.add_node(5)

        myGraph.add_edge(0,1,1)
        myGraph.add_edge(2, 1, 3)


    def test_v_size(self):
        myGraph = DiGraph.DiGraph()
        n = myGraph.v_size()
        self.assertEqual(n, 0, "Empty Graph")

    def test_e_size(self):
        myGraph = DiGraph()
        e = myGraph.e_size()
        self.assertEqual(e, 0, "Empty Graph")
        print("Test2")


    def test_add_edges(self):
        myGraph = DiGraph.DiGraph()
        myGraph.add_edge(1, 2, 6)
        boolTest = False
        for edge in myGraph.all_out_edges_of_node(1):
            if edge == 2:
                boolTest = True
        self.assertTrue(boolTest)
        print("Test3")

    def test_add_node(self):
        myGraph = DiGraph()
        myGraph.add_node(1)
        self.assertEqual(myGraph.v_size(), 1, "One Node Graph ")
        print("Test4")

    def test_to_dictionary(self):
        myGraph = DiGraph
        c = myGraph.DiGraph.to_dictionary()
        a:dict
        self.assertEqual(a,c,"Empty Dict" )
        print("Test5")