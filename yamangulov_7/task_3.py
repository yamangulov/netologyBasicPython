class Employee:
    def __init__(self, name, seniority):
        self.name = name
        self.seniority = seniority

        self.grade = 1

    def grade_up(self):
        """Повышает уровень сотрудника"""
        self.grade += 1

    def publish_grade(self):
        """Публикация результатов аккредитации сотрудников"""
        print(self.name, self.grade)

    def check_if_it_is_time_for_upgrade(self):
        pass

class Designer(Employee):
    # по умолчанию при старте у дизайнера 2 международные премии по 2 балла за каждую, то есть 4 балла
    def __init__(self, name, seniority=4):
        super().__init__(name, seniority)
        self.seniority = seniority
        self.num_upgrades = 0

    def get_international_awards(self):
        self.seniority += 2

    def check_if_it_is_time_for_upgrade(self):
        # для каждой аккредитации увеличиваем счетчик на 1
        self.seniority += 1

        # условие повышения сотрудника из презентации
        # здесь нельзя использовать условие self.seniority % 7 == 0 по аналогии с классом Developer из лекции
        # так как получение международной премии приводит к тому, что между аккредитациями seniority может вырастать
        # более, чем на 1, и поэтому "проскочит" через точки, где seniority нацело делится на 7
        if self.seniority / 7 > self.num_upgrades:
            self.grade_up()
            self.num_upgrades += 1

        # публикация результатов
        return self.publish_grade()

petrov = Designer('Petrov')
for i in range(21):
    petrov.get_international_awards()
    petrov.check_if_it_is_time_for_upgrade()
