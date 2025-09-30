from airflow.sdk import dag, task
from time import sleep

@dag
def celery_dag():
    @task
    def a():
        sleep(5)
        print("A")
    
    @task(
        queue="high_cpu",
    )
    def b():
        sleep(5)
        print("B")
    
    @task(
        queue="high_cpu",
    )
    def c():
        sleep(5)
        print("C")
    
    @task(
        queue="high_cpu",
    )
    def d():
        sleep(5)
        print("D")
    
    a() >> [b(), c()] >> d()

celery_dag()