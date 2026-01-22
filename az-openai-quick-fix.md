# Azure OpenAI Quick Fix

🚨 **Big Issue:** Azure OpenAI script gets empty response. JSON parser crashes. 😵 Now fixed with clear error messages! 📢 Shows exact response & what's wrong.

✅ **Test it:**  

```bash
python azure_simple_query.py --prompt "Who are you?"
```

🔍 **Top Fixes:**

1. **Endpoint URL wrong** ❌ – Must be 
FULL: 

`https://YOUR-RESOURCE.openai.azure.com/openai/deployments/YOUR-DEPLOYMENT/chat/completions?api-version=2024-02-15-preview`

2. **Bad API key** 🔑 – Check `AZURE_OPENAI_API_KEY`

3. **Old API version** 📅 – Update to `2024-02-15-preview`

🎯 **Your Error:** URL too short! `https://azopenai.openai.azure.com` → Server says "OK" (200) but empty cuz no path. 🕵️

🗺️ **Find YOUR Deployment Name:**

- Azure Portal → Your OpenAI resource
- Left menu: **Deployments**
- Copy name like "gpt-4" or "gpt-35-turbo" 📋

🔧 **Set Endpoint:**

```bash
export AZURE_OPENAI_ENDPOINT="https://azopenai.openai.azure.com/openai/deployments/YOUR-DEPLOYMENT-NAME/chat/completions?api-version=2024-02-15-preview"
```

**Or quick run:**

```bash
python azure_simple_query.py --url "https://azopenai.openai.azure.com/openai/deployments/YOUR-DEPLOYMENT-NAME/chat/completions?api-version=2024-02-15-preview" --prompt "Who are you?"
```

<br>
