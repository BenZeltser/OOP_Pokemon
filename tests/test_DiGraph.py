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

    def test_get_all_v(self):
        self.fail()

    def test_all_out_edges_of_node(self):
        self.fail()

    def test_all_in_edges_of_node(self):
        self.fail()

    def test_add_edges(self):
        self.fail()

    def test_add_node(self):
        self.fail()

    def test_remove_edge(self):
        self.fail()

    def test_remove_node(self):
        self.fail()

    def test_to_dictionary(self):
        self.fail()
