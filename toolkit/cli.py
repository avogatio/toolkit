import typer
from commands import uuid, project

app = typer.Typer()
app.add_typer(uuid.app, name="uuid")
app.add_typer(project.app, name="project")
