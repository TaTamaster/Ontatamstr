import os


class Settings:
    """Application settings.

    This project uses a single primary database: PostgreSQL.
    """

    def __init__(self) -> None:
        self.database_url: str = os.getenv(
            "VOD_DATABASE_URL",
            "postgresql+psycopg://vod_user:vod_pass@localhost:5432/vod_db",
        )


settings = Settings()
