limit, dist = 45977295, 305106211101695
print(sum(i * (limit - i) > dist for i in range(limit)))