# import json

# from confluent_kafka import Consumer

# consumer_config = {
#     "bootstrap.servers": "localhost:9092",
#     "group.id": "order-tracker",
#     "auto.offset.reset": "earliest"
# }

# consumer = Consumer(consumer_config)

# consumer.subscribe(["orders"])

# print("🟢 Consumer is running and subscribed to orders topic")

# try:
#     while True:
#         msg = consumer.poll(1.0)
#         if msg is None:
#             continue
#         if msg.error():
#             print("❌ Error:", msg.error())
#             continue

#         value = msg.value().decode("utf-8")
#         order = json.loads(value)
#         print(f"📦 Received order: {order['quantity']} x {order['item']} from {order['user']}")
# except KeyboardInterrupt:
#     print("\n🔴 Stopping consumer")

# finally:
#     consumer.close()


import json
from confluent_kafka import Consumer

TOPIC = "nba_bets"

consumer_conf = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "nba-bets-consumers",
    "auto.offset.reset": "earliest",  # read from the beginning if no offsets stored
}


def main():
    consumer = Consumer(consumer_conf)
    consumer.subscribe([TOPIC])

    print(f"🟢 Consumer is running and subscribed to '{TOPIC}' topic")

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue

            if msg.error():
                print(f"❌ Consumer error: {msg.error()}")
                continue

            data = msg.value()
            bet_event = json.loads(data.decode("utf-8"))

            user = bet_event["user"]
            game = bet_event["game"]
            bet_type = bet_event["bet_type"]
            pick = bet_event["pick"]
            amount = bet_event["wager_amount"]

            print(
                f"🏀 New bet from {user}: ${amount} on {bet_type} "
                f"({pick}) in {game}"
            )

    except KeyboardInterrupt:
        print("\n👋 Stopping consumer...")
    finally:
        consumer.close()
        print("✅ Consumer closed.")


if __name__ == "__main__":
    main()

