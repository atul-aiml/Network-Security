import os


class S3Sync:

  def sync_folder_to_s3(self, folder, aws_bucket_url):
    command = f"aws s3 sync {folder} {aws_bucket_url}"
    print(f"Running: {command}")
    exit_code = os.system(command)
    print(f"Exit code: {exit_code}")

  def sync_folder_from_s3(self, folder, aws_bucket_url):
    command = f"aws s3 sync {aws_bucket_url} {folder}"
    print(f"Running: {command}")
    exit_code = os.system(command)
    print(f"Exit code: {exit_code}")