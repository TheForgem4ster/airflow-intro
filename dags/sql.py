from airflow.sdk import dag, task

@dag
def sql_dag():

    @task.sql(
        conn_id="postgres_default",
    )
    def get_nb_xcom():
        return "SELECT COUNT(*) FROM xcom"
    
    get_nb_xcom()

sql_dag()