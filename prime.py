# coding=utf-8
import math

def sieve_of_eratosthenes(n):#埃拉托色尼筛选法，返回少于n的素数
  primes = [True] * (n+1)#范围0到n的列表
  p = 2#这是最小的素数
  while p * p <= n:#一直筛到sqrt(n)就行了
    if primes[p]:#如果没被筛，一定是素数
      for i in range(p * 2, n + 1, p):#筛掉它的倍数即可
        primes[i] = False
    p += 1
  primes = [element for element in range(2, n) if primes[element]]#得到所有少于n的素数
  return primes
 
def isPrime(n):
  if n % 5 != 0 and n % 7 != 0:    # 判断一个属于是否能被5或7整除
    return True    # 真，则为质数
  else:
    return False
HRNUM = 707829217
daixuan = []
print sieve_of_eratosthenes(100)
def findPrime(arr):
  for num in arr:
    if isPrime(HRNUM / num):
      daixuan.append(num)
  
  print daixuan


findPrime(sieve_of_eratosthenes(100))