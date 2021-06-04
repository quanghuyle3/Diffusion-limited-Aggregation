from mesa import Agent, Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation


class ParticleAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        # True: movable, False: immovable
        self.type = self.random.choice([True, False])

    def step(self):
        if self.type:  # if this is a movable particle
            # Randomly move to new position
            x = self.random.randrange(self.model.grid.width)
            y = self.random.randrange(self.model.grid.height)
            self.model.grid.move_agent(self, (x, y))

            # Check if any immovable at that postion, if so, become immovable
            cellmates = self.model.grid.get_cell_list_contents(self.pos)
            if len(cellmates) > 0:
                for cm in cellmates:
                    if cm.type == False:
                        self.type = False
                        break


class EnvModel(Model):
    def __init__(self, N, width, height):

        self.num_agents = N

        # Schedule (list contains all agents)
        self.schedule = RandomActivation(self)

        # Grid
        self.grid = MultiGrid(width, height, True)

        for i in range(self.num_agents):
            # Initialize agent
            agent = ParticleAgent(i, self)
            self.schedule.add(agent)
            # Place this agent in space
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x, y))

    def step(self):
        self.schedule.step()
