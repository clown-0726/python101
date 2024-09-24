from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator

default_args = {
    'owner': 'airflow',  # 所属用户
    'start_date': datetime(2024, 9, 23),  # 第一次执行的时间
    'retries': 1,  # 失败重试次数
    'retry_delay': timedelta(minutes=1),  # 失败重试间隔
    'catchup': False,  # 执行 DAG 时，将开始时间到目前所有该执行的任务都执行，默认为 True
}

dag = DAG(
    dag_id="execute_ssh",
    default_args=default_args,
    schedule_interval=timedelta(minutes=2),
)

task_1 = SSHOperator(
    task_id="task_1",
    ssh_conn_id="ssh_name",
    command='echo "Hello task_1!"',
    dag=dag,
)

task_2 = SSHOperator(
    task_id="task_2",
    ssh_conn_id="ssh_name",
    command='echo "Hello task_2!"',
    dag=dag,
)

task_1 >> task_2
