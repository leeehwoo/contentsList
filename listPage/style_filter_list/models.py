# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Banner(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=1)
    type = models.CharField(max_length=20)
    priority = models.IntegerField(blank=True, null=True)
    display_timing = models.CharField(max_length=255, blank=True, null=True)
    shutter_times = models.IntegerField(blank=True, null=True)
    link_type = models.CharField(max_length=20)
    link = models.TextField(blank=True, null=True)
    scheme = models.TextField(blank=True, null=True)
    sticker_id = models.BigIntegerField(blank=True, null=True)
    category_ids = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    text = models.CharField(max_length=255, blank=True, null=True)
    localized_text = models.TextField(blank=True, null=True)
    bg_color = models.CharField(max_length=20, blank=True, null=True)
    confirm_bg_color = models.CharField(max_length=20, blank=True, null=True)
    image = models.CharField(max_length=50, blank=True, null=True)
    resource_json = models.TextField(blank=True, null=True)
    image_full = models.CharField(max_length=50, blank=True, null=True)
    tooltip_position = models.CharField(max_length=20, blank=True, null=True)
    target_user = models.CharField(max_length=4, blank=True, null=True)
    display_times = models.IntegerField(blank=True, null=True)
    display_duration = models.IntegerField(blank=True, null=True)
    display_gap_sec = models.IntegerField(blank=True, null=True)
    view_limit_count = models.IntegerField(blank=True, null=True)
    weekend_view_limit_count = models.IntegerField(blank=True, null=True)
    current_view_count = models.IntegerField(blank=True, null=True)
    view_count_marked = models.DateTimeField(blank=True, null=True)
    weekday_request_limit_count = models.IntegerField(blank=True, null=True)
    weekend_request_limit_count = models.IntegerField(blank=True, null=True)
    today_request_count = models.IntegerField(blank=True, null=True)
    today_request_marked = models.DateTimeField(blank=True, null=True)
    min_ios_version = models.CharField(max_length=20, blank=True, null=True)
    max_ios_version = models.CharField(max_length=20, blank=True, null=True)
    min_android_version = models.CharField(max_length=20, blank=True, null=True)
    max_android_version = models.CharField(max_length=20, blank=True, null=True)
    min_ios_os_version = models.CharField(max_length=20, blank=True, null=True)
    min_android_os_version = models.CharField(max_length=20, blank=True, null=True)
    download_from = models.DateTimeField(blank=True, null=True)
    start_display_date = models.DateTimeField(blank=True, null=True)
    end_display_date = models.DateTimeField(blank=True, null=True)
    designated_countries = models.TextField(blank=True, null=True)
    banned_countries = models.TextField(blank=True, null=True)
    admin = models.CharField(max_length=10)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'banner'


class ContentIdSequence(models.Model):
    content_type = models.CharField(primary_key=True, max_length=50)
    last_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'content_id_sequence'


class Device(models.Model):
    sno = models.CharField(unique=True, max_length=50)
    device_type = models.CharField(max_length=1)
    device_token = models.CharField(unique=True, max_length=255, blank=True, null=True)
    device_model = models.CharField(max_length=50)
    app_version = models.CharField(max_length=20)
    os_version = models.CharField(max_length=50)
    language = models.CharField(max_length=10)
    country = models.CharField(max_length=4)
    use_push_notification = models.IntegerField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'device'


class DeviceConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=1)
    type = models.CharField(max_length=10)
    config_json = models.TextField(blank=True, null=True)
    device_types = models.CharField(max_length=255, blank=True, null=True)
    min_ios_version = models.CharField(max_length=255, blank=True, null=True)
    max_ios_version = models.CharField(max_length=255, blank=True, null=True)
    min_android_version = models.CharField(max_length=255, blank=True, null=True)
    max_android_version = models.CharField(max_length=255, blank=True, null=True)
    min_ios_os_version = models.CharField(max_length=20, blank=True, null=True)
    min_android_os_version = models.IntegerField(blank=True, null=True)
    start_display_date = models.DateTimeField(blank=True, null=True)
    end_display_date = models.DateTimeField(blank=True, null=True)
    designated_countries = models.TextField(blank=True, null=True)
    banned_countries = models.TextField(blank=True, null=True)
    skin_smooth = models.TextField(blank=True, null=True)
    sharpness = models.TextField(blank=True, null=True)
    toneup = models.TextField(blank=True, null=True)
    version = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    admin = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_config'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GlobalInformation(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'global_information'


class Makeup(models.Model):
    id = models.BigAutoField(primary_key=True)
    builtin_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=10)
    makeup_name = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    sub_name = models.TextField(blank=True, null=True)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    thumbnail_color = models.CharField(max_length=20, blank=True, null=True)
    version = models.BigIntegerField()
    screen_capture_mode = models.TextField()  # This field type is a guess.
    download_type = models.CharField(max_length=255)
    device_types = models.CharField(max_length=20, blank=True, null=True)
    min_ios_version = models.CharField(max_length=20, blank=True, null=True)
    max_ios_version = models.CharField(max_length=20, blank=True, null=True)
    min_android_version = models.CharField(max_length=20, blank=True, null=True)
    max_android_version = models.CharField(max_length=20, blank=True, null=True)
    newmark_end_date = models.DateTimeField(blank=True, null=True)
    designated_countries = models.TextField(blank=True, null=True)
    banned_countries = models.TextField(blank=True, null=True)
    sale = models.TextField()  # This field type is a guess.
    package_json = models.TextField(blank=True, null=True)
    for_marketing = models.TextField(blank=True, null=True)  # This field type is a guess.
    orderz = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField()
    created = models.DateTimeField()
    admin = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'makeup'


class PushMessageTemplate(models.Model):
    name = models.CharField(unique=True, max_length=45)
    badge_count = models.SmallIntegerField()
    action_type = models.CharField(max_length=2)
    version_min = models.CharField(max_length=20, blank=True, null=True)
    version_max = models.CharField(max_length=20, blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)
    localized_messages = models.TextField(blank=True, null=True)
    action_argument = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField()
    admin = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'push_message_template'


class PushReservation(models.Model):
    filter = models.TextField()
    status = models.CharField(max_length=1)
    push_template_id = models.IntegerField()
    getui_task_id = models.CharField(max_length=50, blank=True, null=True)
    sending_time = models.DateTimeField()
    sent_count = models.IntegerField()
    started = models.DateTimeField(blank=True, null=True)
    ended = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'push_reservation'


class SpecialFilter(models.Model):
    id = models.BigAutoField(primary_key=True)
    builtin_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=10)
    filter_name = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    sub_name = models.TextField(blank=True, null=True)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()
    screen_capture_mode = models.TextField()  # This field type is a guess.
    download_type = models.CharField(max_length=255)
    display_type = models.CharField(max_length=6, blank=True, null=True)
    device_types = models.CharField(max_length=20, blank=True, null=True)
    min_ios_version = models.CharField(max_length=20, blank=True, null=True)
    max_ios_version = models.CharField(max_length=20, blank=True, null=True)
    min_android_version = models.CharField(max_length=20, blank=True, null=True)
    max_android_version = models.CharField(max_length=20, blank=True, null=True)
    newmark_end_date = models.DateTimeField(blank=True, null=True)
    designated_countries = models.TextField(blank=True, null=True)
    banned_countries = models.TextField(blank=True, null=True)
    sale = models.TextField()  # This field type is a guess.
    for_marketing = models.TextField(blank=True, null=True)  # This field type is a guess.
    package_json = models.TextField(blank=True, null=True)
    makeup_json = models.TextField(blank=True, null=True)
    updated = models.DateTimeField()
    created = models.DateTimeField()
    admin = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'special_filter'


class SpecialFilterGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    position = models.CharField(max_length=5, blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    sub_name = models.TextField(blank=True, null=True)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    guide_popup_image = models.TextField(blank=True, null=True)
    designated_countries = models.TextField(blank=True, null=True)
    banned_countries = models.TextField(blank=True, null=True)
    orderz = models.IntegerField()
    prev_filter_id = models.BigIntegerField(blank=True, null=True)
    sale = models.TextField()  # This field type is a guess.
    for_marketing = models.TextField(blank=True, null=True)  # This field type is a guess.
    updated = models.DateTimeField()
    created = models.DateTimeField()
    admin = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'special_filter_group'


class SpecialFilterGroupIndices(models.Model):
    order_group = models.CharField(primary_key=True, max_length=10)
    order_country = models.CharField(max_length=3)
    group_id = models.BigIntegerField()
    orderz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'special_filter_group_indices'
        unique_together = (('order_group', 'order_country', 'group_id'),)


class SpecialFilterGroupRelationship(models.Model):
    group_id = models.BigIntegerField(primary_key=True)
    filter_id = models.BigIntegerField()
    orderz = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'special_filter_group_relationship'
        unique_together = (('group_id', 'filter_id'),)


class SpecialFilterIndices(models.Model):
    order_group = models.CharField(primary_key=True, max_length=10)
    order_country = models.CharField(max_length=3)
    group_id = models.BigIntegerField()
    filter_id = models.BigIntegerField()
    orderz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'special_filter_indices'
        unique_together = (('order_group', 'order_country', 'group_id', 'filter_id'),)


class Splash(models.Model):
    name = models.CharField(max_length=50)
    priority = models.IntegerField()
    type = models.CharField(max_length=2)
    show_close_button = models.CharField(max_length=1)
    top_logo = models.TextField(blank=True, null=True)  # This field type is a guess.
    link = models.TextField(blank=True, null=True)
    scheme = models.TextField(blank=True, null=True)
    link_type = models.CharField(max_length=20, blank=True, null=True)
    file = models.CharField(max_length=255, blank=True, null=True)
    file_full_size = models.CharField(max_length=255, blank=True, null=True)
    min_ios_version = models.CharField(max_length=20, blank=True, null=True)
    max_ios_version = models.CharField(max_length=20, blank=True, null=True)
    min_android_version = models.CharField(max_length=20, blank=True, null=True)
    max_android_version = models.CharField(max_length=20, blank=True, null=True)
    min_android_os_version = models.CharField(max_length=20, blank=True, null=True)
    min_ios_os_version = models.CharField(max_length=20, blank=True, null=True)
    target_user = models.CharField(max_length=4, blank=True, null=True)
    launch_count = models.IntegerField(blank=True, null=True)
    launch_hours = models.IntegerField(blank=True, null=True)
    start_download_date = models.DateTimeField()
    start_display_date = models.DateTimeField()
    end_display_date = models.DateTimeField()
    designated_countries = models.CharField(max_length=255, blank=True, null=True)
    banned_countries = models.CharField(max_length=255, blank=True, null=True)
    display_gap_sec = models.PositiveIntegerField(blank=True, null=True)
    display_duration = models.PositiveIntegerField(blank=True, null=True)
    ad_url = models.CharField(max_length=255, blank=True, null=True)
    view_limit_count = models.IntegerField(blank=True, null=True)
    current_view_count = models.IntegerField(blank=True, null=True)
    view_count_marked = models.DateTimeField(blank=True, null=True)
    admin = models.CharField(max_length=20, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'splash'


class Style(models.Model):
    id = models.BigAutoField(primary_key=True)
    builtin_id = models.IntegerField(blank=True, null=True)
    content_type = models.CharField(max_length=5, blank=True, null=True)
    type = models.CharField(max_length=10)
    style_name = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    localized_names = models.TextField(blank=True, null=True)
    sub_name = models.TextField(blank=True, null=True)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    thumbnail_v2 = models.CharField(max_length=255, blank=True, null=True)
    localized_thumbnails = models.TextField(blank=True, null=True)
    thumbnails = models.TextField(blank=True, null=True)
    thumbnail_color = models.CharField(max_length=20, blank=True, null=True)
    version = models.BigIntegerField()
    screen_capture_mode = models.TextField()  # This field type is a guess.
    sound = models.BooleanField(blank=True, null=True)  # This field type is a guess.
    smart_blur = models.BooleanField(blank=True, null=True)  # This field type is a guess.
    download_type = models.CharField(max_length=255)
    device_level = models.CharField(max_length=2, blank=True, null=True)
    device_types = models.CharField(max_length=20, blank=True, null=True)
    min_ios_version = models.CharField(max_length=20, blank=True, null=True)
    max_ios_version = models.CharField(max_length=20, blank=True, null=True)
    min_android_version = models.CharField(max_length=20, blank=True, null=True)
    max_android_version = models.CharField(max_length=20, blank=True, null=True)
    start_display_date = models.DateTimeField(blank=True, null=True)
    end_display_date = models.DateTimeField(blank=True, null=True)
    newmark_end_date = models.DateTimeField(blank=True, null=True)
    designated_countries = models.TextField(blank=True, null=True)
    banned_countries = models.TextField(blank=True, null=True)
    sale = models.TextField()  # This field type is a guess.
    package_json = models.TextField(blank=True, null=True)
    package_file_size = models.BigIntegerField(blank=True, null=True)
    package_file_ext_processed = models.TextField(blank=True, null=True)  # This field type is a guess.
    for_marketing = models.TextField(blank=True, null=True)  # This field type is a guess.
    promotion_mission = models.CharField(max_length=255, blank=True, null=True)
    mission_url = models.CharField(max_length=512, blank=True, null=True)
    mission_url_external = models.TextField(blank=True, null=True)  # This field type is a guess.
    orderz = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField()
    created = models.DateTimeField()
    admin = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'style'


class StyleBanIndices(models.Model):
    order_group = models.CharField(primary_key=True, max_length=10)
    order_country = models.CharField(max_length=3)
    group_id = models.BigIntegerField()
    ban_country = models.CharField(max_length=3)
    style_id = models.BigIntegerField()
    orderz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'style_ban_indices'
        unique_together = (('order_group', 'order_country', 'group_id', 'ban_country', 'style_id'),)


class StyleGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    position = models.CharField(max_length=5, blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    sub_name = models.TextField(blank=True, null=True)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    designated_countries = models.TextField(blank=True, null=True)
    banned_countries = models.TextField(blank=True, null=True)
    sale = models.TextField()  # This field type is a guess.
    updated = models.DateTimeField()
    created = models.DateTimeField()
    admin = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'style_group'


class StyleGroupIndices(models.Model):
    order_group = models.CharField(primary_key=True, max_length=10)
    order_country = models.CharField(max_length=3)
    group_id = models.BigIntegerField()
    orderz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'style_group_indices'
        unique_together = (('order_group', 'order_country', 'group_id'),)


class StyleIndices(models.Model):
    order_group = models.CharField(primary_key=True, max_length=10)
    order_country = models.CharField(max_length=3)
    group_id = models.BigIntegerField()
    style_id = models.BigIntegerField()
    orderz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'style_indices'
        unique_together = (('order_group', 'order_country', 'group_id', 'style_id'),)


class Template(models.Model):
    id = models.BigAutoField(primary_key=True)
    content_type = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=255)
    localized_name = models.TextField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    media_count = models.IntegerField(blank=True, null=True)
    like_count = models.IntegerField(blank=True, null=True)
    view_count = models.IntegerField(blank=True, null=True)
    view_count_makred = models.DateTimeField(blank=True, null=True)
    create_count = models.IntegerField(blank=True, null=True)
    clip_count = models.IntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    localized_title = models.TextField(blank=True, null=True)
    localized_sub_title = models.TextField(blank=True, null=True)
    collection_id = models.BigIntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    link_type = models.CharField(max_length=20, blank=True, null=True)
    detail_page = models.TextField(blank=True, null=True)  # This field type is a guess.
    use_frame = models.TextField(blank=True, null=True)  # This field type is a guess.
    frame_color = models.CharField(max_length=10, blank=True, null=True)
    sticker_id = models.BigIntegerField(blank=True, null=True)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    thumbnail_ratio = models.FloatField(blank=True, null=True)
    thumbnail_sub = models.CharField(max_length=255, blank=True, null=True)
    thumbnail_event_camera = models.CharField(max_length=255, blank=True, null=True)
    preview_video = models.CharField(max_length=255, blank=True, null=True)
    orderz = models.IntegerField()
    sale = models.TextField()  # This field type is a guess.
    version = models.IntegerField()
    device_types = models.CharField(max_length=20, blank=True, null=True)
    use_on_gallery = models.TextField(blank=True, null=True)  # This field type is a guess.
    min_ios_version = models.CharField(max_length=20, blank=True, null=True)
    max_ios_version = models.CharField(max_length=20, blank=True, null=True)
    min_android_version = models.CharField(max_length=20, blank=True, null=True)
    max_android_version = models.CharField(max_length=20, blank=True, null=True)
    designated_countries = models.TextField(blank=True, null=True)
    banned_countries = models.TextField(blank=True, null=True)
    start_display_date = models.DateTimeField(blank=True, null=True)
    end_display_date = models.DateTimeField(blank=True, null=True)
    template_json = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    admin = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'template'


class TemplateCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    localized_title = models.TextField(blank=True, null=True)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    sale = models.TextField()  # This field type is a guess.
    default_category = models.TextField(blank=True, null=True)  # This field type is a guess.
    orderz = models.IntegerField()
    device_types = models.CharField(max_length=20, blank=True, null=True)
    min_ios_version = models.CharField(max_length=20, blank=True, null=True)
    max_ios_version = models.CharField(max_length=20, blank=True, null=True)
    min_android_version = models.CharField(max_length=20, blank=True, null=True)
    max_android_version = models.CharField(max_length=20, blank=True, null=True)
    designated_countries = models.TextField(blank=True, null=True)
    banned_countries = models.TextField(blank=True, null=True)
    start_display_date = models.DateTimeField(blank=True, null=True)
    end_display_date = models.DateTimeField(blank=True, null=True)
    collection = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField()
    updated = models.DateTimeField()
    admin = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'template_category'


class TemplateCategoryIndices(models.Model):
    category_id = models.BigIntegerField(primary_key=True)
    orderz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'template_category_indices'


class TemplateCategoryTemplate(models.Model):
    category_id = models.BigIntegerField(primary_key=True)
    template_id = models.BigIntegerField()
    orderz = models.IntegerField(blank=True, null=True)
    fix = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'template_category_template'
        unique_together = (('category_id', 'template_id'),)


class TemplateSearchKeyword(models.Model):
    category_id = models.BigIntegerField(primary_key=True)
    keyword = models.CharField(max_length=100)
    orderz = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'template_search_keyword'
        unique_together = (('category_id', 'keyword'),)


class TemplateSearchKeywordCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    device_types = models.CharField(max_length=20, blank=True, null=True)
    start_display_date = models.DateTimeField(blank=True, null=True)
    end_display_date = models.DateTimeField(blank=True, null=True)
    designated_countries = models.TextField(blank=True, null=True)
    banned_countries = models.TextField(blank=True, null=True)
    sale = models.TextField()  # This field type is a guess.
    orderz = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    admin = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'template_search_keyword_category'
