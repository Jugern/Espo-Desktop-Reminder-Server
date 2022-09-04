from espo_api_client import EspoAPI

client = EspoAPI('http://Espo', '5316bb3cf3bb7a40d6288f95e63b48cd')

# Create a lead
# data = {
#     'firstName': 'John',
#     'lastName': 'Does',
#     'phoneNumber': '+11111-22222-33333',
#     'source': 'Web Site',
#     'assignedUserId': '1',
#     'industry': 'Legal',
# }
# print(client.request('POST', 'Lead', data))
#
# # Update
# print(client.request('PUT', 'Lead/5b3c37b74b19680f1', {'lastName': 'Alice'}))
#
# # Get accounts
print(client.request('GET', 'Task'))
#
# # Get accounts with search params
# params = {
#     "select": "id,phoneNumber",
#     "where": [
#         {
#             "type": "equals",
#             "attribute": "phoneNumber",
#             "value": '+1',
#         },
#     ],
# }
# print(client.request('GET', 'Account', params))
#
# # Delete an opportunity
# print(client.request('DELETE', 'Opportunity/5b3b0b8c0b2b8bea5'))