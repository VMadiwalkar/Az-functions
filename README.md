# Az-functions

FastAPI API scaffolded for Azure Functions Flex Consumption with Python 3.13 and `uv`.

## Project layout

- `function_app.py`: Azure Functions entrypoint using `func.AsgiFunctionApp`
- `app/main.py`: FastAPI application and routes
- `pyproject.toml`: source of truth for dependencies managed by `uv`
- `requirements.txt`: exported dependency list for Azure remote build

## Local setup with uv

```powershell
uv venv
.venv\Scripts\Activate.ps1
uv sync
```

If you change dependencies in `pyproject.toml`, refresh the Azure build file:

```powershell
uv lock
uv export --format requirements.txt --no-hashes --output-file requirements.txt
```

## Run locally

Install Azure Functions Core Tools if needed, then start the app from the project root:

```powershell
func start
```

Try:

- `http://localhost:7071/`
- `http://localhost:7071/health`

## Deploy to your existing Flex Consumption Function App

Flex Consumption uses One Deploy, and for Python apps Azure recommends a remote build.

With Azure Functions Core Tools:

```powershell
func azure functionapp publish <APP_NAME> --build remote
```

If deployment fails because the app has no deployment package location configured, set the deployment storage once with Azure CLI:

```powershell
az functionapp deployment config set `
  --resource-group <RESOURCE_GROUP> `
  --name <APP_NAME> `
  --deployment-storage-name <STORAGE_ACCOUNT> `
  --deployment-storage-container-name <CONTAINER_NAME>
```

## Notes

- Keep the Function App on Python `3.13`.
- `host.json` sets `routePrefix` to an empty string so FastAPI routes stay clean.
- For production, change `http_auth_level` in `function_app.py` if you do not want anonymous access.
