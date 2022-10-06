import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True, health_check_interval=2)

q = r.pubsub()
q.subscribe('channel_a')

print('Enter Message')
m = input()
m = '{"message": "' + m + '"}'

r.publish("channel_a", m)
