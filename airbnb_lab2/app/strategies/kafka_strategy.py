from .output_strategy import OutputStrategy

class KafkaStrategy(OutputStrategy):

    def output(self, data):
        print("Sending data to Kafka...")
        print(f"Records: {len(data)}")