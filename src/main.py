from fastapi import FastAPI

from src.salaries.repozitory import salaries_repozitory
from src.salaries.schemas import Document, AvgResponse, RequestData


app = FastAPI()


@app.get('/', response_model=list[Document])
async def get_all():
    res = await salaries_repozitory.get_all()
    return res


@app.get('/load')
async def load():
    return await salaries_repozitory.load_data()


@app.post('/aggregate', response_model=AvgResponse)
async def avg(data: RequestData):
    return await salaries_repozitory.avg_by_date(data.model_dump())


@app.get('/{pk}', response_model=Document)
async def retrieve(pk: str):
    return await salaries_repozitory.retrieve(pk)

