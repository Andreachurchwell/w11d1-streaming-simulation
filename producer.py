# import json
# import uuid

# from confluent_kafka import Producer

# producer_config = {
#     "bootstrap.servers": "localhost:9092"
# }

# producer = Producer(producer_config)

# def delivery_report(err, msg):
#     if err:
#         print(f"❌ Delivery failed: {err}")
#     else:
#         print(f"✅ Delivered {msg.value().decode("utf-8")}")
#         print(f"✅ Delivered to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}")

# order = {
#     "order_id": str(uuid.uuid4()),
#     "user": "lara",
#     "item": "frozen yogurt",
#     "quantity": 10
# }

# value = json.dumps(order).encode("utf-8")

# producer.produce(
#     topic="orders",
#     value=value,
#     callback=delivery_report
# )

# producer.flush()


import json
import time
import uuid
import random
from confluent_kafka import Producer

# Kafka config - talks to the broker running in Docker
producer_conf = {
    "bootstrap.servers": "localhost:9092"
}

producer = Producer(producer_conf)

# Our custom topic for this assignment
TOPIC = "nba_bets"


def delivery_report(err, msg):
    """Callback that reports if the message was successfully delivered."""
    if err is not None:
        print(f"❌ Delivery failed: {err}")
    else:
        print(
            f"✅ Delivered to {msg.topic()} "
            f": partition {msg.partition()} : at offset {msg.offset()}"
        )


def make_bet_event():
    """Create one fake SheBETS-style bet event."""
    games = [
        "Grizzlies vs Thunder",
        "Lakers vs Warriors",
        "Celtics vs Knicks",
        "Suns vs Nuggets",
    ]
    bet_types = ["spread", "moneyline", "over_under"]
    picks = [
        "home_team",
        "away_team",
        "over",
        "under",
    ]

    return {
        "event_id": str(uuid.uuid4()),
        "user": "andrea_shebets",
        "game": random.choice(games),
        "bet_type": random.choice(bet_types),
        "pick": random.choice(picks),
        "wager_amount": random.choice([5, 10, 15, 20, 25]),
        "timestamp": int(time.time()),
    }


if __name__ == "__main__":
    print("🎲 Sending NBA bet events to Kafka topic 'nba_bets'...")
    for _ in range(5):
        bet_event = make_bet_event()
        data = json.dumps(bet_event).encode("utf-8")

        # Send the event to Kafka
        producer.produce(
            topic=TOPIC,
            value=data,
            callback=delivery_report,
        )

        print(
            f"🎲 Sent bet: {bet_event['user']} bet ${bet_event['wager_amount']} "
            f"on {bet_event['bet_type']} ({bet_event['pick']}) in {bet_event['game']}"
        )

        # Let the producer handle any delivery callbacks
        producer.poll(0)
        time.sleep(1)

    producer.flush()
    print("✅ Done sending bets.")

