import json

import boto3


queue_name = 'SQS QUEUE NAME HERE'

sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName=queue_name)

for message in queue.receive_messages():
    #print(f'raw message: {message.body}')
    order = json.loads(message.body)
    print(f"Your order {order['item']} has been shipped!")
    message.delete()