import csv
from fileinput import filename
import os

DATA_FILE_PATH = os.getenv(
    'DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['Id', 'Story Title', 'User Story',
               'Acceptance Criteria', 'Business Value', 'Estimation', 'Status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']
DATA_KEYS = ['id', 'title', 'user_story', 'acceptance_criteria',
                   'business_value', 'estimation', 'status']


def get_all_user_story():
    with open(DATA_FILE_PATH, 'r+') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        user_story_list = []
        for line in csv_reader:
            user_story_list.append(line)

        return user_story_list


def max_id():
    user_story_list = get_all_user_story()
    high_id = 0
    for dict in user_story_list:
        for key, value in dict.items():
            if key == "id":
                if high_id < int(value):
                    high_id = int(value)

    return high_id


def add_user_story(data):
    with open(DATA_FILE_PATH, 'a', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=DATA_KEYS)
        csv_writer.writerow(data)


def get_user_story(id):
    user_story_list = get_all_user_story()
    for line in user_story_list:
        if line['id'] == id:
            return line
    return None


def update_user_story(user_story, id):
    user_story_list = get_all_user_story()
    with open(DATA_FILE_PATH, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=DATA_KEYS)
        csv_writer.writeheader()
        for line in user_story_list:
            if line['id'] == id:
                line['title'] = user_story['title']
                line['user_story'] = user_story['user_story']
                line['acceptance_criteria'] = user_story['acceptance_criteria']
                line['business_value'] = user_story['business_value']
                line['estimation'] = user_story['estimation']
                line['status'] = user_story['status']
            csv_writer.writerow(line)
