# PySerialGenerator
Serial number generator and verifier


###1. 시리얼 생성하기
- 생성을 원하는 수를 인자로 입력한다.
- ![](http://i.imgur.com/kgh7P3X.png)
- 매 5000개의 시리얼마다 새로 파일을 생성한다.
- serial과 output은 별개의 파일로 생성된다.

###2. 시리얼 검증하기
- 입력받은 시리얼의 해시값을 다시 생성한다.
- 보유한 output 파일을 탐색하여 기존의 해시값과 일치하는 값이 있는지를 판별한다.

######검증 성공
- 일치하는 값을 발견하면 검증 성공.
- ![](http://i.imgur.com/sOihUpg.png)

######검증 실패
- 보유한 전체 output에서 일치하는 값을 발견하지 못하면 검증 실패.
- ![](http://i.imgur.com/GN47cjn.png)
