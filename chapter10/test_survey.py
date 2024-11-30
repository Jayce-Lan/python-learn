from survey import AnonymousSurvey

def test_store_single_response():
    """测试能否正确存储答案"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response("English")
    language_survey.store_response("Chinese")
    assert 'English' in language_survey.show_results()
