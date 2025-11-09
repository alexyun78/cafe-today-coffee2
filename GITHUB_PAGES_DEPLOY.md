# 🚀 GitHub Pages 배포 가이드 (서버 없이!)

## ✨ 특징

- ✅ **완전 무료** - GitHub Pages 사용
- ✅ **서버 불필요** - 순수 HTML/JavaScript
- ✅ **자동 업데이트** - GitHub Actions로 주기적 업데이트
- ✅ **안전** - API Token을 GitHub Secrets에 보관
- ✅ **빠름** - CDN을 통한 전 세계 배포

---

## 📋 작동 원리

```
1. GitHub Actions가 매시간 실행
   ↓
2. Notion API에서 데이터 가져오기
   ↓
3. data/coffee.json 파일 생성
   ↓
4. GitHub에 커밋 & 푸시
   ↓
5. GitHub Pages가 자동 배포
   ↓
6. 사용자가 접속하면 JSON 읽어서 표시
```

---

## 🚀 배포 단계

### 1단계: GitHub 저장소 생성

1. GitHub에 로그인
2. 새 저장소 생성
   - Repository name: `cafe-today-coffee2`
   - **Public** 선택 (GitHub Pages 무료)
   - Initialize with README 체크 안 함

### 2단계: 파일 업로드

다음 파일들을 저장소에 업로드:

```
cafe-today-coffee/
├── .github/
│   └── workflows/
│       └── update-data.yml       # GitHub Actions 워크플로우
├── data/
│   └── .gitkeep                   # 빈 폴더 유지
├── index.html                     # 정적 웹 페이지
├── fetch_notion_data.py           # Notion 데이터 가져오기 스크립트
└── README.md                      # 설명서
```

**방법 A: Git 명령어**

```bash
cd D:\python\92\cafe-today-coffee-static

# 필요한 파일만 복사
# (index-static.html을 index.html로 이름 변경)

git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/alexyun78/cafe-today-coffee2.git
git branch -M main
git push -u origin main
```

**방법 B: GitHub 웹 인터페이스**

1. 저장소 페이지에서 `Add file` → `Upload files`
2. 파일들을 드래그 앤 드롭
3. `Commit changes`

### 3단계: GitHub Secrets 설정

1. **저장소 Settings** 클릭
2. 왼쪽 메뉴에서 **Secrets and variables** → **Actions** 클릭
3. **New repository secret** 클릭

**Secret 추가:**

| Name | Value |
|------|-------|
| `NOTION_TOKEN` | `` |
| `DATABASE_ID` | `` |

**⚠️ 중요:** 본인의 실제 Token과 Database ID를 입력하세요!

### 4단계: GitHub Pages 활성화

1. **저장소 Settings** 클릭
2. 왼쪽 메뉴에서 **Pages** 클릭
3. **Source** 섹션에서:
   - Branch: `main` 선택
   - Folder: `/ (root)` 선택
4. **Save** 클릭

### 5단계: GitHub Actions 실행

1. **Actions** 탭 클릭
2. **Update Coffee Data** 워크플로우 선택
3. **Run workflow** → **Run workflow** 클릭
4. 완료 대기 (1-2분)

### 6단계: 접속!

웹사이트 URL이 생성됩니다:

```
https://alexyun78.github.io/cafe-today-coffee2/
```

---

## ⚙️ 업데이트 주기 설정

`.github/workflows/update-data.yml` 파일에서 cron 표현식 수정:

```yaml
schedule:
  # 매 30분마다
  - cron: '*/30 * * * *'
  
  # 매 시간마다 (기본값)
  - cron: '0 * * * *'
  
  # 매 6시간마다
  - cron: '0 */6 * * *'
  
  # 매일 아침 9시 (KST 기준은 0시 = UTC)
  - cron: '0 0 * * *'
```

---

## 🎯 QR 코드 생성

1. **QR 코드 생성 사이트 접속**
   - https://www.qr-code-generator.com/

2. **URL 입력**
   ```
   https://alexyun78.github.io/cafe-today-coffee2/
   ```

3. **QR 코드 생성 및 다운로드**

4. **매장에 게시**

---

## 🔧 커스텀 도메인 설정 (선택사항)

### 1. 도메인 구매
   - Cloudflare, Namecheap 등

### 2. DNS 설정

도메인 DNS 관리에서 CNAME 레코드 추가:

```
Type: CNAME
Name: www (또는 @)
Value: alexyun78.github.io
```

### 3. GitHub Pages에서 설정

Settings → Pages → Custom domain:
```
www.your-domain.com
```

### 4. HTTPS 활성화

Enforce HTTPS 체크박스 선택

---

## 📊 비교: Flask vs GitHub Pages

| 항목 | Flask (Render) | GitHub Pages |
|------|----------------|--------------|
| **서버** | 필요 | 불필요 |
| **비용** | 무료 (제한 있음) | 완전 무료 |
| **실시간 업데이트** | ✅ 즉시 | ⏱️ 주기적 (설정 가능) |
| **슬립 모드** | 있음 (15분) | 없음 |
| **속도** | 느림 (슬립 시) | 매우 빠름 (CDN) |
| **유지보수** | 필요 | 거의 불필요 |
| **설정 난이도** | 중간 | 쉬움 |

---

## 💡 장점

### ✅ 서버 관리 불필요
- Render 무료 플랜의 슬립 모드 없음
- 항상 빠른 응답 속도

### ✅ 완전 무료
- GitHub Actions: 월 2,000분 무료
- GitHub Pages: 무료
- 추가 비용 없음

### ✅ 안정적
- GitHub의 글로벌 CDN
- 99.9% 업타임

### ✅ 빠름
- 정적 파일 제공
- CDN 캐싱

---

## ⚠️ 단점

### ❌ 실시간 업데이트 아님
- 최소 업데이트 주기: 5분 (GitHub Actions 제한)
- 권장 주기: 30분 ~ 1시간

**해결책:** 카페 운영 특성상 커피 변경이 자주 있지 않으므로 큰 문제 없음

### ❌ GitHub Actions 제한
- 무료 플랜: 월 2,000분
- 매시간 업데이트 시: 약 1,440분/월 사용 (충분함!)

---

## 🔍 문제 해결

### Actions 실패

**증상:** Workflow가 실패함

**해결:**
1. Actions 탭 → 실패한 워크플로우 클릭
2. 로그 확인
3. Secrets 설정 확인

### 페이지가 안 열림

**증상:** 404 Not Found

**해결:**
1. Settings → Pages 에서 URL 확인
2. `index.html` 파일이 루트에 있는지 확인
3. 5-10분 대기 (배포 시간)

### 데이터가 업데이트 안 됨

**증상:** Notion 변경사항이 반영 안 됨

**해결:**
1. Actions 탭에서 마지막 실행 시간 확인
2. 수동 실행: Run workflow 클릭
3. Integration이 Database에 연결되어 있는지 확인

---

## 🎉 완료!

이제 다음이 가능합니다:

- ✅ 서버 없이 웹사이트 운영
- ✅ 자동으로 Notion 데이터 동기화
- ✅ 빠른 속도와 안정성
- ✅ 완전 무료

**URL:** `https://alexyun78.github.io/cafe-today-coffee2/`

QR 코드를 생성해서 매장에 부착하세요! ☕✨
