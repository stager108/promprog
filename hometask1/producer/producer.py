
#!/usr/bin/env python
import pika
import time
time.sleep(30)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672))
channel = connection.channel()


channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Test Message')
print "Sent 'Test Message'"
connection.close()

