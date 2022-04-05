from typing import List
def sol(plates: List[str]) -> str:
    dic = {chr(65+i) : i for i in range(26)}
    ans = []

    for plate in plates:
        plate_a, plate_b = plate.split('-')

        value_plate_a = sum([dic[v] * (26 ** i) for i,v in enumerate(plate_a[::-1])])
        value_plate_b = int(plate_b)

        is_nice_plate = abs(value_plate_a - value_plate_b) <= 100
        ans.append("nice" if is_nice_plate else "not nice")

    return '\n'.join(ans)

t = int(input())
plates = [input() for _ in range(t)]
print(sol(plates))