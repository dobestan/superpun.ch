from django.apps import AppConfig


class TidbitsAppConfig(AppConfig):
    name = 'tidbits'

    def ready(self):
        from tidbits.signals.pre_save import pre_save_tidbit
        from tidbits.signals.post_save import create_hash_id, update_meta_tags
