import re
import time
import datetime

# function : check if word present in comment
def search_word(word, text):
    if word in text:
        return True
    return False
    
    # ignore the correct solution ...
    words = re.split(r"[ ,:;!?()\.]", text)
    if word in words:
        return True
    return False



# get the timestamps of given time interval
dt1 = datetime.datetime(year=2016, month=6, day=15)
dt2 = datetime.datetime(year=2016, month=7, day=15)
t1 = int(time.mktime(dt1.timetuple()))
t2 = int(time.mktime(dt2.timetuple()))


# read data
n, m = [ int(x) for x in input().split()]

passions = []
reviews = [] 

for i in range(n):
    p = input().strip().lower()    
    passions.append(p)
  
for j in range(m):
    uid, timestamp = [int(x) for x in input().split()]
    comment = input().strip().lower()    
    reviews.append((uid, timestamp, comment))

    
# process data
for passion in passions:
    scores = {}    
    
    for uid, timestamp, comment  in reviews:        
        if search_word(passion, comment):            
            score = 0
            
            if timestamp >= t1 and timestamp < t2:
                score += 20
            else:
                score += 10
                
            if len(comment) >= 100:
                score += 20
            else:
                score += 10
                
            if uid in scores:
                scores[uid] += score
            else:
                scores[uid] = score
            
    max_score = -1
    best_uid = -1
    for uid, score in scores.items():
        if score > max_score:
            max_score = score
            best_uid = uid
        elif score == max_score:
            if uid < best_uid:
                best_uid = uid
                
    print(best_uid)
            
    
