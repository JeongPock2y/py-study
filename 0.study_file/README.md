![pandas](https://user-images.githubusercontent.com/44747739/208286896-4c26edaf-0b94-453e-b91e-77c97a93df1f.png)

![pp](https://user-images.githubusercontent.com/44747739/208286929-5b8c451f-1723-4103-9793-22714a1cb560.jpg)

파이썬은 컴퓨터 프로그래밍 교육을 위해 많이 사용하지만, 기업의 실무를 위해서도 많이 사용하는 언어이다. 그 대표적인 예가 바로 구글이다. 필자는 구글에서 만든 소프트웨어의 50%이상이 파이썬으로 작성되었다는 이야기를 들었다. 이외에도 많이 알려진 예를 몇 가지 들자면 온라인 사진 공유 서비스 인스타그램(Instagram), 파일 동기화 서비스 드롭박스(Dropbox)등이 있다.

또한 파이썬 프로그램은 공동 작업과 유지 보수가 매우 쉽고 편하다. 그 때문에 이미 다른 언어로 작성된 많은 프로그램과 모듈이 파이썬으로 재구성되고 있다. 국내에서도 그 가치를 인정받아 사용자 층이 더욱 넓어지고 있고, 파이썬을 사용해 프로그램을 개발하는 업체들 또한 늘어 가고 있는 추세이다.


pandas DataFrame에서 index를 통해 해당하는 row를 찾을 때 사용하는 .iloc, .loc, .ix는 겉보기에 다르지 않지만 각각의 용도가 다르다고 한다.

.iloc

integer positon를 통해 값을 찾을 수 있다. label로는 찾을 수 없다

.loc

label 을 통해 값을 찾을 수 있다. integer position로는 찾을 수 없다.

.ix

integer position과 label모두 사용 할 수 있다. 만약 label이 숫자라면 label-based index만 된다.