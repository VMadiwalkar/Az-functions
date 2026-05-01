import azure.functions as func

from app.main import api


app = func.AsgiFunctionApp(
    app=api,
    http_auth_level=func.AuthLevel.ANONYMOUS,
)
