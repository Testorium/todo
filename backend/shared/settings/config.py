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


# --- API Prefix Configuration ---
class APIV1PrefixConfig:
    prefix: str = "/v1"
    auth: str = "/auth"
    users: str = "/users"


class APIPrefixConfig:
    prefix: str = "/api"
    v1: APIV1PrefixConfig = APIV1PrefixConfig()


api_prefix_config = APIPrefixConfig()


# --- JWT Configuration ---
class JWTConfig:
    algorithm: str = os.getenv("JWT_ALGORITHM")
    secret_key: str = os.getenv("JWT_SECRET_KEY")
    token_time: int = int(os.getenv("JWT_TOKEN_TIME"))


jwt_config = JWTConfig()


# --- Cookie Configuration ---
class CookieConfig:
    key: str = "authtoken"
    max_age: int = 900
    samesite: str = "none"
    httponly: bool = True
    secure: bool = True


cookie_config = CookieConfig()
