from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean ,Float
from sqlalchemy.orm import relationship
from datetime import datetime

from .base_model import BaseModel 

class Location(BaseModel):
    __tablename__ = "location"
    
    id = Column(Integer, primary_key=True)
    mission_id = Column(Integer, ForeignKey("mission.id"))

    vertical_coordinate = Column(Float, nullable=False)
    horizontal_coordinate = Column(Float, nullable=False)

    direction_horizontal = Column(Integer, nullable=False,default=0)
    direction_vertical = Column(Integer, nullable=False,default=0)

    synchronized = Column(Boolean,default=False)

    update_date = Column(DateTime, default=datetime.utcnow)

    mission = relationship("Mission", back_populates="location")
