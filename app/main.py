# Main Application entry point - George Mwangi

from fastapi import FastAPI


def create_app() -> FastAPI:
    """ Create FastAPI application """
    server = FastAPI()

    return server


# Instantiate the application
app = create_app()
