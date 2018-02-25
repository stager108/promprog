#!/usr/bin/env python
import pika
from peewee import *
import time
time.sleep(30)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672))
channel = connection.channel()

channel.queue_declare(queue='hello')


myDB = PostgresqlDatabase('postgres', user='user', password='password', host='dtbs', port=5432)
myDB.connect()

class MyPostgresModel(Model):
    class Meta:
        database = myDB

class Message(MyPostgresModel):
    content = CharField()


MODELS = [Message]
myDB.create_tables(MODELS)


print 'Wait!'

def callback(ch, method, properties, body):
    print "Got a message %r" % (body)
    msg = Message(content=body)
    msg.save()

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()

dtbs.close()
