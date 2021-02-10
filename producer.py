import json

import boto3


queue_name = "SQS QUEUE NAME HERE"

sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName = queue_name)

orders = [
            {'id':1, 'item': 'Tesla Model S'},
            {'id':2, 'item': 'Tesla Model 3'},
            {'id':3, 'item': 'Tesla Model X'},
            {'id':4, 'item': 'Tesla Model Y'},
            {'id':5, 'item': 'Cybertruck'}
         ]

for order in orders:
    response = queue.send_message(MessageBody = json.dumps(order))
    #print(response)
    print(f"Your order {order['item']} has been placed!")


