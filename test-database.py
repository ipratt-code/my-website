from replit import db

#db["key"] = "value"
for key in db.keys():
	print(db[key])
	del db[key]