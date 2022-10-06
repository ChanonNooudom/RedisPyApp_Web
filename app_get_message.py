import redis
import time

#health check interval must be higher than get_message interval
#if get_message interval = 1, health check interval must be > 1
r = redis.Redis(host='localhost', port=6379, decode_responses=True, health_check_interval=2)

m = r.get("variable_a")
print(m)

q = r.pubsub()
q.subscribe("channel_a")
while True:
    try:
        m = q.get_message()
        if m:
            print(m)
        time.sleep(1)
    except:
        print("lost connection wtih redis server")

