from data_extractor import DataExtractor
from data_analyzer import DataAnalyzer


class Calculator:
    def __init__(self, filepath, columns, skip_lines, col1, col2, key_col):
        self.extractor = DataExtractor(filepath, skip_lines)
        self.analyzer = DataAnalyzer(col1, col2, key_col)
        self.columns = columns

    def execute(self):
        data = self.extractor.extract(self.columns)
        print("DEBUG: Extracted", len(data), "rows")
        result = self.analyzer.find_min_diff(data)
        return result
