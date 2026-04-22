from .output_strategy import OutputStrategy

class RedisStrategy(OutputStrategy):

    def output(self, data):
        print("Saving data to Redis...")
        print(f"Records: {len(data)}")