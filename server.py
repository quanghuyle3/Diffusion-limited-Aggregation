
from diffusion import EnvModel

from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer


def particle_agent(agent):
    portrayal = {'Shape': 'circle',
                 'r': 0.5,
                 'Filled': 'true'}

    if agent.type:
        portrayal['Color'] = 'blue'
        portrayal['Layer'] = 1
        portrayal['r'] = 0.3
    else:
        portrayal['Color'] = 'red'
        portrayal['Layer'] = 0

    return portrayal


grid = CanvasGrid(particle_agent, 10, 10, 500, 500)
chart = ChartModule([{'Label': 'Num_mov_agents', 'Color': 'Black'}])

server = ModularServer(EnvModel, [
                       grid, chart], "Diffusion-limited Aggregation", {'N': 80, 'width': 10, 'height': 10})

server.launch()
