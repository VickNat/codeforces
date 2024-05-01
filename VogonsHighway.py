size = int(input())

for _ in range(size):
    mach1, mach2 = list(map(int, input().split()))
    planets = list(map(int, input().split()))

    counts = 0
    checkPlanet = []

    for idx in range(mach1 + 1):
        if planets[idx] not in checkPlanet:
            checkPlanet.append(planets[idx])
            counts += mach2

    cost = min(counts, mach1)

    print(cost)