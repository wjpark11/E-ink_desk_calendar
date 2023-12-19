# E-ink 디스플레이를 아용한 만년 탁상달력 제작

좀처럼 마음에 드는 탁상달력 다자인을 찾기 쉽지 않고, 매년 구입하려면 가격도 만만치 않으니 내 니즈에 꼭 맞는 탁상달력을 만들어 보고자 합니다.

## 요구사항

- 컴퓨터 화면에 달력을 띄울 수도 있겠으나 다른 창으로 인해 대부분 가려져 있을 것이므로 별도 디스플레이로 제작
- 컴퓨터 시스템과 독립적으로 작동하게 하고 싶고 무선으로 데이터 업데이트를 하고 싶으므로 무선 연결을 지원하는 싱글보드 컴퓨터를 사용
- 잦은 스크린 업데이트가 필요 없고, 저전력에 시인성 좋은 디스플레이를 원함
- 각 주차의 시작일은 월요일일 것
- 각 주차의 iso weeknum이 표시될 것
- 전월과 다음월의 미니 달력이 표시될 것
- 원격 명령으로 원하는 년월의 달력을 원하는 때에 표시할 수 있을 것
- 일정은 구글 캘린더와 연동되어 표시될 것
- 일정 외 커스텀 메모 기능이 있으면 좋음
- 당일의 시간대벌 날씨가 표시되면 좋음
- 작은 크기의 랜덤 이미지가 표시되면 좋음

## 하드웨어

- 7.5인치 E-ink 디스플레이 사용 [HAT SPI 인터페이스를 포함한 전자 종이](https://ko.aliexpress.com/item/1005005891079210.html?spm=a2g0o.order_list.order_list_main.5.18a8140fihvQre&gatewayAdapt=glo2kor)
- 흑백 디스플레이 사양임 (붉은 색 표현 가능한 전자종이도 있으나 이미 구매해 버린 관계로 흑백 디스플레이로 진행)
- [라즈베리 파이 제로 2W](https://ko.aliexpress.com/item/1005005792181612.html?spm=a2g0o.order_list.order_list_main.4.18a8140fihvQre&gatewayAdapt=glo2kor)
- 다이소 액자
- 라즈베리 파이의 헤더핀 납땜을 위한 헤더핀, 인두기 일습 필요

## 참고 프로젝트

[MagInkDash](https://github.com/speedyg0nz/MagInkDash)