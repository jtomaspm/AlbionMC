from typing import Any


class DbSettings:
    dbname      :str
    user        :str
    password    :str
    host        :str
    port        :str
    def __init__(self, dbname:str, user:str, password:str, host:str, port:str) -> None:
        self.dbname     = dbname   
        self.user       = user    
        self.password   = password
        self.host       = host    
        self.port       = port    