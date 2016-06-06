import matplotlib.pyplot as plt
from collections import Counter

suites = [line.rstrip('\n') for line in open('suites_openssl.txt')]
usage = [line.rstrip('\n') for line in open('used_suites1.txt')]

cntr = Counter(usage)

plt.figure()
ax = plt.subplot(111)
ax.bar(range(0,25), cntr.values()[0:25])
ax.set_xticks(map(lambda x: x + 0.5, range(0,25)))
ax.set_xticklabels(cntr.keys()[0:25], rotation=90)
ax.set_ylabel('Number of sites')

plt.figure()
ax = plt.subplot(111)
ax.bar(range(0,25), cntr.values()[25:50])
ax.set_xticks(map(lambda x: x + 0.5, range(0,25)))
ax.set_xticklabels(cntr.keys()[25:50], rotation=90)
ax.set_ylabel('Number of sites')

plt.figure()
ax = plt.subplot(111)
ax.bar(range(0,25), cntr.values()[50:75])
ax.set_xticks(map(lambda x: x + 0.5, range(0,25)))
ax.set_xticklabels(cntr.keys()[50:75], rotation=90)
ax.set_ylabel('Number of sites')

plt.figure()
ax = plt.subplot(111)
ax.bar(range(0,25), cntr.values()[75:100])
ax.set_xticks(map(lambda x: x + 0.5, range(0,25)))
ax.set_xticklabels(cntr.keys()[75:100], rotation=90)
ax.set_ylabel('Number of sites')

all_used = len(cntr.values())
plt.figure()
ax = plt.subplot(111)
ax.bar(range(0,all_used-100), cntr.values()[100:all_used])
ax.set_xticks(map(lambda x: x + 0.5, range(0,all_used-100)))
ax.set_xticklabels(cntr.keys()[100:all_used], rotation=90)
ax.set_ylabel('Number of sites')

plt.show()
