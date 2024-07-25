
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sayvai_sqlagent.agent import SQLAgent

app = FastAPI()

agent = SQLAgent()


class Query(BaseModel):
    sql_query: str


@app.post("/run-query")
def run_query(query: Query):
    try:
        result = agent.run(query.sql_query)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
