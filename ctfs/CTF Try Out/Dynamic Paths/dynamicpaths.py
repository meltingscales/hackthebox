'''
    You will be given a number of t = 100 grids for the different regions you need to pass. For every map you will have the below values:
        1. The dimensions i x j of the map grid where 2 <= i, j <= 100
        2. The numbers n_i,j symbolizing the distances between the blocks where 1 <= n_i,j <= 50
    You will start at the top left element, and your goal is to reach the bottom right, while only being allowed to move down or right, minimizing the sum of the numbers you pass. Provide the minimum sum.

    Example Question:
        4 3
        2 5 1 9 2 3 9 1 3 11 7 4

    This generates the following grid:
        2 5 1
        9 2 3
        9 1 3
        11 7 4

    Example Response:
        17
    (Optimal route is 2 -> 5 -> 2 -> 1 -> 3 -> 4)
'''

sample_input = '''Test 1/100
    4 3
    2 5 1 9 2 3 9 1 3 11 7 4'''

from pprint import pprint

class InputData(object):
    def __init__(self, test_number_raw, i, j, values):
        self.test_number_high = test_number_raw.split('/')[1].strip()
        self.test_number_low = test_number_raw.split('/')[0].strip().replace('Test ', '')
        self.i = i
        self.j = j
        self.values = values

    def __repr__(self):
        return f"InputData(test_number={self.test_number_low}/{self.test_number_high}, i={self.i}, j={self.j}, values={self.values})"
    
    def generate_grid(self):
        """Generates a 2D grid from the values."""
        if len(self.values) != self.i * self.j:
            raise ValueError("The number of values does not match the grid dimensions.")
        if self.i < 2 or self.j < 2 or self.i > 100 or self.j > 100:
            raise ValueError("Grid dimensions must be between 2 and 100 inclusive.")
        if any(not (1 <= v <= 50) for v in self.values):
            raise ValueError("All values must be between 1 and 50 inclusive.")
        # Create the grid from the flat list of values
        if len(self.values) == 0:
            return []
        if self.i <= 0 or self.j <= 0:
            return []
        grid = []
        index = 0
        for _ in range(self.i):
            row = self.values[index:index + self.j]
            grid.append(row)
            index += self.j
        return grid




def parse_input(input_str) -> InputData:
    lines = input_str.strip().split('\n')        

    test_number_raw = lines[0].strip()
    n, m = map(int, lines[1].strip().split())
    values = list(map(int, lines[2].strip().split()))
    return InputData(test_number_raw, n, m, values)




if __name__ == '__main__':

    # test 1: can parse the input correctly and generate the grid
    id = parse_input(sample_input)
    assert id.test_number_low == '1'
    assert id.test_number_high == '100'
    assert id.i == 4
    assert id.j == 3
    assert id.values == [2, 5, 1, 9, 2, 3, 9, 1, 3, 11, 7, 4]

    # test 2: can generate a response
    assert id.generate_response() == 17