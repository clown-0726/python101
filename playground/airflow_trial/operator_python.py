from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airflow',  # 所属用户
    'start_date': datetime(2024, 9, 24),  # 第一次执行的时间
    'retries': 1,  # 失败重试次数
    'retry_delay': timedelta(minutes=1),  # 失败重试间隔
    'catchup': False,  # 执行 DAG 时，将开始时间到目前所有该执行的任务都执行，默认为 True
}

dag = DAG(
    dag_id="execute_python",
    default_args=default_args,
    schedule_interval=timedelta(minutes=2),
)


def print_hello(*args, **kwargs):
    print(args)
    print(kwargs)


task_1 = PythonOperator(
    task_id="task_1",
    python_callable=print_hello,
    op_args=[1, 2, 'c'],
    op_kwargs={"hello": "world"},
    dag=dag,
)

task_2 = PythonOperator(
    task_id="task_2",
    python_callable=print_hello,
    op_args=[1, 2, 'c'],
    op_kwargs={"hello": "world"},
    dag=dag,
)

task_1 >> task_2
