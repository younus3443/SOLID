class DataAnalyzer:
    def __init__(self, col1, col2, key_col):
        self.col1 = col1
        self.col2 = col2
        self.key_col = key_col

    def find_min_diff(self, data):
        min_diff = float('inf')
        min_key = None
        for row in data:
            try:
                diff = abs(int(row[self.col1]) - int(row[self.col2]))
                if diff < min_diff:
                    min_diff = diff
                    min_key = row[self.key_col]
            except ValueError:
                continue
        return min_key, min_diff
