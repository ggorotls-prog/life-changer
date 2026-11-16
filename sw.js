// 라이프 체인저 관리자: 폰에 앱으로 설치되게 하는 파일(2026-11-16 룡).
// 아무것도 저장하지 않는다. 늘 인터넷에서 새로 받는다(옛 화면이 남지 않게).
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', (e) => e.waitUntil(self.clients.claim()));
self.addEventListener('fetch', () => {});
