query = """ {
    people {
        edges {
            node {
                name
                height
                birthYear
                gender
                homeworld {
                   name
                }
            }
        }
    }
} """

result_query = {
    "people": {
        "edges": [
            {
                "node": {
                    "name": "Luke Skywalker",
                    "height": "172",
                    "birthYear": "19BBY",
                    "gender": "male",
                    "homeworld": {
                        "name": "Tatooine"
                    }
                }
            },
        ]
    }
}

create_mutation = """
mutation create($input: CreatePersonInput!) {
    createPerson(input: $input) {
        person {
            name
            height
            birthYear
            gender
            homeworld {
                name
            }
        }
    }
}
"""

input_mutation = {
    "input": {
        "name": "New Person",
        "gender": "male",
        "skinColor": "fair",
        "hairColor": "blond",
        "height": "173",
        "eyeColor": "green",
        "mass": "82",
        "homeworld": 1,
        "birthYear": "29BBY",
    }
}
