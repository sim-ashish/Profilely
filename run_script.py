import subprocess

def run_command(command):
    """Run a shell command and print output in real-time."""
    print(f"\nRunning: {command}")
    process = subprocess.Popen(command, shell=True)

    process.communicate()

    if process.returncode != 0:
        print(f"❌ Command failed: {command}")
        exit(process.returncode)
    else:
        print(f"✅ Finished: {command}")

if __name__ == "__main__":
    commands = [
        "pip install uv",
        "uv run alembic revision --autogenerate -m 'Initial models'",
        "uv run alembic upgrade head"
    ]

    for cmd in commands:
        run_command(cmd)
