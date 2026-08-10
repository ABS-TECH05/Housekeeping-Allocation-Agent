from pathlib import Path
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(
    BASE_DIR / "data" / "processed" / "housekeeping_dataset.csv"
)

print("Dataset Loaded")
print(df.shape)

import pandas as pd
import numpy as np


# Load processed dataset
df = pd.read_csv(
    "data/processed/housekeeping_dataset.csv"
)


# Create housekeeping staff
staff = pd.DataFrame({
    "staff_id": range(1, 11),
    "staff_name": [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Emma",
        "Frank",
        "Grace",
        "Henry",
        "Ivy",
        "Jack"
    ]
})


# Select rooms needing attention
rooms = df[
    df["room_status"] == "Dirty"
].copy()


# Priority mapping
priority_map = {
    "High": 3,
    "Medium": 2,
    "Low": 1
}

rooms["priority_score"] = (
    rooms["housekeeping_priority"]
    .map(priority_map)
)


# Sort rooms
rooms = rooms.sort_values(
    by=[
        "priority_score",
        "checkout_hour"
    ],
    ascending=[
        False,
        True
    ]
)


allocations = []

for i, (_, room) in enumerate(
    rooms.iterrows()
):

    staff_member = staff.iloc[
        i % len(staff)
    ]

    allocations.append({
        "room_id": room["room_id"],
        "hotel_name": room["hotel_name"],
        "priority": room["housekeeping_priority"],
        "checkout_hour": room["checkout_hour"],
        "assigned_staff":
            staff_member["staff_name"]
    })


allocation_df = pd.DataFrame(
    allocations
)

allocation_df["task_status"] = "Pending"

allocation_df["estimated_finish_hour"] = (
    allocation_df["checkout_hour"] + 1
)

allocation_df.to_csv(
    BASE_DIR / "data" / "processed" / "housekeeping_plan.csv",
    index=False
)

print("\nHousekeeping Plan Generated")
print(
    allocation_df.shape
)

print(
    allocation_df.head(20)
)