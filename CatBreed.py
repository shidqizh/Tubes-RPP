from dataclasses import dataclass
from typing import List

@dataclass
class CatBreed:
    name: str
    size: str  
    coat_type: str
    coat_colors: List[str]
    face_shape: str
    ear_type: str
    eye_colors: List[str]
    body_type: str
    tail_type: str
    personality: List[str]
    origin: str
    life_span: str
    health_issues: List[str]
    recognition_score: float  