# Ollama Guide: Installing and Running the Two Class Models

**Status:** Draft for team review. Used in Week 5 (provider abstraction and the Ollama adapter), and in the Harbour labs from then on.
**Models:** `qwen2.5:7b` (the class default) and `llama3.1:8b` (the comparison model).
**Checked:** against the Ollama documentation and current third-party guides in November 2026. Ollama's commands and variables change between releases. If a command here doesn't match your version, run `ollama --help` or check ollama.com.

---

## 1. What you will have at the end

- Ollama installed on your laptop, with the server running in the background.
- Both models downloaded and tested with the command line and with a short script.
- Your laptop set up so that only one model is in memory at a time.
- A way to record token counts and response times, so the two models can be compared on the same test set.

---

## 2. Check your laptop first

| Item | Team standard | What it means |
|---|---|---|
| RAM | 16 GB | `qwen2.5:7b` needs about 5.7 GB at an 8K context. Docker, VS Code and the browser also use memory. |
| Storage | 512 GB SSD | Both models together need about 10 GB, plus Docker. |
| Processor | Any modern CPU, or Apple silicon | Without a dedicated GPU the model runs on the CPU. It works, but it's slower. |

### CPU-only laptops (no GPU)

No GPU is needed. Ollama detects that there is no GPU and runs the model on the CPU automatically. Nothing needs to be configured. `ollama ps` will show `100% CPU` for a loaded model. That is expected on your machines, not a fault.

**What to expect (estimates from third-party benchmarks, not measured on team laptops):**

| Setup | Estimated generation speed for a 7B to 8B model |
|---|---|
| Recent multi-core laptop CPU with 16 GB of RAM | roughly 6 to 15 tokens per second |
| Older or budget laptop CPU | roughly 3 to 7 tokens per second |

Speed depends mostly on the processor and how fast the memory is, so two laptops with 16 GB can differ a lot. A short triage answer of 50 to 100 tokens takes about 5 to 20 seconds. Long answers take longer. Prompt processing is usually quicker than generation.

**What this means for the labs:**
- Triage and classification tests (short output) are practical on CPU.
- Long answers, large contexts and many runs are slow. Keep `num_ctx` at 8192 or lower, and keep test sets to 10 to 20 inputs.
- A comparison run of 20 inputs on both models may take 10 to 30 minutes per model. Plan it as an offline task, not a live demo.
- Apple silicon Macs usually run these models faster than Intel or AMD laptops of the same age, because the chip and memory are built together.
- Use your first run to measure the real speed on your laptop, and record it in the comparison note (section 10). Don't rely on the estimates above.

**Check your processor:**
- Windows: Task Manager, Performance tab, CPU.
- macOS: Apple menu, About This Mac.
- Linux: `lscpu`.

**If your laptop has 8 GB of RAM:** use a smaller model such as `qwen3.5:4b` for labs, or share a stronger laptop on the class network (section 9). Tell the instructor before the first lab so the team can plan.

**If your laptop has 16 GB but feels slow:** close other applications, keep Docker stopped unless you need it, and check section 11.

---

## 3. Install Ollama

Install only from **ollama.com**. Be careful with one-line install commands shared in videos or chat groups. The official ones are shown below.

### Windows

Option A, the installer:
1. Go to ollama.com/download and download `OllamaSetup.exe`.
2. Run it. It installs for your user account and does not need administrator rights.
3. Ollama runs in the system tray after installation.

Option B, PowerShell or winget:
```powershell
winget install Ollama.Ollama
```
or
```powershell
irm https://ollama.com/install.ps1 | iex
```
Only use the second command if your organisation's script policy allows it.

### macOS

Option A, the app: download `Ollama.dmg` from ollama.com/download, drag Ollama into Applications, and open it. It runs as a menu-bar app.

Option B, Homebrew:
```bash
brew install ollama
```

### Linux

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

To read the script before running it:
```bash
curl -fsSL https://ollama.com/install.sh -o install.sh
less install.sh
sh install.sh
```

The script installs Ollama as a systemd service, so it starts automatically.

### Check the installation

Open a new terminal (PowerShell or Command Prompt on Windows) and run:

```bash
ollama --version
```

If you see a version number, the command works. If you get "command not found", close the terminal and open a new one. On Windows, the installer adds Ollama to your PATH for new sessions, so a restart may be needed.

---

## 4. Set up Ollama

Ollama is controlled by environment variables. Set them once, then restart Ollama.

### The variables the team uses

| Variable | Recommended value | Why |
|---|---|---|
| `OLLAMA_HOST` | `127.0.0.1:11434` (the default) | Keeps the server reachable only from your laptop. Change it only in section 9. |
| `OLLAMA_MODELS` | A folder with at least 15 GB free | Moves model storage off a nearly full drive. Optional. |
| `OLLAMA_KEEP_ALIVE` | `5m` (the default) | A model stays in memory for 5 minutes after its last request. |
| `OLLAMA_MAX_LOADED_MODELS` | `1` | Stops two 7B models from loading together and swapping on 16 GB. |
| `OLLAMA_NUM_PARALLEL` | `1` | One request at a time per model. Simplest on a laptop. |
| `OLLAMA_CONTEXT_LENGTH` | `8192` | A reasonable context for labs. The default depends on memory and may be smaller. |
| `OLLAMA_NO_CLOUD` | `1` | Disables cloud models and web search, so lab runs stay on your laptop. |

Test your settings after you change them. Memory use goes up with context length, so check that the laptop stays responsive.

### Windows: set variables

1. Quit Ollama from the system tray.
2. Open **Settings**, search for **environment variables**, and choose **Edit environment variables for your account**.
3. Under **User variables**, click **New**, enter the name and value (for example `OLLAMA_MAX_LOADED_MODELS` and `1`), and click **OK**. Repeat for each variable.
4. Click **OK** to close the window.
5. Start Ollama again from the Start menu.

### macOS: set variables

For the Ollama app, use `launchctl`:

```bash
launchctl setenv OLLAMA_MAX_LOADED_MODELS "1"
launchctl setenv OLLAMA_CONTEXT_LENGTH "8192"
launchctl setenv OLLAMA_NO_CLOUD "1"
```

Then quit the Ollama app and open it again. These settings may not survive a restart, so check them after a reboot with `ollama ps`, and set them again if needed.

### Linux: set variables (systemd)

```bash
sudo systemctl edit ollama
```

In the editor, add the variables under `[Service]`:

```ini
[Service]
Environment="OLLAMA_MAX_LOADED_MODELS=1"
Environment="OLLAMA_CONTEXT_LENGTH=8192"
Environment="OLLAMA_NO_CLOUD=1"
```

Save, then run:

```bash
sudo systemctl daemon-reload
sudo systemctl restart ollama
```

### Move model storage (optional)

If the default folder is on a full drive, set `OLLAMA_MODELS` to another folder using the steps above, then restart Ollama. Models already downloaded to the old folder need to be pulled again, or copied across before you restart.

---

## 5. Start the server and check it

On Windows and macOS the app starts the server for you. On Linux the service does. If you need to start it by hand in a terminal:

```bash
ollama serve
```

Leave that terminal open. Then, in another terminal, check the server:

```bash
curl http://localhost:11434/api/tags
```

If the server is running, you'll get a JSON list of installed models. A "connection refused" error means the server isn't running.

**Port already in use:** on Windows and macOS the app already runs the server. If you see "address already in use", quit the Ollama app first, or don't run `ollama serve` at all.

---

## 6. Download the two models

```bash
ollama pull qwen2.5:7b
ollama pull llama3.1:8b
```

| Model | Download size | Memory at about 8K context | Licence |
|---|---|---|---|
| `qwen2.5:7b` | about 4.7 GB | about 5.7 GB | Apache 2.0 |
| `llama3.1:8b` | about 4.9 GB | about 6 GB | Meta Llama 3.1 Community License |

Check that both are installed:

```bash
ollama list
```

Downloads can take a while. If a download stops, run the same `pull` command again. It resumes.

---

## 7. Run a model

### Interactive chat

```bash
ollama run qwen2.5:7b
```

Type a question and press Enter. To leave the chat, type `/bye`.

### See what is loaded

```bash
ollama ps
```

This shows which models are in memory, how much memory they use, and whether they run on the CPU, the GPU, or both. Use it to confirm that only one model is loaded at a time.

### Unload a model

```bash
ollama stop qwen2.5:7b
```

Ollama also unloads a model on its own after the `OLLAMA_KEEP_ALIVE` time, which is 5 minutes by default.

### Remove a model

```bash
ollama rm llama3.1:8b
```

Only remove a model when the team has agreed it's not needed. The download can take a long time to get back.

---

## 8. Use the models from code

Ollama serves an HTTP API on `http://localhost:11434`. The Harbour provider adapter (Week 5) calls this API. These examples show the same calls.

### Quick test with curl

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "qwen2.5:7b",
  "messages": [{"role": "user", "content": "Say hello in Nigerian Pidgin in one sentence."}],
  "stream": false,
  "options": {"temperature": 0, "num_ctx": 8192}
}'
```

The reply includes the answer in `message.content`, and the token counts and timing in fields such as:

- `prompt_eval_count`: input tokens.
- `eval_count`: output tokens.
- `total_duration`: total time in nanoseconds.

### Python with httpx

Install httpx if you don't have it: `pip install httpx`.

```python
import httpx

OLLAMA_URL = "http://localhost:11434/api/chat"

def ask(model: str, prompt: str) -> dict:
    resp = httpx.post(
        OLLAMA_URL,
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
            "options": {"temperature": 0, "num_ctx": 8192},
        },
        timeout=120,  # CPU inference can be slow; allow two minutes
    )
    resp.raise_for_status()
    data = resp.json()
    return {
        "text": data["message"]["content"],
        "input_tokens": data.get("prompt_eval_count"),
        "output_tokens": data.get("eval_count"),
        "total_seconds": data.get("total_duration", 0) / 1e9,
    }

if __name__ == "__main__":
    for model in ["qwen2.5:7b", "llama3.1:8b"]:
        result = ask(model, "Classify this email as complaint, invoice, or other: 'My order is still missing.'")
        print(model, result)
```

### Ask for JSON

For triage and other structured tasks, ask Ollama to return JSON. Add `"format": "json"` to the request body, and ask for the JSON shape in the prompt. Then parse the reply and validate it with Pydantic. Don't trust the output without checking it.

```python
payload = {
    "model": "qwen2.5:7b",
    "messages": [{"role": "user", "content":
        'Return JSON only: {"category": "...", "urgency": "low|normal|high"}. '
        "Email: 'I was charged twice for my order.'"}],
    "stream": False,
    "format": "json",
    "options": {"temperature": 0, "num_ctx": 8192},
}
```

### Official Python library (optional)

Ollama also has an official Python package: `pip install ollama`. The team uses httpx in Week 5 so that everyone sees the raw API. You can use the package later.

---

## 9. Share one laptop with the class (for weaker laptops)

Use this only when a member's laptop can't run the models and a stronger laptop on the same private network can.

On the **server laptop**, make Ollama listen on the network:

- Windows: set `OLLAMA_HOST` to `0.0.0.0:11434` in your user environment variables, then restart Ollama.
- macOS: `launchctl setenv OLLAMA_HOST "0.0.0.0:11434"`, then restart the app.
- Linux: add `Environment="OLLAMA_HOST=0.0.0.0:11434"` under `[Service]` as in section 4, then restart.

Then:
- Allow Ollama through the firewall on the private network only.
- Other members call `http://<server-ip>:11434/api/chat` in place of `localhost`.

**Important:** Ollama has no login. Anyone who can reach port 11434 can use the server. Only use this on a trusted, private network, and set `OLLAMA_HOST` back to `127.0.0.1:11434` when the session ends.

---

## 10. Compare the two models on the same test set

This is the Week 5 comparison exercise, and it also gives the team its first model choice.

1. Write 10 to 20 test inputs, including some Pidgin messages, with the expected answer written before you run anything.
2. Use the same prompt, temperature 0 and `num_ctx` for both models.
3. Run each input through both models with the script in section 8.
4. Record for each run: the output, whether the JSON parsed, whether the answer matches the expected one, input tokens, output tokens, and total seconds.
5. Compare the results in a table. Look at format errors, accuracy, speed and token use.
6. Write the choice and the numbers in a short note. The TRD lists the model choice as ADR 5.

**Don't decide from one or two examples.** The test set is small, so treat the result as a first decision and rerun it in Week 14.

---

## 11. Troubleshooting

| Problem | What to check |
|---|---|
| `connection refused` on port 11434 | The server isn't running. Start the Ollama app, or run `ollama serve` in a terminal. |
| `address already in use` | Ollama is already running. Quit the app or service first. |
| `model not found` | Run `ollama pull <model>`, then `ollama list`. Check the spelling, including the tag after the colon. |
| Very slow replies | Expected on CPU-only laptops (section 2). Close other applications, reduce `num_ctx`, keep prompts short, or use a smaller model. `ollama ps` showing `100% CPU` is normal here. |
| Laptop runs out of memory or freezes | Set `OLLAMA_MAX_LOADED_MODELS=1`, lower `OLLAMA_CONTEXT_LENGTH`, close Docker, and use a smaller model. |
| Replies cut off or ignore the text you sent | Check `num_ctx`. The prompt and the answer both count towards the context. |
| Disk full | Move storage with `OLLAMA_MODELS` (section 4), or remove a model you no longer need. |
| Need more detail | Set `OLLAMA_DEBUG=1`, restart Ollama, and check the logs. On Linux use `journalctl -u ollama -f`. On other systems check the Ollama log folder for your version. |

---

## 12. Updating Ollama

- **Windows and macOS:** the app offers updates. Choose **Restart to update** from the tray or menu-bar icon, or download the latest version from ollama.com and install it over the old one.
- **Linux:** run the install script again: `curl -fsSL https://ollama.com/install.sh | sh`.

Downloaded models stay in place when you update Ollama. Check `ollama list` afterwards.

---

## 13. Done when

- [ ] `ollama --version` shows a version.
- [ ] The environment variables in section 4 are set, and Ollama was restarted after setting them.
- [ ] `curl http://localhost:11434/api/tags` lists both models.
- [ ] `ollama run qwen2.5:7b` answers a question, and `/bye` exits.
- [ ] `ollama run llama3.1:8b` answers a question, and `/bye` exits.
- [ ] The Python script in section 8 prints a result for both models.
- [ ] `ollama ps` shows only one model loaded after you switch between them.
- [ ] You can explain what `OLLAMA_MAX_LOADED_MODELS` and `OLLAMA_CONTEXT_LENGTH` do.

---

## 14. Limits and reminders

- Local models are weaker than hosted ones, especially in Pidgin. Measure before you trust them.
- Speed depends on your laptop. Latency results from one laptop don't carry over to another, or to the production setup.
- Ollama has no built-in login. Keep it on `127.0.0.1` unless you're sharing it on a private network (section 9).
- Each model has its own licence, as listed in section 6. Check it before you reuse a model outside the course.
- Use test data only in the labs.
