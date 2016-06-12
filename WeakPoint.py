def golf(m):a = list(map(sum,m));b = list(map(sum,list(zip(*m))));return [a.index(min(a)),b.index(min(b))]
