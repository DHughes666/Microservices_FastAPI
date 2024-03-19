from fastapi import FastAPI
from pathlib import Path
import yaml

app = FastAPI(
    debug=True, openapi_url='/openapi/orders.json', docs_url='/docs/orders'
    )

oas_doc =yaml.safe_load(
    (Path(__file__).parent / '../oas.yaml').read_text()
)

app.openapi = lambda: oas_doc