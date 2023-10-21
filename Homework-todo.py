class Todo:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add(self, task, description):
        task_info = {"task": task, "description": description}
        self.tasks.append(task_info)

    def remove(self, task):
        for task_info in self.tasks:
            if task_info["task"] == task:
                self.tasks.remove(task_info)

    def list_hw(self):
        for task_info in self.tasks:
            print(f"{task_info['task']} : {task_info['description']}")
            
class Todo_pro(Todo):
    def __init__(self, name):
        super().__init__(name)
        
    def count_hw(self):
        print(len(self.tasks))
        
homework = Todo_pro("homework")
homework.add("พะสะไท", "ทำอะไรก็ไม่รู้")
homework.add("พะสะปะกิด", "ทำอะไรก็ไม่รู้2")
homework.list_hw()
homework.count_hw()