class Services:
    TV = {"id": 0,
          "name": "tv",
          "description": "tv",
          "price": 300,
          "device_types": ['tv']}
    MOBILE = {"id": 1,
              "name": "mobile",
              "description": "mobile",
              "price": 150,
              "device_types": ['mobile']}
    STB = {"id": 2,
           "name": "stb",
           "description": "description",
           "price": 0,
           "device_types": ['stb']}


class Films:
    RELEASED = {"name": "Gemini",
                "description": "Action thriller",
                "start_date": 1569888000,
                "end_date": 1609459199,
                "services": [0]}
    NOT_RELEASED = {"name": "28 Months Later",
                    "description": "Horror",
                    "start_date": 1640908800,
                    "end_date": 1672531199,
                    "services": [0]}
    ENDED = {"name": "Green Book",
             "description": "Comedy-drama",
             "start_date": 1536624000,
             "end_date": 1577836799,
             "services": [0]}
