query = """ {
    planets {
        edges {
            node {
                name
                terrain
                climate
                population
            }
        }
    }
} """

result_query = {
    "planets": {
        "edges": [
            {
                "node": {
                    "name": "Tatooine",
                    "terrain": "dessert",
                    "climate": "arid",
                    "population": "200000"
                }
            }, 
        ]
    }
}

create_mutation = """
mutation create($input: CreatePlanetInput!) {
    createPlanet(input: $input) {
        planet {
            name
        }
    }
}
"""

input_mutation = {
    "input": {
        "name": "test",
        "rotationPeriod": "1",
        "orbitalPeriod": "1",
        "diameter": "10",
        "climate": "arid",
        "gravity": "1",
        "terrain": "dessert",
        "surfaceWater": "1",
        "population": "1"
    }
}
