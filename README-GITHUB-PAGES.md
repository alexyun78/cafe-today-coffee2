# ☕ 오늘의 커피 - GitHub Pages 버전

서버 없이 GitHub Pages로 운영하는 "오늘의 커피" 웹 애플리케이션

## ✨ 특징

- 🆓 **완전 무료** - 서버 비용 없음
- ⚡ **빠른 속도** - GitHub CDN 사용
- 🔄 **자동 업데이트** - GitHub Actions로 주기적 동기화
- 🔒 **안전** - API Token을 Secrets에 보관
- 📱 **반응형** - 모바일/태블릿/PC 최적화

## 🚀 빠른 시작

### 1. 이 저장소를 Fork 또는 Clone

```bash
git clone https://github.com/alexyun78/cafe-today-coffee-static.git
cd cafe-today-coffee-static
```

### 2. GitHub Secrets 설정

Settings → Secrets and variables → Actions → New repository secret

| Secret Name | Value |
|-------------|-------|
| `NOTION_TOKEN` | 본인의 Notion Integration Token |
| `DATABASE_ID` | 본인의 Notion Database ID |

### 3. GitHub Pages 활성화

Settings → Pages → Source: `main` branch → Save

### 4. GitHub Actions 실행

Actions → Update Coffee Data → Run workflow

### 5. 완료!

웹사이트 접속: `https://[username].github.io/[repository-name]/`

## 📖 상세 가이드

**[GITHUB_PAGES_DEPLOY.md](GITHUB_PAGES_DEPLOY.md)** - 전체 배포 가이드

## 📁 파일 구조

```
cafe-today-coffee-static/
├── .github/
│   └── workflows/
│       └── update-data.yml       # GitHub Actions 워크플로우
├── data/
│   └── coffee.json                # Notion 데이터 (자동 생성)
├── index.html                     # 웹 페이지
├── fetch_notion_data.py           # 데이터 가져오기 스크립트
└── README.md                      # 이 파일
```

## 🔄 업데이트 주기

기본값: **매 시간마다** 자동 업데이트

변경하려면 `.github/workflows/update-data.yml` 파일 수정:

```yaml
schedule:
  - cron: '0 * * * *'  # 매 시간
  # - cron: '*/30 * * * *'  # 매 30분
  # - cron: '0 */6 * * *'  # 매 6시간
```

## 🎯 사용 방법

### QR 코드 생성

1. https://www.qr-code-generator.com 접속
2. GitHub Pages URL 입력
3. QR 코드 생성 및 다운로드
4. 매장에 게시

### 수동 업데이트

Actions → Update Coffee Data → Run workflow 클릭

## 📊 GitHub Pages vs Render

| 항목 | GitHub Pages | Render |
|------|--------------|--------|
| 비용 | 무료 | 무료 (제한) |
| 속도 | 매우 빠름 | 보통 |
| 실시간 업데이트 | ❌ (주기적) | ✅ |
| 슬립 모드 | ❌ 없음 | ✅ 있음 |
| 서버 관리 | 불필요 | 필요 |

## 💡 팁

### 커스텀 도메인

Settings → Pages → Custom domain에 도메인 입력

### HTTPS 강제

Settings → Pages → Enforce HTTPS 체크

### 모니터링

Actions 탭에서 워크플로우 실행 상태 확인

## 🆘 문제 해결

### Actions 실패
→ Secrets 설정 확인 (NOTION_TOKEN, DATABASE_ID)

### 페이지 404
→ GitHub Pages 활성화 확인, 5분 대기

### 데이터 업데이트 안 됨
→ Notion Integration이 Database에 연결되었는지 확인

## 📞 지원

문제가 발생하면 [Issues](../../issues)에 문의하세요.

## 📄 라이선스

MIT License

---

**Made with ☕ for coffee lovers**
