from match import Match

#NOTE: quick_match and complex_match require different data structure preconditions
test2 = {
    "3": [
        {
            "id": 32589021,
            "username": "dragolla",
            "interests": [
                1,
                3
            ],
            "biography": "",
            "tags": [
                "swimming"
            ]
        }
    ],
    "5": [
        {
            "id": 578172410,
            "username": "teststs",
            "interests": [
                5
            ],
            "biography": "",
            "tags": [
                "coding"
            ]
        }
    ]
}  
test = [
        {
            "id": 32589021,
            "username": "dragolla",
            "interests": [
                1,
                3
            ],
            "biography": "",
            "tags": [
                "swimming"
            ]
        }
    ,
        {
            "id": 578172410,
            "username": "teststs",
            "interests": [
                5
            ],
            "biography": "",
            "tags": [
                "coding"
            ]
        }
]
target = [3]
#print(Match.complex_match(target, test))
print(Match.quick_match(target, test2)) 