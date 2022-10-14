import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['AttendanceProject']
# collection = db['superadmin_createaccounts']