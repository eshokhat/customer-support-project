from faker import Faker
import pandas as pd
import random

fake = Faker()
data = []
for _ in range(50000):
    data.append({
        "ticket_id": fake.uuid4(),
        "date_opened": fake.date_this_year(),
        "channel": random.choice(["Phone","App","Website"]),
        "issue_type": random.choice(["Limit","Refund","Block Card","Tech"]),
        "time_to_resolution": random.randint(1,72),
        "status": random.choice(["Resolved","Escalated","Reopened"])
    })
df = pd.DataFrame(data)
df.to_csv("dataset.csv", index=False)
