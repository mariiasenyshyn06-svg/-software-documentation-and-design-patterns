class ConsoleStrategy:
    def output(self, data):
        print("=== TOP INCIDENTS ===")
        for item in data:
            print(item)