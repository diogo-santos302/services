import os
import requests
import sys
import tarfile

def main():
    changed_files_path = sys.argv[1]
    new_services = _get_new_services_from_diff(changed_files_path)
    if len(new_services) == 0:
        print("No new service detected")
    for new_service in new_services:
        service_tar = _compress_service(new_service)
        response = _onboard_service(new_service, service_tar)
        print(response.text)
        if not response.ok:
            sys.exit(1)

def _get_new_services_from_diff(changed_files_path: str) -> set:
    new_services = set()
    with open(changed_files_path, "r") as file:
        changed_files = file.readlines()
        for changed_file in changed_files:
            path = changed_file.split("/")
            is_service = len(path) > 1
            if not is_service:
                continue
            service = path[0]
            was_service_deleted = not os.path.exists(service)
            if was_service_deleted:
                continue
            new_services.add(service)
    return new_services

def _compress_service(name: str) -> str:
    service_tar = name + ".tar.gz"
    with tarfile.open(service_tar, "w:gz") as tar:
        tar.add(name, arcname=os.path.basename(name))
    return service_tar

def _onboard_service(name: str, tar_path: str):
    api_url = os.environ.get("ACTIONS_API", "localhost")
    files = {
        "service": (name, open(tar_path, "rb"), "application/gzip")
    }
    return requests.post(
        url=f"http://{api_url}:8000/v1", 
        files=files
    )

if __name__ == "__main__":
    main()
