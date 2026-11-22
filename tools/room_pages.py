# 방마다 카톡 미리보기에 방 이름이 나오는 작은 페이지(room/<방코드>/index.html)를 만든다.
# 카톡 미리보기는 페이지의 og:title만 읽고 JS는 안 돌린다. 그래서 방마다 정적 페이지가 따로 있어야 한다.
# 이 페이지는 사람이 열면 바로 참가자 화면(room/?r=방코드)으로 넘어간다.
# 새 방을 만들면: 아래 ROOMS에 (방코드, 방 이름)을 더하고 `python tools/room_pages.py` → 저장소에 올린다.
# 방 이름·코드는 슈파베이스 hero_rooms(id, name).
import html, json, os

ROOMS = [
    ('hero', '히어로'),
    ('788f6662', '박인정셀'),
]

BASE = 'https://ggorotls-prog.github.io/life-changer/room/'
HERE = os.path.dirname(os.path.abspath(__file__))

PAGE = '''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="라이프 체인저 1단계 운동방 · 이름을 고르고 오늘 운동을 인증해요">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://ggorotls-prog.github.io/life-changer/icon-512.png">
<script>location.replace({target} + location.hash);</script>
</head>
<body style="font-family:sans-serif;text-align:center;padding:40px 16px">
<p><a href={target_attr}>{title} 열기</a></p>
</body>
</html>
'''

for rid, name in ROOMS:
    title = '💪 ' + name + ' 운동 챌린지'
    target = '../?r=' + rid
    d = os.path.join(HERE, '..', 'room', rid)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, 'index.html'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(PAGE.format(title=html.escape(title), url=html.escape(BASE + rid + '/'),
                            target=json.dumps(target), target_attr='"' + html.escape(target) + '"'))
    print('만듦', rid, title)
