from KB import CatBreedKB
from dataclasses import asdict

def main():
    kb = CatBreedKB()
    
    while True:
        print("\nCat Breed Identification System:")
        print("1. Identify breed")
        print("2. View breed details")
        print("3. List all breeds")
        print("4. Exit")
        
        choice = input("\nChoice (1-4): ")
        
        if choice == '1':
            chars = {}
            print("\nEnter characteristics (press Enter to skip):")
            chars['size'] = input("Size (Small/Medium/Large): ")
            chars['coat_type'] = input("Coat type: ")
            chars['coat_colors'] = input("Coat color: ")
            chars['face_shape'] = input("Face shape: ")
            chars['ear_type'] = input("Ear type: ")
            chars['eye_colors'] = input("Eye color: ")
            chars['body_type'] = input("Body type: ")
            
            chars = {k: v for k, v in chars.items() if v}
            matches = kb.identify_breed(chars)
            
            print("\nPossible matches:")
            for breed, score in matches[:3]:
                print(f"{breed}: {score:.2%} confidence")
                
        elif choice == '2':
            breed_name = input("Enter breed name: ")
            breed = next((value for key, value in kb.breeds.items() if key.lower() == breed_name), None)
            if breed:
                print(f"\n{breed.name} Details:")
                for field, value in asdict(breed).items():
                    if field != 'name':
                        print(f"{field.replace('_', ' ').title()}: {value}")
            else:
                print("Breed not found!")
                
        elif choice == '3':
            print("\nAvailable breeds:")
            for breed in sorted(kb.breeds.keys()):
                print(f"- {breed}")
                
        elif choice == '4':
            break

if __name__ == "__main__":
    main()