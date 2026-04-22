from app.reader.data_reader import DataReader
from app.services.shooting_service import ShootingService
from app.strategies.factory import get_strategy
import json

with open("app/config/strategy_config.json") as f:
    config = json.load(f)

reader = DataReader()
data = reader.read("data/shootings.csv")

service = ShootingService()

filtered = service.filter_by_borough(data, config["borough"])
top = service.top_dangerous(filtered)

strategy = get_strategy(config["output"])
strategy.output(top)