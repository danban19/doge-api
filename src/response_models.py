"""DTO Models for the application."""
from typing import List, Optional
from pydantic import BaseModel


class BreedWeightResponseModel(BaseModel):
    """DTO model for the weight of a breed."""
    imperial: str
    metric: str


class BreedHeightResponseModel(BreedWeightResponseModel):
    """DTO model for the height of a breed."""


class BreedImageResponseModel(BaseModel):
    """DTO model for the image of a breed."""
    id: str
    width: int
    height: int
    url: str


class BreedResponseModel(BaseModel):
    """DTO model for a breed."""
    id: int
    name: str
    country_code: Optional[str] = None
    bred_for: Optional[str] = None
    breed_group: Optional[str] = None
    life_span: str
    temperament: str
    origin: Optional[str] = None
    reference_image_id: str
    weight: BreedWeightResponseModel
    height: BreedHeightResponseModel
    image: Optional[BreedImageResponseModel] = None


class BreedListResponseModel(BaseModel):
    """DTO model for a list of breeds."""
    breeds: List[BreedResponseModel]
