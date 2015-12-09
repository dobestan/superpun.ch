def meta_image_upload_to(instance, filename):
    return "tidbits/{filename}.{extension}".format(
        filename=instance.hash_id,
        extension=filename.split('.')[-1],
    )
