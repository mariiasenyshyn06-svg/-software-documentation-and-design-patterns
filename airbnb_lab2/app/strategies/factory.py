from .console_strategy import ConsoleStrategy
from .file_strategy import FileStrategy
from .kafka_strategy import KafkaStrategy
from .redis_strategy import RedisStrategy

def get_strategy(strategy_name):
    if strategy_name == "console":
        return ConsoleStrategy()
    elif strategy_name == "file":
        return FileStrategy()
    elif strategy_name == "kafka":
        return KafkaStrategy()
    elif strategy_name == "redis":
        return RedisStrategy()
    else:
        raise ValueError("Unknown strategy")