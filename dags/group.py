from airflow.sdk import dag, task, task_group

@dag
def group():
    
    @task
    def a():
        return 21
    
    @task_group(default_args={
        "retries": 2
    })
    def my_group(val: int):
    
        @task
        def b(my_val: int):
            return my_val * 21

        @task_group(default_args={
            "retries": 3
        })
        def my_nested_group():

            @task
            def c():
                print("C")
            
            c()

        b(val) >> my_nested_group()
 
    my_group(a())

group()