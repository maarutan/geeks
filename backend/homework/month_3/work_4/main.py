from decouple import Config, RepositoryEnv  # type: ignore
config = Config(RepositoryEnv("../.env"))
TOKEN = config("TOKEN")
print(TOKEN)               