class DataExtractor:

    def __init__(self, filepath, skip_lines=0):
        self.filepath = filepath
        self.skip_lines = skip_lines

    def extract(self, columns):
        data = []
        with open(self.filepath) as file:
            lines = file.readlines()[self.skip_lines:]
            for line in lines:
                parts = line.split()
                if len(parts) < len(columns):
                    continue
                row = {col: parts[i] for i, col in enumerate(columns)}
                data.append(row)
            return data
