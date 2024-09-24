from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',  # 所属用户
    'start_date': datetime(2024, 9, 23),  # 第一次执行的时间
    'retries': 1,  # 失败重试次数
    'retry_delay': timedelta(minutes=1),  # 失败重试间隔
    'catchup': False,  # 执行 DAG 时，将开始时间到目前所有该执行的任务都执行，默认为 True
}

dag = DAG(
    dag_id="execute_shell_cmd",
    default_args=default_args,
    schedule_interval=timedelta(minutes=2),
)

bash_task_1 = BashOperator(
    task_id="bash_task_1",
    bash_command='echo "Hello bash_task_1!"',
    dag=dag,
)

bash_task_2 = BashOperator(
    task_id="bash_task_2",
    bash_command="""
    {% for x in range(10) %}
        echo "{{ ds }}"
        echo "{{ params.name }}"
        echo "{{ params.age }}"
    {% endfor %}
    """,
    params={'name': 'Zhang San', 'age': 18},
    dag=dag,
)

bash_task_1 >> bash_task_2
