import yaml

dados = {
    "alunos": [
        "Antonio", "Beatriz", "Carlos", "Daniela", "Eduardo",
        "Fabiana", "Gustavo", "Helena", "Igor", "Julia",
        "Kleber", "Larissa", "Marcelo", "Natalia", "Otavio",
        "Patricia", "Rafael", "Silvia", "Thiago", "Vanessa",
        "William", "Yasmin", "Zelia", "Bernardo", "Camila",
        "Diego", "Eloisa", "Felipe", "Gabriela", "Hugo",
        "Isabela", "Joel", "Leticia", "Matheus", "Nicole",
        "Oscar", "Paula", "Rodrigo", "Sara", "Tiago",
        "Valeria", "Wagner", "Xavier", "Yago", "Zara",
        "Adriano", "Bruna", "Cesar", "Denise", "Emilio",
        "Fernanda", "Guilherme", "Heloisa", "Ivan", "Joice",
        "Kaique", "Lorena", "Marcela", "Nelson", "Oliveira",
        "Pedro", "Raquel", "Samuel", "Tatiana", "Ulisses",
        "Vitor", "Wanessa", "Xandao", "Yasmin", "Zeca",
        "Ana Clara", "Bernardo", "Clara", "Davi", "Estela",
        "Felipe", "Gabriela", "Henrique", "Isabela", "Julio",
        "Karina", "Lucas", "Mariana", "Nathan", "Olivia",
        "Paulo", "Rafaela", "Sandro", "Teresa", "Ulisses"
    ],
    "notas": [
        2, 5, 7, 4, 8, 3, 9, 6, 8, 7,
        5, 2, 9, 4, 6, 8, 3, 5, 7, 4,
        8, 3, 6, 9, 2, 5, 7, 4, 8, 3,
        6, 9, 2, 5, 7, 4, 8, 3, 6, 9,
        2, 5, 7, 4, 8, 3, 6, 9, 2, 5,
        7, 4, 8, 3, 6, 9, 2, 5, 7, 4,
        8, 3, 6, 9, 2, 5, 7, 4, 8, 3,
        6, 9, 2, 5, 7, 4, 8, 3, 6, 9,
        2, 5, 7, 4, 8, 3, 6, 9, 2, 5,
        7, 4, 8, 3, 6, 9, 2, 5, 7, 4
    ],
    "idade": [
        22, 20, 24, 21, 23, 19, 25, 23, 22, 20,
        24, 21, 23, 19, 25, 23, 22, 20, 24, 21,
        23, 19, 25, 23, 22, 20, 24, 21, 23, 19,
        25, 23, 22, 20, 24, 21, 23, 19, 25, 23,
        22, 20, 24, 21, 23, 19, 25, 23, 22, 20,
        24, 21, 23, 19, 25, 23, 22, 20, 24, 21,
        23, 19, 25, 23, 22, 20, 24, 21, 23, 19,
        25, 23, 22, 20, 24, 21, 23, 19, 25, 23,
        22, 20, 24, 21, 23, 19, 25, 23, 22, 20,
        24, 21, 23, 19, 25, 23, 22, 20, 24, 21
    ],
    "altura": [
        1.70, 1.65, 1.80, 1.68, 1.75, 1.72, 1.67, 1.78, 1.69, 1.73,
        1.74, 1.71, 1.79, 1.66, 1.76, 1.77, 1.70, 1.65, 1.80, 1.68,
        1.75, 1.72, 1.67, 1.78, 1.69, 1.73, 1.74, 1.71, 1.79, 1.66,
        1.76, 1.77, 1.70, 1.65, 1.80, 1.68, 1.75, 1.72, 1.67, 1.78,
        1.69, 1.73, 1.74, 1.71, 1.79, 1.66, 1.76, 1.77, 1.70, 1.65,
        1.80, 1.68, 1.75, 1.72, 1.67, 1.78, 1.69, 1.73, 1.74, 1.71,
        1.79, 1.66, 1.76, 1.77, 1.70, 1.65, 1.80, 1.68, 1.75, 1.72,
        1.67, 1.78, 1.69, 1.73, 1.74, 1.71, 1.79, 1.66, 1.76, 1.77,
        1.70, 1.65, 1.80, 1.68, 1.75, 1.72, 1.67, 1.78, 1.69, 1.73,
        1.74, 1.71, 1.79, 1.66, 1.76, 1.77
    ]
}


with open("PythonClass8/dados.yaml", "w") as file:
    yaml.dump(dados, file)

print("Arquivo YAML com dados criado com sucesso!")
