import pytest # type: ignore
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """
    一个可供所有测试函数调用的AnonymousSurvey
    使用夹具fixtrue使得下面的测试方法都能使用到这个创建实体的方法
    """
    question = "What language did you first learn to speak?"
    return AnonymousSurvey(question)

def test_store_single_response(language_survey):
    """
    测试单个答案是否能被存储
    函数接收与上面创建实体类函数方法名一致的形参，统一调用
    """
    language_survey.store_response('English')
    assert 'English' in language_survey.show_results()

def test_store_single_responses(language_survey):
    """
    测试单个答案是否能被存储
    函数接收与上面创建实体类函数方法名一致的形参，统一调用
    """
    responses = ['English', 'Chinese', 'Spanish']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.show_results()