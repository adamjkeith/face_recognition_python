print("Who would you like to vote for?")
print("\nCandidate A")
print("Candidate B")
while True:
    q = input("\nCadidate: ").lower()
    if q == "a" or q == "b":
        break
    else:
        print("Sorry unrecognised input, please type 'A' or 'B'")

print("\nYou have successfully voted for Cadidate",q.upper())
input('Press ENTER to exit')
