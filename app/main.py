from fastapi import FastAPI

api = FastAPI(title="FastAPI on Azure Functions", version="0.1.0")


@api.get("/")
async def root() -> dict[str, str]:
    return {"message": "FastAPI is running on Azure Functions"}


@api.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
