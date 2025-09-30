from airflow.sdk import dag, task

@dag
def branch():
    @task
    def a():
        return 1 
    
    @task.branch
    def b(val: int) -> str:
        if val == 1:
            return ["equal_1", "run_if_1"]
        elif val < 1:
            return "less_1"
        else:
            return "more_1"
    
    @task
    def equal_1(val: int):
        print(f"is equal to {val}")

    @task
    def less_1(val: int):
        print("is less than {val}")
    
    @task
    def more_1(val: int):
        print("is more than {val}")

    @task
    def run_if_1():
        print("This runs only if value is 1")
    
    val = a()
    b(val) >> [equal_1(val), run_if_1(), less_1(val), more_1(val)]


branch()