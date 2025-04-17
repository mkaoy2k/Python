"""
此檔案為一個使用 FastAPI 框架實作的簡易 RESTful API 範例，包含以下功能：

1. 定義了一個 Pydantic 的 User 資料模型，包含姓名（name）、電子郵件（email）以及可選的年齡（age）欄位。
2. 提供一個 POST /users 的 API 路徑，接收來自用戶端的 User 資料，並回傳建立成功的訊息以及該用戶資料。
3. 使用 EmailStr 型別驗證 email 欄位格式，確保資料正確性。
4. age 欄位為可選，預設為 None，提升彈性。
5. 適合用於學習 FastAPI 與 Pydantic 的基本應用與資料驗證流程。

本範例未涉及資料庫操作，僅作為 API 輸入與驗證的展示。

你可以依下列步驟操作：

1. 啟動 FastAPI 伺服器：`uvicorn greetings2:app --reload`
2. Client 
   - 使用 Postman 或其他工具測試 API：`POST http://127.0.0.1:8000/users`
   - 請求體（Body）：`{"name": "John Doe", "email": "john.doe@example.com", "age": 30}`
   - 預期回應：`{"message": "User created", "user": {"name": "John Doe", "email": "john.doe@example.com", "age": 30}}`
   - 訪問 API 文檔：`http://127.0.0.1:8000/docs`
3. Control-C 停止伺服器
"""

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional

app = FastAPI()

# Pydantic model for request/response
class User(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None  # Optional field with default None

@app.post("/users")
async def create_user(user: User):
    return {"message": "User created", "user": user}


def main():
    import uvicorn
    # 使用 uvicorn 啟動 FastAPI 應用
    uvicorn.run("greetings2:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    main()
