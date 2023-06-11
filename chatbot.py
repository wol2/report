import pandas as pd
from Levenshtein import distance

# 챗봇 클래스를 정의합니다.
class SimpleChatBot:
    # 챗봇 객체를 초기화하는 메서드입니다.
    def __init__(self, filepath):
        self.questions, self.answers = self.load_data(filepath)

    # CSV 파일로부터 질문과 답변 데이터를 불러오는 메서드입니다.
    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        questions = data['Q'].tolist()  # 질문 열을 리스트로 저장
        answers = data['A'].tolist()  # 답변 열을 리스트로 저장
        return questions, answers

    # 입력 문장과 가장 유사한 질문을 찾아 해당하는 답변을 반환하는 메서드입니다.
    def find_best_answer(self, input_sentence):
        min_distance = float('inf')  # 초기 거리를 무한대로 설정
        best_match_index = -1  # 초기 가장 유사한 질문의 인덱스를 -1로 설정
        for i, question in enumerate(self.questions):
            lev_distance = distance(question, input_sentence)  # 레벤슈타인 거리 계산
            if lev_distance < min_distance:
                min_distance = lev_distance
                best_match_index = i
        return self.answers[best_match_index]

# 데이터 파일의 경로를 지정합니다.
filepath = 'ChatbotData.csv'

# 챗봇 객체를 생성합니다.
chatbot = SimpleChatBot(filepath)

# '종료'라는 입력이 나올 때까지 사용자의 입력에 따라 챗봇의 응답을 출력하는 무한 루프를 실행합니다.
while True:
    input_sentence = input('You: ')
    if input_sentence.lower() == '종료':
        break
    response = chatbot.find_best_answer(input_sentence)
    print('Chatbot:', response)
