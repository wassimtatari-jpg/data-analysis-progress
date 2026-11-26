import pandas as pd

animals = pd.DataFrame({
    "animal_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "animal_name": ["Lion", "Elephant", "Gazelle", "Leopard",
                    "Zebra", "Hyena", "Giraffe", "Cheetah"],
    "species": ["Mammal", "Mammal", "Mammal", "Mammal",
                "Mammal", "Mammal", "Mammal", "Mammal"],
    "reserve": ["Serengeti", "Kruger", "Serengeti", "Kruger",
                "Amboseli", "Serengeti", "Amboseli", "Kruger"]
})

observations = pd.DataFrame({
    "observation_id": [1, 2, 3, 4, 5, 6, 7, 8],
    "animal_id": [101, 103, 105, 109, 102, 110, 107, 111],
    "observation_date": [
        "2026-10-01", "2026-10-02", "2026-10-03",
        "2026-10-04", "2026-10-05", "2026-10-06",
        "2026-10-07", "2026-10-08"
    ],
    "hours_observed": [3, 2, 5, 1, 4, 2, 3, 6]
})
#use filtring joing
animals_observed=animals[animals["animal_id"].isin(observations['animal_id'])]
print(animals_observed)
animals_not_observed=animals[~animals['animal_id'].isin(observations["animal_id"])]
print(animals_not_observed)
