from fastapi import FastAPI, APIRouter
from fastapi.responses import ORJSONResponse
from clickhouse_driver import Client

router = APIRouter()

app = FastAPI(
    title='ClickHouse example',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)



clickhouse = Client(host='clickhouse')

@router.get(
    '/getWords'
)
async def get_words():
    query = '''
    SELECT word, count(*)
    FROM (
    SELECT
        splitByChar(' ', combined_text) AS word
    FROM (
        SELECT arrayJoin([title, text, topic]) AS combined_text
        FROM `default`.lenta_ru_news lrn
        )
    )
    GROUP BY word
    ORDER BY count(*) DESC
    LIMIT 100
    '''
    result = clickhouse.execute(query)
    return result

app.include_router(router)
