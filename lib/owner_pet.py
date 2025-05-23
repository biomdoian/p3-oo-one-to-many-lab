class Owner:
    def __init__(self, name: str):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of the Pet class.")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name: str, pet_type: str, owner=None):
        self.name = name

        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type. Must be one of: {', '.join(Pet.PET_TYPES)}.")
        self._pet_type = pet_type

        self._owner = None
        if owner is not None:
            self.owner = owner

        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, Owner):
            raise Exception("Owner must be an instance of Owner class.")
        self._owner = value