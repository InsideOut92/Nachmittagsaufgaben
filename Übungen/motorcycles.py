motorcycles = ['honda', 'suzuki', 'yamaha', 'ducati', 'pegasus']
print(motorcycles)
last_owned = motorcycles.pop()
print(motorcycles)

print("\nThe last motorcycle I owned was a " + last_owned)

first_owned = motorcycles.pop(0)

print(f"\nThe first motorcycle I ever had was a {first_owned.title()}")

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me :( ")
