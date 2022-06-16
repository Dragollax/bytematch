from transform import transform_user
import copy
test2 = {
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
test = [
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
_self = {
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


passed = []
once = False
class Match:
    def complex_match(*args, **kwargs):

        matches = []

        matchedUsers = [] 


        #return a dict of keys that are the user's interests
        modified_user = transform_user(_self, 'interest')   

        for user in test: #NOTE: change this later!!
            matchedInterests=[]
            for userInterest in user['interests']:
                #will compare key from modified_user with userInterest    
                #this will prevent us from having another nested for loop and waste time iterating through the user's interest every time
                if userInterest in modified_user: 
                    matchedInterests.append(userInterest)
                    user['matchedPercentage']=((len(matchedInterests)+1)/(len(user['interests'])+2)+(len(matchedInterests)+1)/(len(_self.get('interests'))+2))/2
                    user['matchedInterests']=matchedInterests
                    matchedUsers.append(user)
                    break
        matchedUsers.sort(key=lambda x: x.get('matchedPercentage'), reverse=True)

        for x in matchedUsers: #to remove duplicate dictionaries from list
            if x not in matches:
                matches.append(x)
        #if not enough users, use recursion to get enough users, and append the existing users into passed

        results = {
            "matched": matches,
        }
        return results
    def quick_match(*args,  **kwargs):
        #data group for matching
        #match_data = kwargs[0]
        #target for matching
        #target = args[0]
        i = 0 #will be used to iterate through interests
        j = 0 #will be used to iterate through the current user's interests
        once = False#just ot make sure we only assign inverted_group's length to length once
        length = 0
        raw_matches = []
        #this will stop the algo if we have reached the end of the user's interests. 
        while i < len(_self.get('interests')) or j < length: 
            #matchedInterests = []
            if once == False:
                once = True
                length = len(test2)
            
            if int(_self.get('interests')[i]) == int(list(test2.keys())[j]): #if the j'th value of inverted_group is equal to the i'th value of current_user
                j += 1
                users = test2.get(str(_self.get('interests')[i]))

                raw_matches.extend(users)

                    
            else: # if no matches, then move on onto the next interest in inverted_group
                j+=1
                if j == length: #if j reaches the end of inverted_group, then reset every value and move on to the next interest in current_user
                    i += 1 
                    j = 0
                    length = 0
                    once = False
                    continue
              
            if j == length: #reset everything and move onto the next interest
                i += 1 
                j = 0 
                once = False
                length = 0

        #removes duplicates in raw_matches, now contains dictionaries that have matchedTags...but some DON'T have matchedTags
        cleaned_matches = [i for n, i in enumerate(raw_matches) if i not in raw_matches[n + 1:]] 
        #Here we take all the dictionaries with matchedTags, and save those into the final match list. Complete!
        results= {
            "matched": cleaned_matches,
        }
        return results

print(Match.complex_match())
print(Match.quick_match())