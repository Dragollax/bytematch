#------------------------------------new algorithm-----------------------------------
from collections import OrderedDict
"""
current_user - the user making the request and their interests
inverted group - is exactly as the people dictionary as you see below, but ordered as 'interest' : ['person1', 'person2']...etc

The concept behind this algorithm to compare every j'th interest(key) of inverted group with the i'th interest(key) of current_user.
To do this, for every i incremented by one, j is looped through the entire inverted_group's length of interests
For example: current_user has 2 interests, inverted_group has 13 interests]
i represents the current current_user's interest, while j is the current inverted_group's interest
everytime j reaches 13, it gets reset and i is incremented by 1. This will allow every interest of inverted_group to be compared with 
every interest of current_user

in other words, we increment j by one every time , which is equivalent to getting every interest in inverted_group. We then take this value and 
compare it with the i'th value of the user's interest. Doing this will compare all 13 interests with the i'th interest of current_user
"""
people = {
'person1': ['interest','interest3', 'interest4', 'interest5'], 
'person2': ['interest', 'interest4', 'interest5','interest6','interest2','interest9','interest3'],
'person3': ['interest6 ', 'interest4', 'interest5', 'interest3', 'interest2', 'interest', 'interest10'],
'person4': ['interest7', 'interest4', 'interest6','interest8','interest9','interest10'],
'person6': ['interest', 'interest4','interest5', 'interest6','interest7','interest8','interest9'],
'person7': ['interest', 'interest3', 'interest2', 'interest1','interest6','interest7','interest8'],
'person8': ['interest', 'interest4', 'interest5','interest6','interest7'],
'person10': ['interest3', 'interest4', 'interest6','interest7','interest8','interest9'],
'person11': ['interest', 'interest7', 'interest8', 'interest5'],
'person12': ['interest2', 'interest4', 'interest8','interest9', 'interest10', 'interest3', 'interest7', 'interest6'],
'person13': ['interest5', 'interest6', 'interest10', 'interest7', 'interest2'],
'person14': ['interest3', 'interest4', 'interest8', 'interest10', 'interest9', 'interest7'],
'person15': ['interest', 'interest4', 'interest5', 'interest6', 'interest8', 'interest0'],
}
current_user = people.get('person3') #request.user
people.pop('person3') #remove current user from matching list

#print(current_user[2])
#quit()
inverted_group = {}
for key, value in person.items():
    for x in value:
        inverted_group.setdefault(x, list()).append(key)
#print(len(list(inverted_group.keys())))
#print(inverted_group["interest"])
#print(len(inverted_group))
#print(len(current_user))
#quit()

i = 0 #will be used to iterate through interests
j = 0 #will be used to iterate through the current user's interests
once = False#just ot make sure we only assign inverted_group's length to length once
length = 0
raw_matches = []

#this will stop the algo if we have reached the end of the user's interests. 
while i < len(current_user) or j < length: 
    if once == False:
       once = True
       length = len(inverted_group)
    if current_user[i] == list(inverted_group.keys())[j]: #if the j'th value of inverted_group is equal to the i'th value of current_user
        j += 1
        raw_matches.extend(inverted_group[current_user[i]])#add the values(people) of the dict into raw_matches
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

final_matches = list(OrderedDict.fromkeys(raw_matches)) #removes duplicates in raw_matches


                

#print('group ', interest_group,'\n') #this could be for posts section
print('matches: ', final_matches,'\n')

#------------------------------------------------------extracting location matched------------------------------------------
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
location = {
    578172410 : 
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
            ],
            "matchedInterests":
                [
                "running",
                "swimming"
                ],
        }
        
    
    
}
for k,v in test.items():
    for x in v:
        if x['id'] in location:
            location[x['id']]['matchedInterests'].extend(["coding"])
        else:
            location[x['id']] = x
            location[x['id']]['matchedInterests'] = ['swimming', 'running']
            #print(location[x['id']])
            
print(location)


# ---------------------------------------------------OLD ALGORITHM---------------------------------------------------------
people = {
'person1': ['interest','interest3', 'interest4', 'interest5'], 
'person2': ['interest', 'interest4', 'interest5','interest6','interest2','interest9','interest3'],
'person3': ['interest6 ', 'interest4', 'interest5', 'interest3', 'interest2', 'interest', 'interest10'],
'person4': ['interest7', 'interest4', 'interest6','interest8','interest9','interest10'],
'person6': ['interest', 'interest4','interest5', 'interest6','interest7','interest8','interest9'],
'person7': ['interest', 'interest3', 'interest2', 'interest1','interest6','interest7','interest8'],
'person8': ['interest', 'interest4', 'interest5','interest6','interest7'],
'person10': ['interest3', 'interest4', 'interest6','interest7','interest8','interest9'],
'person11': ['interest', 'interest7', 'interest8', 'interest5'],
'person12': ['interest2', 'interest4', 'interest8','interest9', 'interest10', 'interest3', 'interest7', 'interest6'],
'person13': ['interest5', 'interest6', 'interest10', 'interest7', 'interest2'],
'person14': ['interest3', 'interest4', 'interest8', 'interest10', 'interest9', 'interest7'],
'person15': ['interest', 'interest4', 'interest5', 'interest6', 'interest8', 'interest0'],
}
current_user = people.get('person3') #request.user
people.pop('person3') #remove current user from matching list
choice = people #new list
location = {}#where the users matched
seen = [] #to remove duplicate matches
match_group =[] # matches
person = {}
interest_group = {}
#------------------------------part 1----------------------------------
#sample result: {"person1": ["interest", "interest3", "interest4"] }
for i in choice:
    if i in choice:
        match = choice.get(i)
        for k in range(len(match)):
            person[i] = match
    else:
        print("Uh oh, I don't know about that item")

#----------------------------part 2------------------------------------
# invert the group for matching
inverted_group = {}
for key, value in person.items():
    for x in value:
        inverted_group.setdefault(x, list()).append(key)

#invert context dictionary in everything
#inverted_group = {'interest': ['person1'], 'interest4': ['person1']...etc}
#----------------------------part 3------------------------------------
#remove duplicate users in interests
#return True if seen, False if not
def spotted(person, plist):
    for i in plist:
        if(i == person):
            return True #has been spotted
    return False #has not been seen
#----------------------------part 4------------------------------------
#start matching the users
for i in current_user: #interest3
    for n in inverted_group: #interest3
        if n == i: #interest3 == interest3
            p = inverted_group.get(i)
            for x in p:
                location.setdefault(x, list()).append(n)
                 #put all seen people into seen list
                if(spotted(x, seen) == False): #if spotted returns False, which means person is not in list 
                    match_group.append(x) #get all values from context dictionary key and put them into match_group
                    seen.append(x)
for key, value in location.items():
    for x in value:
        interest_group.setdefault(x, list()).append(key)                    

print('group ', interest_group,'\n') #NOTE: this could be for posts section, but would require a model to do so 
print('matches: ', match_group,'\n')
print('location matched: ', location, '\n')

#Same algorithm, just no comments
people = {
'person1': ['interest','interest3', 'interest4', 'interest5'], 
'person2': ['interest', 'interest4', 'interest5','interest6','interest2','interest9','interest3'],
'person3': ['interest6 ', 'interest4', 'interest5', 'interest3', 'interest2', 'interest', 'interest10'],
'person4': ['interest7', 'interest4', 'interest6','interest8','interest9','interest10'],
'person6': ['interest', 'interest4','interest5', 'interest6','interest7','interest8','interest9'],
'person7': ['interest', 'interest3', 'interest2', 'interest1','interest6','interest7','interest8'],
'person8': ['interest', 'interest4', 'interest5','interest6','interest7'],
'person10': ['interest3', 'interest4', 'interest6','interest7','interest8','interest9'],
'person11': ['interest', 'interest7', 'interest8', 'interest5'],
'person12': ['interest2', 'interest4', 'interest8','interest9', 'interest10', 'interest3', 'interest7', 'interest6'],
'person13': ['interest5', 'interest6', 'interest10', 'interest7', 'interest2'],
'person14': ['interest3', 'interest4', 'interest8', 'interest10', 'interest9', 'interest7'],
'person15': ['interest', 'interest4', 'interest5', 'interest6', 'interest8', 'interest0'],
}
current_user = people.get('person3')
people.pop('person3')
choice = people
location = {}
seen = [] 
match_group =[]
person = {}
interest_group = {}

for i in choice:
    if i in choice:
        match = choice.get(i)
        for k in range(len(match)):
            person[i] = match
    else:
        print("Uh oh, I don't know about that item")

inverted_group = {}
for key, value in person.items():
    for x in value:
        inverted_group.setdefault(x, list()).append(key)

def spotted(person, plist):
    for i in plist:
        if(i == person):
            return True 
    return False 
#for current user
var = 0; 
#for dictionary
var2 = 0;
for i in current_user:
    while current_user[var] == inverted_group.keys[var2]:
        p = inverted_group.get(i)
        #try a faster time complexity here, put while loop inside for loop
        for x in p:
            location.setdefault(x, list()).append(n)
            if(spotted(x, seen) == False): 
                match_group.append(x) 
                seen.append(x)
    var += 1
    var2 += 1
                    
for key, value in location.items():
    for x in value:
        interest_group.setdefault(x, list()).append(key)                    

print('group ', interest_group,'\n') 
print('matches: ', match_group,'\n')
print('location matched: ', location, '\n')

