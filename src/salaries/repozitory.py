from datetime import timedelta
from motor.motor_asyncio import AsyncIOMotorCollection

from src.core.db.db import db
from src.core.config.db import settings_db


class SalaryRepozitory:
    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def avg_by_date(self, data: dict):
        group_type = data['group_type'].name

        projection = {
            "hour": {"format": "%Y-%m-%dT%H:00:00", 'timedelta': 3600},
            "day": {"format": "%Y-%m-%dT00:00:00", 'timedelta': 86400},
            "month": {"format": "%Y-%m-01T00:00:00"}
        }[group_type]

        match = {
            "dt": {
                "$gte": data['dt_from'],
                "$lte": data['dt_upto']
            }
        }

        project = {
                    "date": {
                        "$dateToString": {
                            "format": projection["format"],
                            "date": f"$dt"
                        }
                    },
                    "value": 1
                }

        group = {
            "_id": "$date",
            "avg_value": {
                "$sum": "$value"
            }
        }

        sort = {"_id": 1}

        pipeline = [{"$match": match}, {"$project": project}, {"$group": group}, {"$sort": sort}]
        result = await self.collection.aggregate(pipeline).to_list(None)

        if group_type == 'month':
            dataset = [item["avg_value"] for item in result]
            labels = [item["_id"] for item in result]
        else:
            start_date = data['dt_from']
            end_date = data['dt_upto']
            delta = projection['timedelta']
            date_range = [
                (start_date + timedelta(seconds=delta * x)).strftime(projection["format"])
                for x in range(0, int((end_date - start_date).total_seconds()/delta) + 1)
            ]
            aggregated_data = {item["_id"]: item['avg_value'] for item in result}
            dataset = []
            labels = []
            for date in date_range:
                dataset.append(aggregated_data.get(date, 0))
                labels.append(date)

        return {
            "dataset": dataset,
            "labels": labels
        }


salaries_repozitory = SalaryRepozitory(db.get_collection(settings_db.MONGO_COLLECTION))
