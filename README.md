<!-- # kafka-crash-course

### Install confluent-kafka dependency
`pip3 install confluent-kafka`

### Validate that the topic was created in kafka container
`docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092`

### Describe that topic and see its partitions
`docker exec -it kafka kafka-topics --bootstrap-server localhost:9092 --describe --topic new_orders`

#### View all events in a topic
`docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic orders --from-beginning` -->


## W11D1 Streaming Assignment – NBA Betting Simulation 🎬🏀
### Andrea Churchwell
#### Justice Through Code – Applied AI Solutions Engineering
#### December 2025

### 🌟 Overview

For this assignment, I built a real-time streaming setup using Kafka. I modeled the flow around NBA bets because it directly connects to a personal project I’ve been working on called SheBETS.

Actually seeing messages leave one terminal and instantly show up in another made streaming “click” for me — not just conceptually, but visually.

### 🏀 Why I Chose This Domain

SheBETS simulates NBA betting and tracks results. Since betting happens live and continuously, it fit perfectly into a streaming model.

Each event represents a realistic sports bet, including:

- game matchup

- bet type (spread, ML, over/under)

- pick (home, away, over, under)

- user that made the pick

- wager amount

- timestamp

Example bet event:
```

{
  "event_id": "8cd23c9e-93c3-4cd2-9040-6e1b151e57fb",
  "user": "andrea_shebets",
  "game": "Grizzlies vs Thunder",
  "bet_type": "spread",
  "pick": "home_team",
  "wager_amount": 15,
  "timestamp": 1733802902
}

```

**I loved this because it felt like something I might actually plug into my real project later.**

### 🔧 What I Customized

Compared to the original example from the tutorial, I changed the following:

| Original Example               | My Version                                    |
| ------------------------------ | --------------------------------------------- |
| Topic: `orders`                | Topic: `nba_bets`                             |
| Fields: orderId, item, user    | event_id, game, pick, wager_amount, timestamp |
| “Delivered pizza order...” log | “Sent bet...” log                             |
| Single order repeated          | Dynamic matchups, bet types, amounts          |


These changes made the simulation more realistic and directly aligned with how my real project would work.

### 🧠 Architecture (simple version)
producer.py  →  Kafka topic (nba_bets) →  tracker.py

✔ Producer creates NBA bet events
✔ Kafka carries them
✔ Consumer prints them instantly

Seeing the pipeline run in real-time was the coolest part.

### 🚀 How To Run This
1️⃣ Start Kafka
```
docker compose up -d
```
Confirm it is running:
```
docker ps
```
2️⃣ Run Consumer (Terminal #1)
```
python tracker.py
```

Expected output:
```
🟢 Listening for bets...
🏀 New bet from andrea_shebets: $10 on spread (home_team) in Hawks vs Bulls
```
Keep this running.

3️⃣ Run the Producer (Terminal #2)
```
python producer.py
```

Example output:
```
🎲 Sent bet: $15 on over in Warriors vs Lakers

```
Run it multiple times — streaming makes more sense visually.

📸 Screenshots
Real-Time Consumer Output
<img src="assets/terminal_output.png" width="600">


<div align="center"> <img src="assets/shebet.png" width="350"> </div>

### 🔗 How This Connects to My Real Project

SheBETS currently processes bets after they're placed.
After doing this assignment, I can clearly see how a streaming model could change that:

💡 Bets could enter Kafka instead of going directly into storage
💡 Separate consumers could update stats
💡 Another consumer could track streaks
💡 Results could update user balances automatically
💡 A UI could show bets as they happen

Now it makes sense how sports apps show data “in motion.”

### 🧠 What I Learned

Not from slides — from watching actual terminals talk back and forth:

✔ How JSON events move end-to-end
✔ What topics are and how consumers subscribe
✔ Kafka holds messages even between reads
✔ Real-time communication is literally real-time

That visual connection changed everything.

### 🧰 Tools Used

- Python

- Kafka (through Docker)

- confluent-kafka

- VS Code

🎯 Final Outcome

A working streaming system that models real NBA betting behavior and gives me a clear vision of how future SheBETS features could work using real-time events.

### 🙌 Shoutout

A huge thank-you to this YouTube walkthrough for helping everything make sense visually and step-by-step:

⭐ Kafka Crash Course — Python Coding Tutorial by TechWorld with Nana
https://www.youtube.com/watch?v=B7CwU_tNYIE

Her walkthrough was exactly what I needed to tie the concepts together and actually see streaming in motion.
