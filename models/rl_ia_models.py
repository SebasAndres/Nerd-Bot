from .uni_models import *

def all_combinations (ls:list) -> list:
    """ 
    Receives a list of elements and returns another list of lists 
    with all the possible manners to pick elements from the original one.
    
    It works recursively, adding all_combs of tail list with the sum of 
    fst element to all_combs of tail list.

    Parameters:
        ls: List<Obj>
    
    Returns List<List<Obj>>
    """
    if len(ls) == 0:
        return [[]]
    elif len(ls) == 1:
        return [[], [ls[0]]]
    else:
        lst_combs = all_combinations(ls[:-1])
        return lst_combs + [c+[ls[-1]] for c in lst_combs]

class State ():
    # state de materias cursadas y por cursar
    def __init__ (self, cuatrimestres_cursados:list(), materias_por_cursar:list()):
        self.cuatrimestres_cursados = cuatrimestres_cursados
        self.materias_cursadas = []
        for cuatr in cuatrimestres_cursados:
            self.materias_cursadas += cuatr.materias # lista de materias
        self.materias_por_cursar = materias_por_cursar
        ult_cuatr = self.cuatrimestres_cursados[-1]
        self.fecha_ultimo_cuatrimestre = (ult_cuatr.year, ult_cuatr.n_cuatr)

    def possible_actions(self) -> list:
        materias_a_combinar = self.filtrar_por_correlatividad(
                    self.materias_cursadas,
                    self.materias_por_cursar
        )
        # pruebo eliminar el caso que se elige no estudiar nada
        return all_combinations(materias_a_combinar)[1:] 
        
    def filtrar_por_correlatividad(self, materias_cursadas,
                                         _materias_por_cursar) -> list:
        for materia in _materias_por_cursar:
            if materia.requirements in materias_cursadas:
                _materias_por_cursar.remove(materia)
        return _materias_por_cursar

    def __str__ (self):
        return (f"state:\nmaterias_cursadas: {[m.nombre for m in self.materias_cursadas]} "+ 
                 f"\nmaterias_por_cursar: {[m.nombre for m in self.materias_por_cursar]}")

class Environment ():
    # materias disponibles
    def __init__ (self, init_state):
        self.state = init_state

    def in_end_state (self):
        return len(self.state.possible_actions()) == 0

    def execute (self, materias_elegidas): # execute action
        """ 
        Updates materias_cursadas and materias_por_cursar adding/deleting selected \
        materias_elegidas.
        Parameters:
            materias_elegidas = List<Materias>
        """
        # agrego las materias estudiadas en el cuatrimestre a materias_cursadas
        # elimino las materias de las materias disponibles
        year, n_cuatr = self.state.fecha_ultimo_cuatrimestre
        for materia in materias_elegidas:
            self.state.materias_cursadas.append(materia)
            self.state.materias_por_cursar.remove(materia)
        return year, n_cuatr

class Agent ():
    def __init__ (self, alpha=0.5):
        self.alpha = alpha
        self.history = []
        self.career_plans = []

    def make_career_plan (self, initial_state) -> dict:
        """ 
        Returns a dict with the agents suggested career plan.
        Parameters:
            initial_state : State
        """
        environment = Environment(initial_state)
        while not environment.in_end_state():
            best_subjects = self.pick_best_action(environment.state) # state contiene metodo state.possible_actions()
            n_cuatr, year = environment.execute(best_subjects) # execute hace un environment.set_state(state')
            # hago un registro en la history del agent
            cuatrimestre = Cuatrimestre(best_subjects, n_cuatr, year)
            self.history.append(cuatrimestre)
        return self.pretty_print_history()

    def pretty_print_history(self):
        return {}

    def learn_career_plans (self, career_plans):
        self.career_plans = career_plans

    def R (self, state):
        """
        Returns a numerical reward from being in state s.
        Parameters:
            state : State
            (internal) planes_de_carrera
        """
        reward = 0
        for plan_de_carrera in self.career_plans:
            if plan_de_carrera.materias in state.materias_cursadas:
                reward += plan_de_carrera.reward
        return reward

    def Q (self, state, action):
        """
        Returns a numerical reward after applying action a from state s.
        Parameters:
            state : State
            action : List<Materias>
        """
        print (state)
        print ("action:",action)
        fake_env = Environment(state)
        fake_env.execute(action)
        post_action = self.pick_best_action(fake_env.state)
        return self.R(state) + self.alpha * self.Q(fake_env.state,post_action) 

    def pick_best_action (self, state):
        """ 
        Returns the suggested Cuatrimestre to study given a state.
        Parameters:
            state : State
        """
        possible_actions = state.possible_actions()
        if len(possible_actions) > 0:
            best_choice = (0, possible_actions[0])
            max = self.Q(state, possible_actions[0])
            for j, a_ in enumerate(possible_actions[1:]):
                val = self.Q(state, a_)
                if best_choice[1] >= max:
                    best_choice = (j, val)
            return best_choice
        return []