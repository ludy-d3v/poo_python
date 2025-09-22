class Participante:
    def __init__ (self, nome, email):
        self._nome = nome
        self._email = email
    
    def emitirCertificado(self):
        print(f"\nCertificado emitido para {self._nome} ({self._email})")
    
class Aluno(Participante):
    def __init__ (self, nome, email, curso):
        super().__init__(nome, email)
        self.__curso = curso
    
    def get_curso(self):
        return self.__curso
    
    def emitirCertificado(self):
        print(f"\nCertificado emitido de conclusão do curso de {self.__curso} para {self._nome} ({self._email})")
    
class Instrutor(Participante):
    def __init__ (self, nome, email, especialidade):
        super().__init__(nome, email)
        self.__especialidade = especialidade

    def get_especialidade(self):
        return self.__especialidade
        
    def emitirCertificado(self):
        print(f"\nCertificado emitido de participação como palestrante na área de {self.__especialidade} para {self._nome} ({self._email})")

def main():
    participantes = []
    
    while True:
        print("\n==== PLATAFORMA DE CURSOS ONLINE ====")
        print("\n[ MENU ]")
        print("\n1 - Cadastrar participante")
        print("2 - Listar participantes")
        print("3 - Emitir certificados")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção (0-3): ")

        if opcao == "1":
            tipo = input("\nTipo de participante (1 - Aluno, 2 - Instrutor): ")

            if tipo == "1":
                nome = input("\nNome: ")
                email = input("Email: ")
                curso = input("Curso: ")
                participante = Aluno(nome, email, curso)
                participantes.append(participante)

            elif tipo == "2":
                nome = input("\nNome: ")
                email = input("Email: ")
                especialidade = input("Especialidade: ")
                participante = Instrutor(nome, email, especialidade)
                participantes.append(participante)

            else:
                print("\nTipo inválido. Tente novamente.")
                continue
            print("\nParticipante cadastrado com sucesso!")

        elif opcao == "2":
            if participantes:
                print("\n==== LISTA DE PARTICIPANTES ====")
                for p in participantes:
                    if isinstance(p, Aluno):
                        print("\nTipo: Aluno")
                        print(f"Nome: {p._nome} - Email: ({p._email})")
                        print(f"Curso: {p.get_curso()}")
                    else:
                        print("\nTipo: Instrutor")
                        print(f"Nome: {p._nome} - Email: ({p._email})")
                        print(f"Curso: {p.get_especialidade()}")
            else:
                print("\nNenhum participante cadastrado.")
                continue
            
        elif opcao == "3":
            if participantes:
                print("\n==== CERTIFICADOS ====")
                for p in participantes:
                    p.emitirCertificado()
            else:
                print("\nNenhum participante cadastrado.")
                continue
            
        elif opcao == "0":
            print("\nSaindo do sistema...\n")
            break

        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()