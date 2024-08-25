class Settings(): 
    POSTGRES_UNAME: str = "pranavrnayakn"
    POSTGRES_PASS: str = "password"
    POSTGRES_HOST:str = 'localhost'
    POSTGRES_PORT:str = '5432'
    POSTGRES_DB:str = 'todo'
    MONGO_URL:str = "mongodb://localhost:27017"
    
    def get_database_url(self) -> str:
        return f"postgresql://{self.POSTGRES_UNAME}:{self.POSTGRES_PASS}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    def get_mongo_url(self) -> str:
        return self.MONGO_URL
# Create an instance of the Settings class
settings = Settings()
