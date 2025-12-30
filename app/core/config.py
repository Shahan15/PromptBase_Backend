from pydantic_settings import BaseSettings,SettingsConfigDict


class Settings(BaseSettings):
    # SUPABASE CONFIG
    SUPABASE_URL : str
    SUPABASE_KEY : str

    # GEMINI CONFIG
    GEMINI_API_KEY : str
    GEMINI_MODEL : str

    # JWT AUTH
    JWT_SECRET : str
    JWT_ALGORITHM : str
    JWT_EXPIRES_MINUTES : int

    model_config = SettingsConfigDict(env_file=".env",extra= "ignore")

settings = Settings()