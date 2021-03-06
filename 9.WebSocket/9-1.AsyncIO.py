# 9. 웹소켓을 이용한 실시간 시세 처리
# AsyncIO 기초
# 비동기처리 방식이 동기처리 방식보다 좋아지려면 수행할 작업이 단순 연산 중심이 아니라
# 중간마다 쉴 수 있는 형태의 작업이어야 한다.

# 파이썬에서는 async 키워드가 있는 함수를 코루틴이라고 부른다.

import asyncio

# 코루틴은 일반 함수처럼 호출할 수 없다.
async def async_func1():
    print("Hello")

# 코루틴을 처리하기 전에 먼저 이벤트 루프를 만들고
# 코루틴의 처리가 끝난 뒤에는 이벤트 루프를 닫아주면 된다.
# 이러한 역할을 간단히 처리해주는 것이 asyncio 모듈의 run 함수이다.
asyncio.run(async_func1())