from unittest import TestCase

from diGraph import DiGraph


class TestDiGraph(TestCase):


    def preTest(self):
        myGraph = DiGraph()
        print("Test0")
    def test_v_size(self):
        myGraph = DiGraph()
        n = myGraph.v_size()
        self.assertEqual(n, 0, "Empty Graph")
        print("Test1")

    def test_e_size(self):
        self.fail()

    def test_get_all_v(self):
        self.fail()

    def test_all_out_edges_of_node(self):
        self.fail()

    def test_all_in_edges_of_node(self):
        self.fail()

    def test_get_mc(self):
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
