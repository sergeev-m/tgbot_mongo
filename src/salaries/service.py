from src.salaries.schemas import RequestData, AvgResponse
from src.salaries.repozitory import salaries_repozitory, SalaryRepozitory


class SalaryService:
    def __init__(self, repozitory: SalaryRepozitory):
        self.repozitory = repozitory

    async def avg_by_date(self, data: RequestData) -> dict:
        res = AvgResponse(** await self.repozitory.avg_by_date(data.model_dump()))
        return res.model_dump()


salary_service = SalaryService(salaries_repozitory)
