from dataclasses import dataclass


@dataclass
class DbSettings:
    dbname      :str
    user        :str
    password    :str
    host        :str
    port        :str