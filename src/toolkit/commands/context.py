import typer
import os
from platformdirs import user_config_dir
from typing_extensions import Annotated
from core.context import Context

app = typer.Typer()

@app.callback(invoke_without_command=True)
def context(
        project_id: Annotated[int, typer.Option()] = None
        ):
    ctx = Context()
    ctx.load()

    if project_id == ctx.project_id:
        print("Context already set.")
        return

