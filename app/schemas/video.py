from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class VideoBase(BaseModel):
    title: str
    description: Optional[str] = None
    storage_key: str
    thumbnail_url: Optional[str] = None
    duration_seconds: Optional[int] = None
    is_published: bool = False


class VideoCreate(VideoBase):
    pass


class VideoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    storage_key: Optional[str] = None
    thumbnail_url: Optional[str] = None
    duration_seconds: Optional[int] = None
    is_published: Optional[bool] = None


class VideoRead(VideoBase):
    id: int
    created_by_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
