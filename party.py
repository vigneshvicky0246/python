def findGuest(guests, N):
	count = 0
	for i in range(N):
		if guests[i] <= count:
			count += 1
	return count

N = 5
guests = [7,0,5,1,3]
totalGusets = findGuest(guests, N)
print(totalGusets)
