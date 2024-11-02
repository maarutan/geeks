from decouple import Config, RepositoryEnv  # type: ignore

config = Config(RepositoryEnv("../.env"))
tgToken = config("TOKEN")
