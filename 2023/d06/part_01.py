import math

print(
    math.prod(
        sum(i * (limit - i) > dist for i in range(dist))
        for limit, dist in zip([45, 97, 72, 95], [305, 1062, 1110, 1695])
    )
)