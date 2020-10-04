# coding=utf-8
# 求递归求数字根
def digital_root(n):
  str_n = str(n)
  sigma = 0
  for i in range(len(str_n)):
    sigma += int(str_n[i])
  if sigma >= 10:
    return digital_root(sigma)
  else:
    return sigma

print(digital_root(78579597657597598758975974764768538653865386))