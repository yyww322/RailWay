# -*- coding: utf-8 -*-
#
# @author CoolYan

import random
import sys


class GameMap(object):
    
    MAX_MAP_SIZE = 100

    def __init__(self, rows, cols):
        """Inits GameMap with row and column count."""
        assert isinstance(rows, int)
        assert isinstance(cols, int)
        assert 0 < rows <= self.MAX_MAP_SIZE
        assert 0 < cols <= self.MAX_MAP_SIZE
        self.size = (rows, cols, )
        self.__rows = rows
        self.__cols = cols
        self.cells = [[0 for col in range(cols)] for row in range(rows)]

    @property
    def rows(self):
        return self.__rows
        pass

    @rows.setter
    def rows(self, value):
        self.__rows = value

    @property
    def cols(self):
        return self.__cols
        pass

    @cols.setter
    def cols(self, value):
        self.__cols = value

    def reset(self, possibility=0.5):
        """Reset the map with random data.

        Args:
            possibility: possibility of life cell
        """
        assert isinstance(possibility, float)
        assert 0 < possibility < 1.0
        for row in range(self.rows):
            for col in range(self.cols):
                check = random.random()
                if check > possibility:
                    """
                        The possibility means living, bigger num equal more alive creature.
                    """
                    self.cells[row][col] = 0
                else:
                    self.cells[row][col] = 1
        pass

    def set(self, row, col, val):
        """Set specific cell in the map."""
        assert val == 0 or val == 1
        self.cells[row][col] = val
        pass

    def get_neighbor_count(self, row, col):
        """Get count of neighbors in specific cell.

        Args:
            row: row number
            col: column number

        Returns:
            Count of live neighbor cells
        """
        dir = {
            "left": [-1, 0],
            "right": [1, 0],
            "up": [0, -1],
            "down": [0, 1],
            "up_left": [-1, -1],
            "up_right": [1, -1],
            "down_left": [-1, 1],
            "down_right": [1, 1]
        }
        neighbor_count = 0
        for key in dir:
            if self.cells[(row + dir[key][0]) % self.rows][(col + dir[key][1]) % self.cols] == 1:
                neighbor_count += 1
        return neighbor_count
        pass


    def get_neighbor_count_map(self):
        """Get count of neighbors of every cell in the map.
        Returns:
            A grid contains every cell's neighbor count.
        """
        return [[self.get_neighbor_count(row, col) for col in range(self.cols)] for row in range(self.rows)]

    def print_map(self, cell_maps=None, sep=' ', fd=sys.stdout):
        """Print the map to target file descriptor

        Args:
            cell_maps: mapping from cell value to a string that will be displayed.
            sep: separator between cells of the same row.
            fd: file descriptor, default standard output
        """
        if not cell_maps:
            cell_maps = ['0', '1']
        assert isinstance(cell_maps, list) or isinstance(cell_maps, dict)
        assert isinstance(sep, str)
        for row in self.cells:
            print(sep.join(map(lambda cell: cell_maps[cell], row)), file=fd)
