from models.rl_ia_models import Agent, State
from set_up import planes_de_carreras, cuatrimestres_cursados, materias_por_cursar

nerd = Agent(alpha=0.7)
nerd.learn_career_plans(planes_de_carreras)
initial_state = State(cuatrimestres_cursados, materias_por_cursar)
my_plan = nerd.make_career_plan(initial_state)

print (my_plan)