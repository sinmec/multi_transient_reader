import numpy as np
from matplotlib import pyplot as plt


class ElongatedBubble():
    def __init__(self, H, L):
        self.L = L
        self.H = H
        self.alpha = (1.0 - self.H)

class LiquidSlug():
    def __init__(self, H, L):
        self.L = L
        self.H = H
        self.alpha = (1.0 - self.H)

class SlugUnit():
    def __init__(self):
        self.liquid_slug = None
        self.elongated_bubble = None

# class TransientSignal():
#     slug_unit =[]
#     def __init__(self,create_signal):
#         self.slug_unit = slug_unit
#         self.create_signal =
#     def sdsfs(self):
#         self.signal =


delta_x = 0.01
slug_unit_colection = []
for i in range(20):

    L_LS = np.random.uniform(low=2*delta_x, high=1.0, size=1)
    H_LS = 1
    liquid_slug = LiquidSlug(H_LS, L_LS)

    L_EB = np.random.uniform(low=2*delta_x, high=1.0, size=1)
    H_EB = 0.01
    elongated_bubble = ElongatedBubble(H_EB, L_EB)

    slug_unit = SlugUnit()
    slug_unit.elongated_bubble = elongated_bubble
    slug_unit.liquid_slug = liquid_slug
    slug_unit_colection.append(slug_unit)


holdup_slug_unit_total = []
for slug_unit in slug_unit_colection:
    N_EB = int(slug_unit.elongated_bubble.L / delta_x)
    N_LS = int(slug_unit.liquid_slug.L / delta_x)

    holdup_slug_unit = np.zeros((N_EB + N_LS), dtype=float)
    holdup_slug_unit[:N_LS] = slug_unit.liquid_slug.H
    holdup_slug_unit[N_LS:] = slug_unit.elongated_bubble.H

    holdup_slug_unit_total.append(holdup_slug_unit)


holdup_slug_unit_total = np.concatenate(holdup_slug_unit_total)
for i in range(1,10,1):
    slug_unit_signal=[]
    holdup_slug_unit_total_new = np.roll(holdup_slug_unit_total, shift=i)
    slug_unit_signal.append(holdup_slug_unit_total_new)


pipe_length = len(holdup_slug_unit_total) * delta_x
length = np.linspace(0, pipe_length, len(holdup_slug_unit_total))


plt.plot(length, holdup_slug_unit_total, color = "red")
plt.plot(length, holdup_slug_unit_total_new, color = "blue")
plt.show()
a = 2