from diffusion import EnvModel
from matplotlib import pyplot as plt
import numpy as np

init_agents = 20
w = 10
h = 10

model = EnvModel(init_agents, w, h)

# Lists contain number of each type of agents after every step
movable_particles = []
immovable_particles = []

# An array to represent space
space = np.zeros((w, h))

# Run this model 50 steps
for i in range(50):
    model.step()
    count = 0
    for agent in model.schedule.agents:
        if agent.type:
            count += 1
    movable_particles.append(count)
    immovable_particles.append(init_agents - count)

# Get the immovable agents at the end
for cell in model.grid.coord_iter():  # loop through each cell
    cell_content, x, y = cell  # get list of all agents, and location from that cell
    num_imm_particles = len(
        [agent for agent in cell_content if agent.type == False])
    space[x][y] += num_imm_particles

# plt.subplot(1, 2, 2)
plt.figure(1)
plt.title('Number of immovable particles on space at the end')
plt.imshow(space)
plt.colorbar()

# plt.subplot(1, 2, 1)
plt.figure(2)
plt.plot(movable_particles, label='Number of mov_particles', color='b')
plt.plot(immovable_particles, label='Number of imm_particles', color='r')
plt.title('Number of each type of partices through time')
plt.legend(loc='center')

plt.show()
