import random

class Course:
    def __init__(self, teacher, name, hours):
        self.teacher = teacher
        self.name = name
        self.hours = hours

class Schedule:
    def __init__(self, courses, teachers, rooms, slots):
        self.courses = courses
        self.teachers = teachers
        self.rooms = rooms
        self.slots = slots
        self.assignment = {slot: None for slot in slots}

    def evaluate(self):
        score = 0
        teacher_hours = {teacher: 0 for teacher in self.teachers}
        
        for slot, course in self.assignment.items():
            if course:
                teacher_hours[course.teacher] += 1
        
        for course in self.courses:
            if teacher_hours[course.teacher] >= course.hours:
                score += 1
        
        return score

    def random_assignment(self):
        for course in self.courses:
            assigned_hours = 0
            while assigned_hours < course.hours:
                slot = random.choice(self.slots)
                if self.assignment[slot] is None:
                    self.assignment[slot] = course
                    assigned_hours += 1

    def neighbor(self):
        new_schedule = Schedule(self.courses, self.teachers, self.rooms, self.slots)
        new_schedule.assignment = self.assignment.copy()
        
        slot1, slot2 = random.sample(self.slots, 2)
        new_schedule.assignment[slot1], new_schedule.assignment[slot2] = new_schedule.assignment[slot2], new_schedule.assignment[slot1]
        
        return new_schedule

    def hill_climbing(self, iterations=1000):
        current_schedule = self
        current_schedule.random_assignment()
        
        for _ in range(iterations):
            neighbor = current_schedule.neighbor()
            if neighbor.evaluate() > current_schedule.evaluate():
                current_schedule = neighbor
        
        return current_schedule

if __name__ == "__main__":
    courses = [
        {'teacher': '  ', 'name': '　　', 'hours': -1}, #那一節沒上課
        {'teacher': '甲', 'name':'機率', 'hours': 2},
        {'teacher': '甲', 'name':'線代', 'hours': 3},
        {'teacher': '甲', 'name':'離散', 'hours': 3},
        {'teacher': '乙', 'name':'視窗', 'hours': 3},
        {'teacher': '乙', 'name':'科學', 'hours': 3},
        {'teacher': '乙', 'name':'系統', 'hours': 3},
        {'teacher': '乙', 'name':'計概', 'hours': 3},
        {'teacher': '丙', 'name':'軟工', 'hours': 3},
        {'teacher': '丙', 'name':'行動', 'hours': 3},
        {'teacher': '丙', 'name':'網路', 'hours': 3},
        {'teacher': '丁', 'name':'媒體', 'hours': 3},
        {'teacher': '丁', 'name':'工數', 'hours': 3},
        {'teacher': '丁', 'name':'動畫', 'hours': 3},
        {'teacher': '丁', 'name':'電子', 'hours': 4},
        {'teacher': '丁', 'name':'嵌入', 'hours': 3},
        {'teacher': '戊', 'name':'網站', 'hours': 3},
        {'teacher': '戊', 'name':'網頁', 'hours': 3},
        {'teacher': '戊', 'name':'演算', 'hours': 3},
        {'teacher': '戊', 'name':'結構', 'hours': 3},
        {'teacher': '戊', 'name':'智慧', 'hours': 3}
    ]

    teachers = ['甲', '乙', '丙', '丁', '戊']
    rooms = ['A', 'B']
    slots = [
        'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
        'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
        'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'A37',
        'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A47',
        'A51', 'A52', 'A53', 'A54', 'A55', 'A56', 'A57',
        'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17',
        'B21', 'B22', 'B23', 'B24', 'B25', 'B26', 'B27',
        'B31', 'B32', 'B33', 'B34', 'B35', 'B36', 'B37',
        'B41', 'B42', 'B43', 'B44', 'B45', 'B46', 'B47',
        'B51', 'B52', 'B53', 'B54', 'B55', 'B56', 'B57',
    ]

    course_objects = [Course(c['teacher'], c['name'], c['hours']) for c in courses if c['hours'] != -1]

    schedule = Schedule(course_objects, teachers, rooms, slots)
    best_schedule = schedule.hill_climbing()

    for slot, course in best_schedule.assignment.items():
        if course:
            print(f"{slot}: {course.teacher} {course.name}")
        else:
            print(f"{slot}: No Class")
