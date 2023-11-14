import click
from fastapi import FastAPI
from pydantic.networks import IPvAnyAddress
import uvicorn
from entrypoints.web.legacy import router as legacy_routes


app = FastAPI()
app.include_router(legacy_routes)


@click.command()
@click.option('--server-port', default=8080)
@click.option('--server-host', type=IPvAnyAddress, default='0.0.0.0')
def main(server_port: int, server_host):
    uvicorn.run(app, host=str(server_host), port=server_port)


if __name__ == '__main__':
    main()