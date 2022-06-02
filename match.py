import transform_user from transform
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

passed = []
once = False

def get(self, request, *args):
    limit = 100
    offset = 0
    global passed
    global once
    if not once:
        #set the initial values for passed
        passed = args[2] #args[2] will contain initial passed values
        if passed:
            passed.append(request.user.id)
    recur = True #to prevent infinite recursion if not enough results
    matches = []
    if args:
        passed = copy.deepcopy(args[0])#for recursion
        matches.extend(args[1])
    if limit and offset:
        #exclude previous user ids, then append new random users onto the list
            _self = __self
            #will only execute if recursion is happening
            if passed:
                limit2 = limit - len(passed) 
                current = passed #should be a list of user id's
                filtered_queryset = test
                if filtered_queryset.count() < 100:
                    recur = False
                #can consider limiting queryset after we've created a match list later on
                users = filtered_queryset.order_by('?')[:int(offset) + int(limit2)]   
                matchedUsers = [] 
           """ else:
                current = request.data.get('users') #should be a list of user id's
                current.append(request.user.id)
                filtered_queryset = UserProfileInfo.objects.all().exclude(id__in=current)
                queryset = UserProfileInfo.objects.all().order_by('?')[:int(offset) + int(limit)]
                """

    else:
        return Response("Either limit or offset was not provided!")
    #return a dict of keys that are the user's interests
    modified_user = transform_user(__self, 'interest')        
    for user in users.data:
        matchedInterests=[]
        for userInterest in user['interests']:
            #will compare key from modified_user with userInterest    
            #this will prevent us from having another nested for loop and waste time iterating through the user's interest every time
            if userInterest in modified_user: 
                matchedInterests.append(userInterest)
                user['matchedPercentage']=((len(matchedInterests)+1)/(len(user['interests'])+2)+(len(matchedInterests)+1)/(len(_self.data['interests'])+2))/2
                user['matchedInterests']=matchedInterests
                matchedUsers.append(user)
                match=True
                break
    matchedUsers.sort(key=lambda x: x.get('matchedPercentage'), reverse=True)
    modified_user = transform_user(_self.data, 'tag')
    for user in users.data:
        matchedInterestsTags=[]
        for userInterestTags in user['tags']:
            if userInterestTags in modified_user:
                matchedInterestsTags.append(userInterestTags)
                user['matchedTags']=matchedInterestsTags
                matchedUsers.append(user)
                match=True 
                break

    for x in matchedUsers: #to remove duplicate dictionaries from list
        if x not in matches:
            matches.append(x)
    #if not enough users, use recursion to get enough users, and append the existing users into passed
    if request.data.get('users'):
        length = len(matches) + len(passed)
        once = True
        if recur:
            if length < limit: #not enough users that matched
                for i in matches:
                    passed.append(i.get('id')) 
                self.get(request, passed, matches)
    context= {
        "matchedUsers": matches,
        "has_more": more_matches(request)
    }
    return Response(context)