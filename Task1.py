from itertools import combinations

# Define the sets of artists for each DJ
djs = {
    "Kevin": {"Halsey", "Taylor Swift", "Mitski", "Joji", "Shawn Mendes", "Sabrina Carpenter", "Nicky Minaj", "Conan Gray", "One Direction", "Justin Bieber"},
    "Stuart": {"Kendrick Lamar", "Steve Lacy", "Tyler the Creator", "Joji", "TheWeeknd", "Coldplay", "Kanye West", "Travis Scott", "Frank Ocean", "Brent Faiyaz"},
    "Bob": {"Conan Gray", "Joji", "Dove Cameron", "Mitski", "Arctic Monkeys", "Steve Lacy", "Kendrick Lamar", "Isabel LaRosa", "Shawn Mendes", "Coldplay"},
    "Edith": {"Metallica", "Billie Eilish", "TheWeeknd", "Mitski", "NF", "Conan Gray", "Kendrick Lamar", "Nicky Minaj", "Kanye West", "Coldplay"}
}

# Function to calculate the overlap percentage between two sets
def overlap_percentage(set1, set2):
    intersection = set1 & set2
    return (len(intersection) / len(set1)) * 100, (len(intersection) / len(set2)) * 100

# Generate all possible DJ pairs
pairs = list(combinations(djs.keys(), 2))

# Initialize a list to store the results
results = []

# Iterate over each pair and calculate the overlap percentage
for pair in pairs:
    dj1, dj2 = pair
    set1, set2 = djs[dj1], djs[dj2]
    overlap1, overlap2 = overlap_percentage(set1, set2)
    # Check if the overlap is at least 30% for both DJs
    if overlap1 >= 30 and overlap2 >= 30:
        # Calculate the average overlap percentage
        avg_overlap = (overlap1 + overlap2) / 2
        results.append((dj1, dj2, avg_overlap))

# Sort the results based on the average overlap percentage
results.sort(key=lambda x: x[2], reverse=True)

# Print the results
for pair in results:
    print(f"DJ Pair: {pair[0]} and {pair[1]}, Average Overlap: {pair[2]:.2f}%")