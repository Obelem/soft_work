#!/usr/bin/python3
import os
import json

from models.assessments import Assessment
from models.question_bank import QuestionBank
from models import storage

def get_files(dir: str, ext: str) -> list:
    '''
    Return names of files with ext in current dir

    args:
        dir: path to directory
        ext: extention to match
    '''
    if not isinstance(dir, str):
        raise TypeError("dir must be a string")
    
    if not isinstance(ext, str):
        raise TypeError("ext must be a sting")


    return [file for file in os.listdir(dir) if file.endswith(f".{ext}")]


def split_questions_answers(filename: str) -> list:
    '''
    opens a file, and split to questions and answers
    args:
        filename: name of the file
    
    Returns a list
    '''

    if not filename.endswith(".txt"):
        raise TypeError("file must be a txt file")

    with open(filename) as f:
        file_content = f.read()

    return file_content.split("[ANSWERS]\n")


def preprocess_questions(raw: str) -> list:
    '''
    Preprocess raw data to  get questions and options

    args:
        raw: The raw data
    '''

    return raw.split("\n---")


def separate_questions(questions: list) -> list:
    '''
    Splits each question and respective options into a list

    args:
        questions: prepared questions from prepare_questions()
    '''
    clean_question = []
    for raw in questions:
        if raw.startswith("\n"):
            raw = raw[1:].strip().split("\n")
        else:
            raw = raw.strip().split("\n")
        q = [raw[0], raw[1:]]
        clean_question.append(q)

    return clean_question


def separate_answers(answers: str) -> list:
    '''
    Splits each answers to a list
    args:
        answers: a string of answers
    '''

    return answers.split("\n")


def articulate_question_answer(questions: list, answers: list) -> list:
    '''
    Combines questions and answer:
    args:
        questions: list of questions containing options
        answers: list of correct answers
    '''

    if not isinstance(questions, list):
        raise TypeError("questions must be a list")
    
    if not isinstance(answers, list):
        raise TypeError("answers must be a list")

    if len(questions) != len(answers):
        print(f"Number of questions = {len(questions)}")
        print(f"Number of answers = {len(answers)}")
        print(answers)
        raise TypeError("Number of questions must match number of answers")

    questions_answers = []
    for question, answer in zip(questions, answers):
        options = question[1]
        if answer not in options:
            print(f"could not find {answer} in {options}")
            continue

        q = {}
        q['question'] = question[0]
        q['options'] = options
        q["answer"] = answer
        questions_answers.append(q)

    return questions_answers


def get_cleaned_data(dir, ext) -> dict:
    filenames = get_files(dir, ext)

    clean_data = {}

    for name in filenames:

        # get raw questions and answers from file
        split_qa_from_file = split_questions_answers(f"{dir}/{name}")

        raw_questions = split_qa_from_file[0]
        raw_answers = split_qa_from_file[1]

        # preprocess questions
        preprocess_questions_ = preprocess_questions(raw_questions)

        # get list of each question and options
        questions_options = separate_questions(preprocess_questions_)

        # get list of answers
        answers = separate_answers(raw_answers)

        # articulate each question with its options and correct answer
        data = articulate_question_answer(questions_options, answers)

        # store data
        clean_data[name.split(".")[0]] = data

    with open("data.json", "w") as f:
        json.dump(clean_data, f, indent=4)


def upload_to_storage():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
        os.remove("data.json")
    except FileNotFoundError as e:
        raise e

    assessments = list(data.keys())
    # create assessment objects
    assessment_objects = {}
    for assessment in assessments:
        assessment_objects[assessment] = Assessment(name=assessment)
        # save the assessment object
        assessment_objects[assessment].save()
        print(assessment_objects[assessment].to_dict())

    #  Add questions
    for assessment in assessments:
        for item in data[assessment]:
            question = QuestionBank(
                assessment_id=assessment_objects[assessment].id,
                assessment_name=assessment_objects[assessment].name,
                question=item["question"],
                options=item["options"],
                answer=item["answer"],
            )
            # save question
            question.save()
    
    return True
    
    
if __name__ == "__main__":
    get_cleaned_data("questions/", "txt")
    if upload_to_storage():
        print("Upload successful")
    else:
        print("Upload failed")

