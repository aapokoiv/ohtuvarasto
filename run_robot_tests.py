#!/usr/bin/env python3
import sys
import time
import subprocess
import signal
import os


def run_tests():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Start Flask app in background
    env = os.environ.copy()
    env['FLASK_APP'] = 'src/app.py'
    
    flask_process = subprocess.Popen(
        ['poetry', 'run', 'python', '-m', 'flask', 'run', '--port=5000'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
        cwd=script_dir
    )
    
    # Wait for Flask to start
    print("Starting Flask app...")
    time.sleep(3)
    
    try:
        # Run Robot tests
        print("Running Robot tests...")
        result = subprocess.run(
            ['poetry', 'run', 'robot', 'src/tests/robot/'],
            cwd=script_dir,
            capture_output=False
        )
        return result.returncode
    finally:
        # Clean up Flask process
        print("Stopping Flask app...")
        flask_process.send_signal(signal.SIGTERM)
        flask_process.wait(timeout=5)


if __name__ == '__main__':
    sys.exit(run_tests())
