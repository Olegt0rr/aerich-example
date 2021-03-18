import os

POSTGRES_URL = os.getenv("POSTGRES_URL")

TORTOISE_ORM = {
    "connections": {"default": POSTGRES_URL},
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
