from collections import defaultdict

class ShootingService:

    def filter_by_borough(self, data, borough):
        if borough == "ALL":
            return data
        return [item for item in data if item["borough"] == borough]

    def top_dangerous(self, data):
        stats = defaultdict(int)

        for item in data:
            stats[item["borough"]] += item["count"]

        result = [
            {"borough": k, "count": v}
            for k, v in stats.items()
        ]

        result.sort(key=lambda x: x["count"], reverse=True)

        return result[:5]