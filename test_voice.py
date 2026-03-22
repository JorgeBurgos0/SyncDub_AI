import requests
import time
import glob
import json

base_url = "http://localhost:8000"
# Find latest project
j_files = glob.glob("uploads/*.json")
if not j_files:
    print("NO PROJECTS!")
    exit(1)

project_path = max(j_files)
project_id = project_path.split("/")[-1].replace(".json", "")

print(f"Testing on project {project_id}")

# 1. Fetch current data
res = requests.get(f"{base_url}/api/data/{project_id}")
data = res.json()
print("Original segment 1 voice:", data[0].get("voice"))

# 2. Update to santa
data[0]["voice"] = "em_santa"
res_put = requests.put(f"{base_url}/api/data/{project_id}", json=data)
print("PUT response:", res_put.status_code)

res = requests.get(f"{base_url}/api/data/{project_id}")
data2 = res.json()
print("Voice after PUT:", data2[0].get("voice"))

# 3. Regen audio
res_regen = requests.post(f"{base_url}/api/generate-audio/{project_id}/1")
print("Regen started", res_regen.status_code)

# 4. Wait for idle
while True:
    st = requests.get(f"{base_url}/api/status/{project_id}").json()
    if st["status"] == "idle":
        break
    elif "error" in st["status"]:
        print("ERROR IN STATUS:", st["status"])
        break
    time.sleep(1)

# 5. Fetch data again
res = requests.get(f"{base_url}/api/data/{project_id}")
data3 = res.json()
print("Voice after REGEN:", data3[0].get("voice"))
