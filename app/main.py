# Main Application entry point - George Mwangi

from fastapi import FastAPI
from app.routes import employee_routes


def create_app() -> FastAPI:
    """ Create FastAPI application """

    # instantiating the FastAPI class
    server = FastAPI()

    # instantiate employee router
    employee_router = employee_routes()

    # include employee routes to main application
    server.include_router(employee_router)

    return server


# Instantiate the application
app = create_app()
