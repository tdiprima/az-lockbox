#!/usr/bin/env python3
import argparse
import json
import os
import sys
import urllib.error
import urllib.request


def call_azure_openai(endpoint_url: str, api_key: str, prompt: str, timeout: int = 60):
    """
    Calls Azure OpenAI Chat Completions endpoint via raw HTTPS request.
    Works with endpoint URLs like:
      https://YOUR-RESOURCE.openai.azure.com/openai/deployments/YOUR-DEPLOYMENT/chat/completions?api-version=2024-02-15-preview
    """

    payload = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.7,
        "max_tokens": 400,
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        endpoint_url,
        data=data,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "api-key": api_key,
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body)

    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(
            f"HTTP {e.code} {e.reason}\n"
            f"Endpoint: {endpoint_url}\n"
            f"Response body:\n{err_body}"
        ) from e

    except urllib.error.URLError as e:
        raise RuntimeError(f"Network error: {e}") from e


def extract_answer(result_json: dict) -> str:
    """
    Extracts the assistant message from Azure OpenAI chat completions response.
    """
    try:
        return result_json["choices"][0]["message"]["content"].strip()
    except Exception:
        return json.dumps(result_json, indent=2)


def main():
    parser = argparse.ArgumentParser(
        description="Tiny Azure OpenAI query script (env var auth, URL endpoint)."
    )
    parser.add_argument(
        "--url",
        default=os.getenv("AZURE_OPENAI_ENDPOINT"),
        help="Full Azure OpenAI endpoint URL (or set AZURE_OPENAI_ENDPOINT).",
    )
    parser.add_argument(
        "--prompt",
        "-p",
        default=None,
        help="Prompt text to send. If omitted, reads from stdin.",
    )
    parser.add_argument("--timeout", type=int, default=60, help="HTTP timeout seconds.")

    args = parser.parse_args()

    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    if not api_key:
        print("ERROR: AZURE_OPENAI_API_KEY env var is not set.", file=sys.stderr)
        sys.exit(2)

    if not args.url:
        print(
            "ERROR: Missing endpoint URL. Provide --url or set AZURE_OPENAI_ENDPOINT.",
            file=sys.stderr,
        )
        sys.exit(2)

    prompt = args.prompt
    if not prompt:
        prompt = sys.stdin.read().strip()

    if not prompt:
        print("ERROR: Prompt is empty.", file=sys.stderr)
        sys.exit(2)

    result = call_azure_openai(args.url, api_key, prompt, timeout=args.timeout)
    answer = extract_answer(result)
    print(answer)


if __name__ == "__main__":
    main()
