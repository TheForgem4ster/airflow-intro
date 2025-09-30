from airflow.sdk import dag, task, Context
from typing import Dict, Any


@dag
def xcom_dag():

    # 1 way to pass data between taskss - XCom
    # XCom - a small amount of data (up to 48KB) that is stored in the Airflow metadata database   
    # @task
    # def t1(context: Context):
    #     val = 21
    #     context["ti"].xcom_push(key="my_key", value=val)

    # @task
    # def t2(context: Context):
    #     val = context["ti"].xcom_pull(key="my_key", task_ids="t1")
    #     print(val)


    # 2 way to pass data between tasks - return value
    @task
    def t1() -> Dict[str, Any]:
        my_val = 21
        my_sentence = "The answer to life, the universe and everything"
        return {
            "my_val": my_val,
            "my_sentence": my_sentence,
        } # xcom_push(key="my_key", value=val)
    
    @task
    def t2(data: Dict[str, Any]):
        print(data["my_val"])
        print(data["my_sentence"])


    val = t1() 
    t2(val)


xcom_dag()