from unittest import TestCase

from src.Edge import Edge


class TestEdge(TestCase):

    e = Edge(0,0,0)
    e = Edge(0, 0, 1)
    e = Edge(2, 0, 0)
    e = Edge(2, 1, 5)
    e = Edge(6, 6, 123)

    def test_get_src(self):
        e = Edge(1,1,1)
        src = e.getSRC()
        self.assertEqual(src,1,"src:1")
        print("test0")


    def test_get_dest(self):
        e = Edge(1, 1, 1)
        src = e.getDest()
        self.assertEqual(src, 1, "Dest:1")
        print("test0")

    def test_get_weight(self):
        e = Edge(1, 1, 1)
        src = e.getWeight()
        self.assertEqual(src, 1, "Weight:1")
        print("test0")
