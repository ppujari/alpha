
# Example traffic record
#        traffic_rec = {
#        "store_id":"100",
#        "time_stamp":,
#        "people_count":0,
#        "gender": M,
#        "age_group":"40-55"
#        }

from pymongo import MongoClient





def write_to_mongo(mongo_docs, ip='localhost', collection='traffic_data', database='alpha'):

    print ("Connecting to mongodb ..")
    batch_count = 100

    try :
        client = MongoClient(ip, 27017)
        db = client[database]
        col = db[collection]
        if len(mongo_docs) == batch_count:
            col.insert_many(mongo_docs)
            mongo_docs = []
       
        if len(mongo_docs) > 0:
            col.insert_many(mongo_docs)
        print ( " Inserted row count: " , col.count())
    except Exception as e:
        print(e) 
        pass



