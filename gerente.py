from funcionario import Funcionario

class Gerente (Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtde_fuuncionarios):
        super().__init__(nome, cpf, salario, senha)
        self._qtde_funcionarios = qtde_fuuncionarios

    @property
    def qtde_funcionarios(self):
        return self._qtde_funcionarios
        
    @qtde_funcionarios.setter
    def qtde_funcionarios(self, qtde_funcionarios):
        self._qtde_funcionarios = qtde_funcionarios