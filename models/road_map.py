from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean ,Float
from sqlalchemy.orm import relationship
from datetime import datetime
from .base_model import BaseModel 

class RoadMap(BaseModel):
    __tablename__ = "road_map"
    
    id = Column(Integer, primary_key=True)
    mission_id = Column(Integer, ForeignKey("mission.id"))

    area_name = Column(String, nullable=False)

    active = Column(Boolean, default=False)
    reached = Column(Boolean, default=False)
    index = Column(Integer,nullable=True)

    synchronized = Column(Boolean,default=False)

    reached_time = Column(DateTime,nullable=True)
    created_date = Column(DateTime, default=datetime.utcnow)

    mission = relationship("Mission", back_populates="road_map")
