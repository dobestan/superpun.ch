def default_meta_image_upload_to(instance, filename):
    return "meta/{filename}.{extension}".format(
        filename=instance.site.domain,
        extension=filename.split('.')[-1],
    )
