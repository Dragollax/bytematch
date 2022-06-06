from transform import transform_user
import copy
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
class Match:
    def complex_match(self, *args, **kwargs):
        limit = 100
        offset = 0
        global passed
        global once
        if not once:
            #set the initial values for passed
            passed = args[2] #args[2] will contain initial passed values

        recur = True #to prevent infinite recursion if not enough results
        matches = []
        if args:
            passed = copy.deepcopy(args[0])#for recursion
            matches.extend(args[1])

        #exclude previous user ids, then append new random users onto the list
            _self = kwargs[0]
            #will only execute if recursion is happening
            if passed:
                limit2 = limit - len(passed) 
                current = passed #should be a list of user id's
                filtered_queryset = kwargs[1]
                if filtered_queryset.count() < 100:
                    recur = False
                #can consider limiting queryset after we've created a match list later on
                users = filtered_queryset.order_by('?')[:int(offset) + int(limit2)]   
                matchedUsers = [] 


        #return a dict of keys that are the user's interests
        modified_user = transform_user(_self, 'interest')        
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

        for x in matchedUsers: #to remove duplicate dictionaries from list
            if x not in matches:
                matches.append(x)
        #if not enough users, use recursion to get enough users, and append the existing users into passed

        length = len(matches) + len(passed)
        once = True
        if recur:
            if length < limit: #not enough users that matched
                for i in matches:
                    passed.append(i.get('id')) 
                self.complex_match(passed, matches, kwargs[0], kwargs[1])
        context= {
            "matchedUsers": matches,
            "has_more": more_matches(request)
        }
        return Response(context)
    def quick_match(self, *args,  **kwargs):
        _self = kwargs[0] 
        queryset = kwargs[1]
        modified_group = transform_user(_self, "interest")
        i = 0 #will be used to iterate through interests
        j = 0 #will be used to iterate through the current user's interests
        once = False#just ot make sure we only assign inverted_group's length to length once
        length = 0
        raw_matches = []
        #this will stop the algo if we have reached the end of the user's interests. 
        while i < len(_self.data['interests']) or j < length: 
            #matchedInterests = []
            if once == False:
                once = True
                length = len(modified_group)
            if _self.data['interests'][i] == list(modified_group.keys())[j]: #if the j'th value of inverted_group is equal to the i'th value of current_user
                j += 1
                users = modified_group[_self.data['interests'][i]] 

                raw_matches.extend(users)
                #raw_matches.extend([dict(item, **{'matchedInterest':matchedInterests}) for item in user])#add the values(people) of the dict into raw_matches
                #NOTE: need to do .extend() to get all values of list in existing list
                    
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
        context= {
            "matchedUsers": cleaned_matches,
            "has_more": more_matches(request)
        }
        return Response(context)