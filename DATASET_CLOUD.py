import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
import csv

fake = Faker()

cases = []
parties = []
documents = []
tasks = []
notes = []

num_cases = 100

for i in range(num_cases):
    case_id = "PI" + str(i + 1).zfill(3)
    case_title = fake.sentence(nb_words=6, variable_nb_words=True)
    case_type = random.choice(["Motor Vehicle Accident", "Slip and Fall", "Product Liability"])
    case_status = random.choice(["Open", "Closed", "In Progress"])
    case_assigned_to = fake.name()
    case_start_date = fake.date_between(start_date="-2y", end_date="today")
    case_close_date = fake.date_between(start_date=case_start_date, end_date="today")

    cases.append({
        "Case ID": case_id,
        "Case Title": case_title,
        "Case Type": case_type,
        "Case Status": case_status,
        "Case Assigned To": case_assigned_to,
        "Case Start Date": case_start_date,
        "Case Close Date": case_close_date
    })

for case in cases:
    num_documents = random.randint(0, 5)  # Define the number of documents per case
    for _ in range(num_documents):
        document_id = fake.unique.random_number(digits=5)
        document_name = fake.file_name(extension="pdf")
        document_type = random.choice(["Agreement", "Medical Report", "Evidence"])
        documents.append({
            "Case ID": case["Case ID"],
            "Document ID": document_id,
            "Document Name": document_name,
            "Document Type": document_type
        })

for case in cases:
    for _ in range(random.randint(1, 5)):
        document_id = fake.unique.random_number(digits=5)
        document_name = fake.sentence(nb_words=4, variable_nb_words=True)
        document_type = random.choice(["Medical Records", "Accident Report", "Witness Statement"])
        date_created = fake.date_between(start_date=case["Case Start Date"], end_date=case["Case Close Date"])
        created_by = fake.name()
        date_last_modified = fake.date_between(start_date=date_created, end_date="today")
        last_modified_by = fake.name()
        documents.append({
            "Case ID": case["Case ID"],
            "Document ID": document_id,
            "Document Name": document_name,
            "Document Type": document_type,
            "Date Created": date_created,
            "Created By": created_by,
            "Date Last Modified": date_last_modified,
            "Last Modified By": last_modified_by
        })

for case in cases:
    for _ in range(random.randint(1, 3)):
        task_id = fake.unique.random_number(digits=5)
        task_description = fake.sentence(nb_words=8, variable_nb_words=True)
        assigned_to = fake.name()
        task_due_date = fake.date_between(start_date=case["Case Start Date"], end_date=case["Case Close Date"])
        task_status = random.choice(["Pending", "Completed"])
        tasks.append({
            "Case ID": case["Case ID"],
            "Task ID": task_id,
            "Task Description": task_description,
            "Assigned To": assigned_to,
            "Task Due Date": task_due_date,
            "Task Status": task_status
        })

for case in cases:
    for _ in range(random.randint(1, 5)):
        note_id = fake.unique.random_number(digits=5)
        note_content = fake.paragraph(nb_sentences=3, variable_nb_sentences=True)
        created_by = fake.name()
        date_created = fake.date_between(start_date=case["Case Start Date"], end_date=case["Case Close Date"])
        notes.append({
            "Case ID": case["Case ID"],
            "Note ID": note_id,
            "Note Content": note_content,
            "Created By": created_by,
            "Date Created": date_created
        })

dataset = []
for case in cases:
    case_data = case.copy()
    case_parties = [party for party in parties if party["Case ID"] == case["Case ID"]]
    case_data["Parties Involved"] = case_parties
    case_documents = [document for document in documents if document["Case ID"] == case["Case ID"]]
    case_data["Case Documents"] = case_documents
    case_tasks = [task for task in tasks if task["Case ID"] == case["Case ID"]]
    case_data["Case Tasks"] = case_tasks
    case_notes = [note for note in notes if note["Case ID"] == case["Case ID"]]
    case_data["Case Notes"] = case_notes
    dataset.append(case_data)

fields = ["Case ID", "Case Title", "Case Type", "Case Status", "Case Assigned To", "Case Start Date",
          "Case Close Date", "Parties Involved", "Case Documents", "Case Tasks", "Case Notes"]

filename = "personal_injury_cases.csv"

with open(filename, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(dataset)


