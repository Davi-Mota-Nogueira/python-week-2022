from sqlmodel import create_engine
from beerlog.config import settings
from beerlog import models

# myslq://localhost:5453@user:pass/berrer

engine = create_engine(settings.database.url)

models.SQLModel.metadata.create_all(engine)
