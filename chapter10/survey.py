class AnonymousSurvey:
    """
    收集匿名调查问卷的答案
    """
    def __init__(self, question):
        """
        存储一个问题，并为存储答案做准备
        """
        self.question = question
        self.responses = []
        
    def show_question(self):
        """返回调查问卷"""
        return self.question
    
    def store_response(self, new_response):
        """
        @param new_response 新的答案/单份调查问卷的答案
        存储单份调查问卷的答案
        """
        self.responses.append(new_response)
        
    def show_results(self):
        """
        返回收集到的所有答案
        """
        return self.responses
        