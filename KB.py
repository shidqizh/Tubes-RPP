import json
from typing import List, Dict
from dataclasses import asdict
import difflib
from CatBreed import CatBreed


class CatBreedKB:
    def __init__(self, filename='cat_breeds.json'):
        self.filename = filename
        self.breeds = self._initialize_breeds()
        self.save()
        
    def save(self):
        with open(self.filename, 'w') as f:
            json.dump({name: asdict(breed) for name, breed in self.breeds.items()}, f, indent=2)
            
    def _initialize_breeds(self) -> Dict[str, CatBreed]:
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return {name: CatBreed(**attrs) for name, attrs in data.items()}
        except FileNotFoundError:
            return {
                "Persian": CatBreed(
                    name="Persian",
                    size="Large",
                    coat_type="Long, thick, luxurious",
                    coat_colors=["White", "Black", "Blue", "Red", "Cream", "Tabby"],
                    face_shape="Flat, round",
                    ear_type="Small, rounded",
                    eye_colors=["Blue", "Copper", "Odd-eyed"],
                    body_type="Cobby, muscular",
                    tail_type="Short, thick",
                    personality=["Gentle", "Quiet", "Laid-back"],
                    origin="Iran (Persia)",
                    life_span="12-17 years",
                    health_issues=["Polycystic kidney disease", "Breathing problems"],
                    recognition_score=0.9
                ),
                "Siamese": CatBreed(
                    name="Siamese",
                    size="Medium",
                    coat_type="Short, fine, glossy",
                    coat_colors=["Seal Point", "Blue Point", "Chocolate Point", "Lilac Point"],
                    face_shape="Wedge-shaped",
                    ear_type="Large, pointed",
                    eye_colors=["Blue"],
                    body_type="Slender, athletic",
                    tail_type="Long, thin, tapered",
                    personality=["Vocal", "Intelligent", "Social"],
                    origin="Thailand (Siam)",
                    life_span="12-20 years",
                    health_issues=["Cross-eyed condition", "Liver amyloidosis"],
                    recognition_score=0.95
                )
            }

    def identify_breed(self, characteristics: Dict[str, str]) -> List[tuple]:
        matches = []
        for breed in self.breeds.values():
            score = 0
            total_weights = 0
            
            weights = {
                'coat_type': 0.2,
                'coat_colors': 0.15,
                'face_shape': 0.2,
                'ear_type': 0.15,
                'eye_colors': 0.1,
                'body_type': 0.1,
                'size': 0.1
            }
            
            for attr, weight in weights.items():
                if attr in characteristics:
                    value = characteristics[attr]
                    breed_value = getattr(breed, attr)
                    
                    if isinstance(breed_value, list):
                        if value in breed_value:
                            score += weight
                    else:
                        similarity = difflib.SequenceMatcher(None, value.lower(), 
                                                           breed_value.lower()).ratio()
                        score += weight * similarity
                    
                    total_weights += weight
            
            if total_weights > 0:
                normalized_score = (score / total_weights) * breed.recognition_score
                matches.append((breed.name, normalized_score))
        
        return sorted(matches, key=lambda x: x[1], reverse=True)
