query = """ {
    films {
        edges {
            node {
                title
                episodeId
                producer
                director
                people {
                    edges {
                        node {
                            name
                        }
                    }
                }
                planets {
                    edges {
                        node {
                            name 
                        }
                    }
                }
            }
        }
    }
} """

result_query = {
    "films": {
        "edges": [
            {
                "node": {
                    "title": "A New Hope",
                    "episodeId": 4,
                    "producer": "Gary Kurtz, Rick McCallum",
                    "director": "George Lucas",
                    "people": {
                        "edges": [
                            {
                                "node": {
                                    "name": "Luke Skywalker"
                                }
                            }
                        ]
                    },
                    "planets": {
                        "edges": [
                            {
                                "node": {
                                    "name": "Tatooine"
                                }
                            }
                        ]
                    }
                }
            },
        ]
    }
}

create_mutation = """
mutation create($input: CreateFilmInput!) {
    createFilm(input: $input) {
        film {
            title
            episodeId
            openingCrawl
            director
            producer
            releaseDate
            people {
                edges {
                    node {
                        name
                    }
                }
            }
            planets {
                edges {
                    node {
                        name
                    }
                }
            }
        }
    }
}
"""

input_mutation = {
    "input": {
        "title": "New Film",
        "episodeId": "13",
        "openingCrawl": "New Episode Star Wars",
        "director": "George Lucas",
        "producer": "Gary Kurtz, Rick McCallum",
        "releaseDate": "2020-05-25",
        "people": [1],
        "planets": [1],
    }
}
