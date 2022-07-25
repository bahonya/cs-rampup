from pymongo import MongoClient
import pprint

client = MongoClient()
print(client.list_database_names())
db = client.physical_stores
print(db.list_collection_names())
receipts = db.receipts

print("(a)")
for receipt in receipts.find(
    {"salesperson": "Betty Lewis"}, projection={"_id": 0, "date": 1, "time": 1}
):
    pprint.pprint(receipt)

print("(b)")
print(
    receipts.count_documents(
        {
            "customer.first_name": "Jeffrey",
            "customer.last_name": "Martinez",
            "salesperson": "Betty Lewis",
        }
    )
)

print("(c)")
for receipt in receipts.find(
    {
        "customer.first_name": "Jeffrey",
        "customer.last_name": "Martinez",
        "salesperson": "Betty Lewis",
        "date": {"$gt": 20000826},
        "positions": {"$elemMatch": {'product_name' : 'W'}}
    }
):
    pprint.pprint(receipt)
