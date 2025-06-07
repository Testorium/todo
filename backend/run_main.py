__all__ = (
    "app",
    "main",
)


from main import app
from shared.gunicorn import Application, get_app_options
from shared.settings import gunicorn_config


def main():
    Application(
        application=app,
        options=get_app_options(
            host=gunicorn_config.host,
            port=gunicorn_config.port,
            timeout=gunicorn_config.timeout,
            workers=gunicorn_config.workers,
            log_level=gunicorn_config.log_level,
        ),
    ).run()


if __name__ == "__main__":
    main()
