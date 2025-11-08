import json
import os
from constants import APP_NAME
from pathlib import Path
from tempfile import NamedTemporaryFile
from platformdirs import user_config_dir

class Context:
    _filename = "context.json"

    def __init__(self):
        self._config_path = Path(user_config_dir(APP_NAME))
        self._config_path.mkdir(parents=True, exist_ok=True)
        self._context_path = self._config_path / self._filename
        self._data = {}
        self._dirty = False

    def load(self) -> dict:
        if not self._context_path.exists():
            return {}

        with self._context_path.open("r", encoding="utf-8") as f:
            self._data = json.load(f)
            return self._data

    @property
    def project_id(self) -> str | None:
        return self._data.get("project_id")

    @project_id.setter
    def project_id(self, value: str):
        self._data["project_id"] = value
        self._dirty = True

    def save(self):
        if not self._dirty:
            return

        with NamedTemporaryFile(
                "w", delete=False, dir=self._config_path, encoding="utf-8"
                ) as tmp:
            json.dump(self._data, tmp, indent=2)
            tmp.flush()
            os.fsync(tmp.fileno())
            os.replace(tmp.name, self._context_path)

        self._dirty = False

    def __repr__(self):
        return f"Context(project_id={self.project_id!r})"
