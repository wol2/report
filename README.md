위의 코드는 레벤슈타인 거리를 기반으로 한 챗봇을 구현한 예시입니다. 챗봇 클래스인 SimpleChatBot을 정의하고, 초기화 메서드인 __init__에서 데이터 파일을 로드하고, 입력 문장과 가장 유사한 질문을 찾는 find_best_answer 메서드를 구현합니다.

데이터 파일의 경로는 'ChatbotData.csv'로 지정되어 있으며, 이 부분을 필요에 따라 수정하여 사용하십시오. 챗봇 객체를 생성한 후, 사용자의 입력에 따라 챗봇의 응답을 출력하는 무한 루프를 실행합니다. 사용자가 '종료'라는 입력을 하면 루프가 종료됩니다.
