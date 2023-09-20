from pydantic_settings import BaseSettings, SettingsConfigDict
from yarl import URL


class Settings(BaseSettings):
    # database
    psql_db_dsn: str
    psql_async_db_dsn: str
    psql_db_user: str
    psql_db_pwd: str
    psql_db_host: str
    psql_db_port: str
    psql_db_lt: str
    
    neo4j_bolt_uri: str
    neo4j_user: str
    neo4j_password: str

    model_config = SettingsConfigDict(env_file=".env")
    
    @property
    def psql_dsn(self) -> URL:
        return URL.build(
            scheme="postgresql+asyncpg",
            host=self.psql_db_host,
            port=self.psql_db_port,
            user=self.psql_db_user,
            password=self.psql_db_pwd,
            path=self.psql_db_lt,
        )

settings = Settings()