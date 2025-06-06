import os

from dotenv import load_dotenv

load_dotenv()


# --- Database Configuration ---
class DatabaseConfig:
    driver: str = "sqlite+aiosqlite"
    file_name: str = "database.sqlite"

    echo: bool = os.getenv("DB_ECHO", "false").lower() == "true"
    echo_pool: bool = os.getenv("DB_ECHO_POOL", "false").lower() == "true"
    pool_size: int = int(os.getenv("DB_POOL_SIZE", 5))
    max_overflow: int = int(os.getenv("DB_MAX_OVERFLOW", 10))

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }

    @property
    def url(self) -> str:
        return f"{self.driver}:///./{self.file_name}"


db_config = DatabaseConfig()
