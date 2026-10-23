
import unittest

from day23_graph_path import valid_path


class TestValidPath(unittest.TestCase):
    def test_connected_chain(self):
        self.assertTrue(valid_path(3, [[0, 1], [1, 2]], 0, 2))

    def test_disconnected_components(self):
        edges = [[0, 1], [0, 2], [3, 4], [4, 5]]
        self.assertFalse(valid_path(6, edges, 0, 5))

    def test_same_source_and_destination(self):
        self.assertTrue(valid_path(1, [], 0, 0))

    def test_cycle(self):
        edges = [[0, 1], [1, 2], [2, 0]]
        self.assertTrue(valid_path(3, edges, 0, 2))

    def test_isolated_destination(self):
        self.assertFalse(valid_path(4, [[0, 1]], 0, 3))

    def test_direct_edge(self):
        self.assertTrue(valid_path(2, [[0, 1]], 0, 1))

    def test_empty_edge_list(self):
        self.assertFalse(valid_path(3, [], 0, 2))


if __name__ == "__main__":
    unittest.main()
