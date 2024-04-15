import os
import requests
import sys
import tarfile

def main():
    changed_files_path = sys.argv[1]
    new_services = set()
    with open(changed_files_path, "r") as file:
        changed_files = file.readlines()
        for changed_file in changed_files:
            path = changed_file.split("/")
            if len(path) < 2:
                continue
            service = path[0]
            if not os.path.exists(service):
                continue
            # items = os.listdir()
            # if service in items:
            #     continue
            new_services.add(service)
    for new_service in new_services:
        service_tar = new_service + ".tar.gz"
        with tarfile.open(service_tar, "w:gz") as tar:
            tar.add(new_service, arcname=os.path.basename(new_service))
        files = {
            "service": (new_service, open(service_tar, "rb"), "application/gzip")
        }
        response = requests.post(
            url="http://127.0.0.1:8000/v1", 
            files=files
        )
        print(response.text)
        if not response.ok:
            sys.exit(1)

if __name__ == "__main__":
    main()
