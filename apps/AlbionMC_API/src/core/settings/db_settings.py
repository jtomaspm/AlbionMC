from pydantic import BaseModel


class DbSettings(BaseModel):
    dbname      :str
    user        :str
    password    :str
    host        :str
    port        :str