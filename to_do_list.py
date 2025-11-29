#لیست پیش فرض کار ها 
tasks = [
    {"task": "go to gym", "priority": "normal"},
    {"task": "eat diner",   "priority": "normal"},
    {"task": "do homworke", "priority": "high"}
]

#تابع add_task 
def add_task () :
    '''add new task'''
    print("add new task:")
    task = input ("please enter your task:\n>")
    priority = input ("determine the importance of your task :\n>")
   #چک کردن ورودی ها
    while task.strip() == "" :
        task = input ("Task cannot be empty \nplease enter your task2:\n>")

    #سیو کردن تسک در لیست 
    tasks.append({
        "task" : task,
        "priority" : priority
    })
    print (f'Task "{task}" added successfully :)\n\n')

#تابع get_task
def get_tasks () :
    '''show all tasks'''
    sorted_tasks = sorted(tasks, key=lambda item: item["task"])
    for i, t in enumerate(sorted_tasks, start=1):
        print(f"{i}. {t['task']} - {t['priority']}")
    print()

#تابع countdown_timer
def countdown_timer(minutes):
    """Time Counter"""
    if minutes <= 0:
        print("Time is up! ")
        return
    print(f"{minutes} minutes remaining...")
    countdown_timer(minutes - 1)



    
#نمایش
print ("__To Do List__\n")
while True:
    person_choice = int(input('please enter youer choice:\n1-Add task\n2-get task\n3-countdown timer\ntype "esc" to exit\n>'))
    if person_choice == 1 :
        add_task()
        get_tasks()
    if person_choice == 2 :
        get_tasks()
    if person_choice == 3 :
        time = int(input("\nEnter Your desired time:\n>"))
        countdown_timer(time)
    if person_choice == "esc" :
        break