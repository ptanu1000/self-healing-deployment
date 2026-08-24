from fastapi import FastAPI
import os

app = FastAPI()

VERSION = os.getenv("APP_VERSION", "1.1.0")


@app.get("/")
def root():
    return {
        "application": "Self-Healing Demo",
        "version": VERSION
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "version": VERSION
    }


@app.get("/version")
def version():
    return {
        "version": VERSION
    }