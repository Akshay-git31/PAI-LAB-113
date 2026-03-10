def reflex_vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Left"

roomA = input("Enter status of Room A (Dirty/Clean): ")
roomB = input("Enter status of Room B (Dirty/Clean): ")

env = {"A": roomA, "B": roomB}

location = input("Enter initial location of vacuum (A/B): ")

while env["A"] == "Dirty" or env["B"] == "Dirty":
    status = env[location]
    action = reflex_vacuum_agent(location, status)

    print("Location:", location, "| Status:", status, "| Action:", action)

    if action == "Suck":
        env[location] = "Clean"
    elif action == "Right":
        location = "B"
    elif action == "Left":
        location = "A"

print("Final Environment:", env)
