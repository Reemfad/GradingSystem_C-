def banner(title: str):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

def agent_start(name: str, color="🔵"):
    print(f"\n{color} {name.upper()} AGENT STARTED")

def agent_done(name: str, extra=""):
    print(f"✅ {name.upper()} COMPLETED {extra}")

def token_estimate(agent: str, input_tokens: int, max_output: int):
    print(f"📊 {agent} - Estimated input: {input_tokens}, max output: {max_output}")

def tpm_status(current: int, limit: int):
    print(f"📊 Current TPM usage: {current}/{limit}")

def rpm_wait(seconds: float):
    print(f"⏳ RPM limit. Waiting {seconds:.1f}s...")
