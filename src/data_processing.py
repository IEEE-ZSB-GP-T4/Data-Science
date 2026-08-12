import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import json

# switch to this code when the real data is ready

import pandas as pd

def get_processed_data():
     
    df_users = pd.read_csv('users.csv')
    df_courses = pd.read_csv('courses.csv')
    df_study_plans = pd.read_csv('study_plans.csv')
    df_tasks = pd.read_csv('tasks.csv')

    # to drop any duplicated task and keep the last updated one
    df_tasks = df_tasks.drop_duplicates(subset=['course_id', 'title', 'description'], keep='last')
    
   
    df_tasks['created_at'] = pd.to_datetime(df_tasks['created_at'])
    df_tasks['deadline'] = pd.to_datetime(df_tasks['deadline'])
    df_study_plans['created_at'] = pd.to_datetime(df_study_plans['created_at'])
    
   
    return {
        "users": df_users,
        "courses": df_courses,
        "study_plans": df_study_plans, 
        "tasks": df_tasks
    }



#virtual data till i get csv files for real data
'''
def get_processed_data():
    # 1- Users Table 

 num_users = 10
 users_data = {
    'id': range(1, num_users + 1),
    'name': [f'User_{i}' for i in range(1, num_users + 1)],
    'email': [f'user{i}@example.com' for i in range(1, num_users + 1)],
    'password': ['hashed_pass_123'] * num_users,
    'verify_password': ['hashed_pass_123'] * num_users,
    'created_at': [datetime.now() - timedelta(days=random.randint(30, 365)) for _ in range(num_users)],
}
 df_users = pd.DataFrame(users_data)
 df_users['updated_at'] = df_users['created_at'] + timedelta(days=random.randint(1, 10))



 # 2- Courses Table 

 num_courses = 25
 courses_data = {
     'id': range(1, num_courses + 1),
     'user_id': [random.choice(df_users['id']) for _ in range(num_courses)],
     'name': [f'Course_{i}' for i in range(1, num_courses + 1)],
     'code': [f'CS{random.randint(100, 999)}' for _ in range(num_courses)],
     'created_at': [datetime.now() - timedelta(days=random.randint(10, 100)) for _ in range(num_courses)],
       }
 df_courses = pd.DataFrame(courses_data)
 df_courses['updated_at'] = df_courses['created_at'] + timedelta(days=random.randint(1, 5))



 # 3- Study_plans Table 

 num_plans = 15
 plans_data = {
     'id': range(1, num_plans + 1),
     'user_id': [random.choice(df_users['id']) for _ in range(num_plans)],
     'available_hours': [round(random.uniform(5.0, 40.0), 1) for _ in range(num_plans)],
     'generated_plan': [json.dumps({"week_1": "intro", "week_2": "basics"}) for _ in range(num_plans)],
     'created_at': [datetime.now() - timedelta(days=random.randint(5, 50)) for _ in range(num_plans)],
 }
 df_study_plans = pd.DataFrame(plans_data)
 df_study_plans['updated_at'] = df_study_plans['created_at']



 # 4- Tasks Table 

 num_tasks = 100
 statuses = ['pending', 'progress', 'completed']
 priorities = ['low', 'mid', 'high']

 tasks_data = {
     'id': range(1, num_tasks + 1),
     'course_id': [random.choice(df_courses['id']) for _ in range(num_tasks)],
     'title': [f'Task_{i}' for i in range(1, num_tasks + 1)],
     'description': [f'Description for task {i}' for i in range(1, num_tasks + 1)],
     'estimated_hours': [round(random.uniform(1.0, 10.0), 2) for _ in range(num_tasks)],
     'priority': [random.choice(priorities) for _ in range(num_tasks)],
     'status': [random.choice(statuses) for _ in range(num_tasks)],
     'created_at': [datetime.now() - timedelta(days=random.randint(1, 30)) for _ in range(num_tasks)],
 }

 df_tasks = pd.DataFrame(tasks_data)
 df_tasks['deadline'] = df_tasks['created_at'] + timedelta(days=random.randint(3, 14))
 df_tasks['updated_at'] = df_tasks['created_at'] + timedelta(days=random.randint(0, 2))

 # إضافة completed_at بناءً على الـ status
 df_tasks['completed_at'] = df_tasks.apply(
     lambda row: row['updated_at'] if row['status'] == 'completed' else pd.NaT, 
     axis=1
 )
 return {
        "users": df_users,
        "courses": df_courses,
        "study_plans": df_study_plans, 
        "tasks": df_tasks
    }'''