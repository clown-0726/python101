from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',  # 所属用户
    'start_date': datetime(2024, 9, 8),  # 第一次执行的时间
    'retries': 1,  # 失败重试次数
    'retry_delay': timedelta(minutes=3),  # 失败重试间隔
    'catchup': True,  # 执行 DAG 时，将开始时间到目前所有该执行的任务都执行，默认为 True
}

dag = DAG(
    # 指定 DAG 的 ID，这个会显示到 UI 上
    dag_id="my_workflow_execute_shell",
    # 默认参数
    default_args=default_args,
    # DAG 的调度周期
    schedule_interval=timedelta(days=1),
)

# 定义 task
bash_task_1 = BashOperator(
    task_id="bash_task_1",
    bash_command='echo "Hello bash_task_1!"',
    dag=dag,
)

bash_task_2 = BashOperator(
    task_id="bash_task_2",
    bash_command='echo "Hello bash_task_2!"',
    dag=dag,
)

bash_task_3 = BashOperator(
    task_id="bash_task_3",
    bash_command='echo "Hello bash_task_3!"',
    dag=dag,
)

# 建立任务之间的执行关系
bash_task_1 >> bash_task_2 >> bash_task_3

# 也可以通过下面 API 的方式设置（推荐使用上面的方式）
# bash_task_2.set_upstream(bash_task_1)
# bash_task_2.set_downstream(bash_task_3)
