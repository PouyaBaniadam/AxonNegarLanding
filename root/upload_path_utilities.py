def get_upload_path(instance, filename):
    return f'releases/{instance.os}/{filename}'