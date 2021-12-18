from irc import *
import time
import random

server = "moe.uriirc.org"
port = 16664
nickname = "Pikachu"
channel = "#zxcvber"
channels = ["#zxcvber"]

users = ["zxcvber"]
pika = ["Pika!", "Pika?", "Pikachu!"]
infostr = "#025 피카츄/Pikachu, Lv. 100 (전기) // 차분한 성격 // 특성: 정전기 // 기술: 10만볼트/아이언테일"
ASKY = " 당신의 애인은 안생겨요!!!"

amumal = ["Wingardium Leviosa~", "'기계'가 되어라!\n기계가 싫으면 싫을수록 '기계'보다는 우수해야 한다.", "Amumal3", "Amumal4", "Amumal5"]

linalg = ["ㅎㅎ.", "ㅋㅋ.", "그러므로 웃지만 말고 긴장하기 바란다.","...... 같은 것은 같다.", "자명. ☐", "당연. (정말 아무리 생각해 보아도 쓸 것이 없다.) ☐", "이제 같은 것을 두 개의 이름으로 부를 필요는 없다.", "연습장을 꺼낸다.", "우리가 아는 것은 행렬 뿐이다.", "이 장면에서, 눈치 빠른 독자들은 무언가 느낌이 있었을 것이다.\n그리고, 그렇게 되도록 훈련하여야 한다.", "추상화는 목적이 아니라 typical example 을 이해하기 위한 도구이다.", "우리는 항상 '고향'부터 생각한다는 뜻이다.", "자손의 자손은 자손이다!", "종이 낭비", "잉크 낭비", "분필 낭비", "데이터 낭비", "종이를 아끼자...", "1층과 2층의 구조가 똑같을 때, 1층에 궁금한 것이 있다면 2층에 올라가 살펴보면 된다. 3층에서 내려다 보면 된다.", "왜 그런가?", "두고두고 종이를 절약해 줄 것이다.", "이제 [연습장]은 숨기고 - 마치 아무 일도 없었다는 듯이 - [연습장]을 거꾸로 복사하면 증명 끝. ☐", "학부 수준에서 '수학적 기초론'에 빠지는 것은 위험하다.", "어디서 많이 본 풍경이다.", "독자들은 - 책을 덮고 - '기계'가 되어 증명해 보라.", "쌩뚱맞게 [우리의 철학]이라니? ㅎㅎ.", "이 증명은 '기계'가 한다.", "종이와 연필만 있다면 언제라도 이 증명을 할 수 있다는 확신이 생길 때 까지...", "같은 것은 정말 똑같다.", "이름을 고쳐서 이름도 같게 만들면 된다", "'본능' = 맞아 가며 몸에 익혔다 = 손(연필)이 먼저 저절로 움직인다....", "왜 허전한지는 몇 년 후에 알게 된다.", "다음 연습문제들은 독자들에게 맡긴다.", "이 0이 몇 번째 0인지 아는 사람?", "생략. ☐", "Injective if and only if surjective!", "독자들은 '기계'라는 말이 나오면 즉시 책을 덮고 스스로 '기계'가 되어....", "지금은 '달리기 훈련' 중.", "낙엽이 떨어질 때, 다시 만나게 된다.", "행렬과 선형사상은 같은 것이다.", "이젠 모든 것이 단순 명료하다.", "흥미로운 소재를 만났으니 잠시 옆길로 샌다.", "골치 아픈 수학이 아니라 재미있는 '이야기'였다는 데에 동의해 주어야 한다.", "우리의 '이야기의 줄거리'에는 벡터공간, 기저, 차원, 선형사상, Dimension Theorem, 기본정리로 이어지는 분명한 순서와 체계가 있다.", "다음 증명은 정말 산뜻하다.", "3층에서 보면 완전히 겹쳐 보일 것이다.", "선형사상 L: V -> W 는 L_A : F^n -> F^m 과 같은 함수이다.", "여기가 바로 '선형대수학의 전환점'이다!", "'닮음' 관계의 공부는 이것으로 끝!", "증명은 생략한다.", "A ~ B 이면 A와 B는 같고, 같은 것은 같고, 온통 다 같다...., ㅎㅎ.", "다음 관찰은 앞으로 우리의 '사고방식'이 된다.", "비둘기들도 알고 있다.", "비둘기들이 우리에게 말해준다."]


irc = IRC()
irc.connect(server, channel, port, nickname)

while True:
    for username in users:
        try:
            for i in range(4):
                text = irc.get_text()
                # print(text)
                chanidx = text.find("#")
                chanidx2 = text[chanidx:].find(" ")
                channelname = text[chanidx:chanidx + chanidx2]
                # print(channelname)
                if "INVITE" in text:
                    idx = text[1:].find(":")
                    msg = text[idx + 2:].strip()
                    # print(msg)
                    irc.join(msg)
                    channels.append(msg)
                    irc.send(msg, "피카츄!")
                if "PRIVMSG" in text and channelname in channels:
                    idx = text[1:].find(":")
                    msg = text[idx + 2:]
                    print(msg, end="")
                    if msg.startswith("피카츄!") or msg.find("피카츄?") != -1:
                        irc.send(channelname, pika[random.randint(0, len(pika) - 1)])
                    if msg.startswith("!op"):
                        irc.give_op(channelname, "calofmijuck")
                    if msg.startswith("!ping"):
                        irc.send(channelname, "pong!")
                    if msg.startswith("!pong"):
                        irc.send(channelname, "ping!")
                    if msg.startswith("피카츄 안녕"):
                        irc.send(channelname, "안녕 " + text.split("!")[0][1:] + "!")
                    if msg.startswith("피카츄 10만볼트"):
                        irc.send(channelname, "피카-츄유유유유유유!!")
                    if msg.startswith("피카츄 아이언테일"):
                        irc.send(channelname, "피-카!")
                    if msg.startswith("피카츄 정보"):
                        irc.send(channelname, infostr)
                    if msg.startswith("피카츄 운세"):
                        irc.send(channelname, text.split("!")[0][1:] + ASKY)
                    if msg.startswith("피카츄 선대"):
                        irc.send(channelname, linalg[random.randint(0, len(linalg) - 1)])
                    if msg.startswith("피카츄 아무말"):
                        irc.send(channelname, amumal[random.randint(0, len(amumal) - 1)])

        except Exception as ex: pass
