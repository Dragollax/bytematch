passed = []
once = False
class Match:
    def complex_match(*args, **kwargs):

        matches = []

        match_data = args[1]

        target = args[0]
        
        matchedData = [] 


        for user in match_data: #NOTE: change this later!!
            matched=[]
            for attribute in user.get('interests'):
                #will compare key from modified_user with userInterest    
                #this will prevent us from having another nested for loop and waste time iterating through the user's interest every time
                if attribute in target: 
                    matched.append(attribute)
                    user['matchedPercentage']=((len(matched)+1)/(len(user.get('interests'))+2)+(len(matched)+1)/(len(target)+2))/2
                    user['matchedAttributes']=matched
                    matchedData.append(user)
                    
        matchedData.sort(key=lambda x: x.get('matchedPercentage'), reverse=True)

        for x in matchedData: #to remove duplicate dictionaries from list
            if x not in matches:
                matches.append(x)
        results = {
            "matched": matches,
        }
        return results
        
    def quick_match(*args,  **kwargs):
        #data group for matching
        match_data = args[1]
        #target for matching, shouyld be in list data structure
        target = args[0]
        i = 0 #will be used to iterate through interests
        j = 0 #will be used to iterate through the current user's interests
        once = False#just ot make sure we only assign inverted_group's length to length once
        length = 0
        raw_matches = []
        #this will stop the algo if we have reached the end of the user's interests. 
        while i < len(target) or j < length: 
            #matchedInterests = []
            if once == False:
                once = True
                length = len(match_data)
            
            if int(target[i]) == int(list(match_data.keys())[j]): #if the j'th value of inverted_group is equal to the i'th value of current_user
                j += 1
                matched = match_data.get(str(target[i]))

                raw_matches.extend(matched)

                    
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
