import typer
from typing_extensions import Annotated


app = typer.Typer()

@app.callback(invoke_without_command=True)
def uuid(count: Annotated[int, typer.Option("-c")] = 1):
    import uuid

    for _ in range(count):
        print(str(uuid.uuid4()))
