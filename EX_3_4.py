import matplotlib.pyplot as plt

a = [1, 2, 3, 4, 5]
b = [0, 0.6, 0.2, 15, 10, 8, 16, 21]
c = [4, 2, 6, 8, 3, 20, 13, 15]

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Subplot 1: Blue squares
axs[0, 0].plot(a, 'sb')
axs[0, 0].set_title('1st Rep')

# Subplot 2: Red circles
axs[0, 1].plot(b, 'or')
axs[0, 1].set_title('2nd Rep')

# Subplot 3: Green triangles down
axs[1, 0].plot(list(range(0, 22, 3)), 'vg')
axs[1, 0].set_title('3rd Rep')

# Subplot 4: Magenta diamonds with custom Y-ticks
axs[1, 1].plot(c, 'Dm')
axs[1, 1].set_yticks(list(range(0, 24, 4)))
axs[1, 1].set_title('4th Rep')

plt.tight_layout()
plt.show()
