from match import Match

test = {
    "3": [
        {
            "id": 32589021,
            "username": "dragolla",
            "profile_image": "https://weco-static.s3.amazonaws.com/profilepicture.jpg",
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
            "profile_image": "https://weco-static.s3.amazonaws.com/profilepicture.jpg",
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
test2 = [
        {
            "id": 32589021,
            "username": "dragolla",
            "profile_image": "https://weco-static.s3.amazonaws.com/profilepicture.jpg",
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
            "profile_image": "https://weco-static.s3.amazonaws.com/profilepicture.jpg",
            "interests": [
                5
            ],
            "biography": "",
            "tags": [
                "coding"
            ]
        }
]
__self = {
        "5": [
        {
            "id": 578172410,
            "username": "teststs",
            "profile_image": "https://weco-static.s3.amazonaws.com/profilepicture.jpg",
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

#print(Match.complex_match(__self, test)) 
print(Match.complex_match)