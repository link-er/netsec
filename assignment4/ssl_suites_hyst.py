import matplotlib.pyplot as plt
from collections import Counter

suites = [line.rstrip('\n') for line in open('suites_openssl.txt')]
usage = [line.rstrip('\n') for line in open('used_suites.txt')]

cntr = Counter(usage)

plt.rcParams.update({'font.size': 8})
plt.figure()
ax = plt.subplot(111)
quant = len(cntr.values())
ax.bar(range(0,quant), cntr.values())
ax.set_xticks(map(lambda x: x + 0.5, range(0,quant)))
ax.set_xticklabels(cntr.keys(), rotation=90)
ax.set_ylabel('Number of sites')

plt.show()
