# DevSecOps Pipeline Demo

## 程式語言

**Python 3.12** + **Flask 3.0**

## 應用程式說明

一個簡易的 REST API 計算機，提供加法與減法的 HTTP 端點：

| 端點 | 說明 |
|------|------|
| `GET /` | 健康檢查 |
| `GET /add/<a>/<b>` | 回傳 a + b |
| `GET /subtract/<a>/<b>` | 回傳 a - b |

## Pipeline 架構

```
push to GitHub
  │
  ├─ 🧪 Stage 1: Test
  │     install dependencies → run pytest → upload coverage
  │
  ├─ 📦 Stage 2: Build
  │     verify app can be imported/packaged
  │
  ├─ 🔍 Stage 3: Dependency Vulnerability Scan
  │     Trivy filesystem scan (HIGH/CRITICAL) → generate SBOM (CycloneDX)
  │
  ├─ 🔐 Stage 4: Secret Scan
  │     Gitleaks (掃描 git history 中是否含有 API key、密碼等機密)
  │
  └─ 🛡️ Stage 5: Static Code Analysis
        Bandit (Python 安全靜態分析) → upload report
```

## 本地執行

```bash
# 安裝依賴
pip install -r requirements.txt

# 執行測試
pytest test_app.py -v

# 啟動應用
python app.py
```

## 掃描工具說明

| 工具 | 類型 | 說明 |
|------|------|------|
| [Trivy](https://github.com/aquasecurity/trivy) | Dependency Scan | 掃描 requirements.txt 中套件的 CVE 漏洞，並產生 SBOM |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Secret Scan | 掃描整個 git history，偵測是否有 API key、密碼等機密外洩 |
| [Bandit](https://github.com/PyCQA/bandit) | Static Analysis | Python 專用安全靜態分析，偵測常見安全問題（如 SQL injection、硬編碼密碼） |
