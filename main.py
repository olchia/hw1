# Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.


class Task:
    def __init__(self):
        self.task_deadline = [] # Инициировала создание списка, в котором каждый элемент будет представлять словарь (ввод данных от пользователя)

    def add_task(self):
        task = input("Введите задачу: ")
        deadline = input("Введите сроки выполнения задачи: ")
        # Введенные пользователем данные добавляются в виде словаря, очевидно, что они не выполнены, поэтому статус по умолчанию везде будет "Не выполнено"
        self.task_deadline.append({'task' : task,
                                   'deadline' : deadline,
                                  'status' : "Не выполнено"
                                   })
        print(f'Задача "{task}" добавлена в список задач. Срок выполнения - {deadline}')


    def completed_task(self):
        completed_task_name = input("Введите выполненную задачу: ")
        task_check = False # Переменная-флаг для отслеживания нахождения задачи
        for task in self.task_deadline: # Для каждого элемента (в виде словаря) из списка self.task_deadline будет проверка
            if task['task'] == completed_task_name: # Если значение по ключу task равно введенной пользователем задаче, то меняется статус
                task['status'] == "Выполнено"
                print(f'{task["task"]} - выполнено') # {task["task"]} - для элемента {task}, увовлетворившего условие выше, выводится значение по ключу ["task"]
                self.task_deadline.remove(task) # Найденная задача убирается
                task_check = True # Задача найдена
            if not task_check:
                print('Задача не найдена')

    def all_task(self):
        print("Список задач: ")
        if self.task_deadline == 0:
            print("В вашем списке нет задач")
        else:
            for task in self.task_deadline:
                print(f'{task["task"]}, дедлайн - {task["deadline"]}')


olga = Task()

olga.add_task()
olga.add_task()
olga.add_task()
olga.all_task()
olga.completed_task()
olga.all_task()
