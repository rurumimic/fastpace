from typing import Any, Dict, List

from pydantic import BaseModel, Field
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    YamlConfigSettingsSource,
)


class TempModel(BaseModel):
    name: str = Field(default="")
    value: float = Field(default=0.0)


class Settings(BaseSettings):
    """FastPace API Settings"""

    model_config = SettingsConfigDict(
        env_prefix="FASTPACE_",
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        cli_parse_args=False,
        # cli_avoid_json=True,
        # cli_enforce_required=True,
        secrets_dir=None,
        yaml_file=["config.yaml"],
        yaml_file_encoding="utf-8",
    )

    debug: bool = Field(default=False)
    title: str = Field(default="FastPace")
    summary: str = Field(default="A Simple API")
    description: str = Field(default="A simple API")
    version: str = Field(default="0.0.1")

    temp: List[TempModel] = Field(default_factory=list)

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            file_secret_settings,
            YamlConfigSettingsSource(settings_cls),
        )


if __name__ == "__main__":
    from pprint import pprint

    settings = Settings()
    pprint(settings.model_dump())
