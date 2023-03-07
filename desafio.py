import requests


class User:
    def __init__(self, name, profile_url, public_repos, followers, following):
        self.name = name
        self.profile_url = profile_url
        self.public_repos = public_repos
        self.followers = followers
        self.following = following


# faz uma requisição à API do GitHub e cria um objeto User com as informações recebidas
def obter_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(
        url, timeout=5
    )  # O timeout=5 faz com que a app não fique esperando indefinidamente, responda rapido e o tempo também é o suficiente para o server.
    if response.status_code == 200:
        data = response.json()
        name = data.get("name")
        profile_url = data.get("html_url")
        public_repos = data.get("public_repos")
        followers = data.get("followers")
        following = data.get("following")
        return User(name, profile_url, public_repos, followers, following)
    else:
        return None


# faz uma requisição à API do GitHub e retorna um dicionário com os nomes e URLs dos repositórios do usuário.
def obter_user_repos(username):
    response = requests.get(f"https://api.github.com/users/{username}/repos", timeout=5)
    if response.status_code == 200:
        repos_dict = {}
        for repo in response.json():
            repos_dict[repo["name"]] = repo["html_url"]
        return repos_dict
    else:
        print(
            "*********** Woops! Algo deu errado! Verifique o nick do usuário ********"
        )
        return None


# gera um relatório em um arquivo de texto com informações do usuário e seus repositórios.
def user_report(user_obj, repos_dict):
    filename = f'{user_obj.profile_url.split("/")[-1]}.txt'  # Cria uma variável 'filename' com o nome do arquivo, baseado na última parte da URL do perfil do usuário.
    with open(filename, "w") as f:  # Abre o arquivo filename para ser editado.
        f.write(
            f"Nome: {user_obj.name}\n"
        )  # Escreve o nome do usuário no arquivo e depois faz uma quebra de linha.
        f.write(f"Perfil: {user_obj.profile_url}\n")
        f.write(f"Numero de repositorios publicos: {user_obj.public_repos}\n")
        f.write(f"Numero de seguidores: {user_obj.followers}\n")
        f.write(f"Numero de usuarios seguidos: {user_obj.following}\n")
        f.write("Repositorios:\n")
        for repo, url in repos_dict.items():
            f.write(f"{repo}: {url}\n")


import unittest


class TestMethods(unittest.TestCase):
    # Verifica se a classe User possui os atributos mínimos necessários.
    def test_user_class_has_minimal_parameters(self):
        parameters = ["name", "profile_url", "public_repos", "followers", "following"]
        user = obter_user("github")
        for param in parameters:
            self.assertTrue(hasattr(user, param))

    # Verifica se a função obter_user retorna None quando é feita uma requisição inválida
    def test_obter_user_invalido(self):
        user = obter_user("usuario_invalido_que_nao_existe_no_github")
        self.assertIsNone(user)

    # Verifica se a função obter_user_repos retorna um dicionário e se ele tem mais de um item.
    def test_obter_user_repos(self):
        repos = obter_user_repos("github")
        self.assertIsInstance(repos, dict)
        self.assertGreater(len(repos), 0)
        for repo, url in repos.items():
            self.assertIsInstance(repo, str)
            self.assertIsInstance(url, str)

    # Verifica se o relatório gerado pela função user_report contém informações básicas do usuário e dos repositórios.
    def test_user_report(self):
        user = obter_user("github")
        repos = obter_user_repos("github")
        user_report(user, repos)
        filename = f'{user.profile_url.split("/")[-1]}.txt'
        with open(filename, "r") as f:
            content = f.read()
            self.assertIn(user.name, content)
            self.assertIn(user.profile_url, content)
            self.assertIn(str(user.public_repos), content)
            self.assertIn(str(user.followers), content)
            self.assertIn(str(user.following), content)
            for repo, url in repos.items():
                self.assertIn(repo, content)
                self.assertIn(url, content)


if __name__ == "__main__":
    nick = input("Digite o nickname do usuário que deseja gerar o relatório: ")
    user = obter_user(nick)
    repos = obter_user_repos(nick)
    user_report(user, repos)
