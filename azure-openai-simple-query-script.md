Yesss — I got you 😌💙
Here's a clean little Python script that does exactly that:

* You set:

  * `AZURE_OPENAI_API_KEY` (required)
  * `AZURE_OPENAI_ENDPOINT` (optional, if you don't want to pass the URL every time)
* Then you can run a simple prompt and get the model's answer back.

---

## ✅ `azure_simple_query.py`

---

## ✅ Usage

### 1) Set your secret

```bash
export AZURE_OPENAI_API_KEY="YOUR_KEY_HERE"
```

### 2) Run with URL + prompt

```bash
python3 azure_simple_query.py \
  --url "https://YOUR-RESOURCE.openai.azure.com/openai/deployments/YOUR-DEPLOYMENT/chat/completions?api-version=2024-02-15-preview" \
  --prompt "What is DNS?"
```

### Or pipe input

```bash
echo "Explain CIDR in one paragraph" | python3 azure_simple_query.py --url "https://..."
```

### Optional: don't pass URL every time

```bash
export AZURE_OPENAI_ENDPOINT="https://YOUR-RESOURCE.openai.azure.com/openai/deployments/YOUR-DEPLOYMENT/chat/completions?api-version=2024-02-15-preview"
python3 azure_simple_query.py -p "Give me 3 bash aliases for kubectl"
```

---

If you want, I can also make you a *slightly more deluxe* version that:

<br>
