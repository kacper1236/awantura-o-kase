from ..database import Category
import random

def get_categories(db):
    try:
        categories = db.session.query(Category).all()
        return categories
    except Exception as e:
        raise ValueError({'error': str(e)})

def get_categories_for_one_vs_one(db):
    try:
        categories = db.session.query(Category).all()
        if not categories:
            raise ValueError({'error': 'No categories available'})
        
        selected_category = categories.copy()
        random.shuffle(selected_category)
        selected_category = selected_category[:6]

        return [category.category for category in selected_category]
    except Exception as e:
        raise ValueError({'error': str(e)})
    
def get_question(db, category):
    try:
        category_obj = db.session.query(Category).filter_by(category=category).all()
        if not category_obj:
            raise ValueError({'error': 'Category not found'})
        
        questions = category_obj.question
        if not questions:
            raise ValueError({'error': 'No questions available in this category'})
        question = random.choice(questions)
        return question
    except Exception as e:
        raise ValueError({'error': str(e)})
    
def get_hint(db, category, question):
    try:
        category_obj = db.session.query(Category).filter_by(category=category).first()
        if not category_obj:
            raise ValueError({'error': 'Category not found'})
        if question not in category_obj.question:
            raise ValueError({'error': 'Question not found in this category'})
        hint = question.hint
        if not hint:
            raise ValueError({'error': 'No hint available for this question'})
        return hint
    except Exception as e:
        raise ValueError({'error': str(e)})

def get_answer(db, category, question):
    try:
        category_obj = db.session.query(Category).filter_by(category=category).first()
        if not category_obj:
            raise ValueError({'error': 'Category not found'})
        if question not in category_obj.question:
            raise ValueError({'error': 'Question not found in this category'})
        answer = question.answer
        if not answer:
            raise ValueError({'error': 'No answer available for this question'})
        return answer
    except Exception as e:
        raise ValueError({'error': str(e)})

def delete_question_from_category(db, category, question):
    try:
        category_obj = db.session.query(Category).filter_by(category=category).first()
        if not category_obj:
            raise ValueError({'error': 'Category not found'})
        if question in category_obj.questions:
            category_obj.questions.remove(question)
            db.session.commit()
            return {'message': 'Question deleted successfully'}
        else:
            raise ValueError({'error': 'Question not found in category'})
    except Exception as e:
        db.session.rollback()
        raise ValueError({'error': str(e)})