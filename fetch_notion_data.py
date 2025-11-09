import os
import json
import requests
from datetime import datetime

# 환경 변수에서 읽기
NOTION_TOKEN = os.environ.get('NOTION_TOKEN')
DATABASE_ID = os.environ.get('DATABASE_ID')

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

def query_all(db_id):
    url = f"https://api.notion.com/v1/databases/{db_id}/query"
    payload = {"page_size": 100}
    results = []
    while True:
        res = requests.post(url, headers=headers, json=payload, timeout=30)
        res.raise_for_status()
        data = res.json()
        results.extend(data.get("results", []))
        if not data.get("has_more"):
            break
        payload["start_cursor"] = data["next_cursor"]
    return results

def humanize_property(prop: dict):
    t = prop.get("type")
    if not t:
        return None
    if t == "title":
        return "".join(r.get("plain_text","") for r in prop["title"]).strip() or None
    if t == "rich_text":
        return "".join(r.get("plain_text","") for r in prop["rich_text"]).strip() or None
    if t == "number":
        return prop["number"]
    if t == "select":
        return prop["select"]["name"] if prop["select"] else None
    if t == "multi_select":
        return [o["name"] for o in prop["multi_select"]]
    if t == "status":
        return prop["status"]["name"] if prop["status"] else None
    if t == "date":
        if not prop["date"]:
            return None
        s = prop["date"]["start"]
        e = prop["date"].get("end")
        return {"start": s, "end": e} if e else {"start": s, "end": None}
    if t in {"created_time","last_edited_time"}:
        return prop[t]
    return None

def flatten_row(page: dict) -> dict:
    out = {}
    for name, prop in page.get("properties", {}).items():
        out[name] = humanize_property(prop)
    return out

def parse_date(date_obj):
    if not date_obj:
        return None
    if isinstance(date_obj, dict):
        date_str = date_obj.get("start")
        if date_str:
            try:
                return datetime.fromisoformat(date_str.replace("Z", "+00:00"))
            except:
                return None
    return None

# 데이터 가져오기
print("Fetching data from Notion...")
pages = query_all(DATABASE_ID)
print(f"Found {len(pages)} pages")

all_coffee = []
today_coffee = []

for pg in pages:
    row = flatten_row(pg)
    coffee_data = {
        "커피": row.get("커피"),
        "로스팅": row.get("로스팅"),
        "프로세싱": row.get("프로세싱"),
        "상태": row.get("상태"),
        "컵노트": row.get("컵노트"),
        "감상": row.get("감상"),
        "제공일": row.get("제공일")
    }
    
    all_coffee.append(coffee_data)
    
    if coffee_data["상태"] == "진행 중":
        today_coffee.append(coffee_data)

# 정렬
def sort_key(item):
    date_obj = item.get("제공일")
    provide_date = parse_date(date_obj)
    
    roast_obj = item.get("로스팅")
    roast_date = parse_date(roast_obj)
    
    provide_time = provide_date.timestamp() if provide_date else 0
    roast_time = roast_date.timestamp() if roast_date else 0
    
    return (-provide_time, -roast_time)

all_coffee.sort(key=sort_key)

# JSON으로 저장
output = {
    "success": True,
    "updated_at": datetime.now().isoformat(),
    "today": today_coffee,
    "history": all_coffee
}

# data 디렉토리 생성
os.makedirs("data", exist_ok=True)

# JSON 파일 저장
with open("data/coffee.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"✅ Data saved to data/coffee.json")
print(f"   - Today's coffee: {len(today_coffee)}")
print(f"   - Total history: {len(all_coffee)}")
