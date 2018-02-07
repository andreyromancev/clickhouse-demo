import config

from clickhouse_driver import Client

c = Client(config.DB_CLICKHOUSE_HOST)
c.execute('CREATE DATABASE IF NOT EXISTS stats_db')
c.execute("""
    CREATE TABLE stats_db.stats_flat
    (
        project_id UInt32,
        message_type FixedString(1),
        message_id UInt32,
        post_id Nullable(UInt32),
        
        datetime DateTime DEFAULT now(),
        date Date DEFAULT today(),
        year UInt16,
        quarter UInt8,
        month UInt8,
        hour UInt8,
        
        total UInt32,
        viewed UInt32,
        selected UInt32,
        sent UInt32,
        
        opened_total UInt8,
        opened_dev_pc UInt8,
        opened_dev_mobile UInt8,
        opened_dev_tablet UInt8,
        opened_dev_other UInt8,
        opened_os_ios UInt8,
        opened_os_android UInt8,
        opened_os_winmobile UInt8,
        opened_os_windows UInt8,
        opened_os_linux UInt8,
        opened_os_macos UInt8,
        opened_os_other UInt8,
        
        clicked_total UInt8,
        clicked_dev_pc UInt8,
        clicked_dev_mobile UInt8,
        clicked_dev_tablet UInt8,
        clicked_dev_other UInt8,
        clicked_os_ios UInt8,
        clicked_os_android UInt8,
        clicked_os_winmobile UInt8,
        clicked_os_windows UInt8,
        clicked_os_linux UInt8,
        clicked_os_macos UInt8,
        clicked_os_other UInt8,
        
        stop_total UInt32,
        stop_invalid UInt32,
        stop_corp UInt32,
        stop_nomailru UInt32,
        stop_inactive UInt32,
        stop_nonexistent UInt32,
        stop_spam_added UInt32,
        stop_sendlog_added UInt32,
        stop_unsubscr UInt32,
        stop_letter_single_quarantine UInt32,
        stop_template_errors UInt32,
        
        bounce_total UInt32,
        bounce_nonexistent UInt32,
        bounce_temp_unavailable UInt32,
        bounce_spam UInt32,
        bounce_overflow UInt32,
        bounce_other UInt32
    )
    ENGINE = MergeTree(date, (project_id, message_type, message_id, date), 8192)
""")

c.execute("""
    CREATE TABLE stats_db.stats_null
    (
        project_id UInt32,
        message_type FixedString(1),
        message_id UInt32,
        post_id Nullable(UInt32),

        datetime DateTime DEFAULT now(),
        date Date DEFAULT today(),
        year UInt16,
        quarter UInt8,
        month UInt8,
        hour UInt8,

        total Nullable(UInt32),
        viewed Nullable(UInt32),
        selected Nullable(UInt32),
        sent Nullable(UInt32),

        opened_total Nullable(UInt8),
        opened_dev_pc Nullable(UInt8),
        opened_dev_mobile Nullable(UInt8),
        opened_dev_tablet Nullable(UInt8),
        opened_dev_other Nullable(UInt8),
        opened_os_ios Nullable(UInt8),
        opened_os_android Nullable(UInt8),
        opened_os_winmobile Nullable(UInt8),
        opened_os_windows Nullable(UInt8),
        opened_os_linux Nullable(UInt8),
        opened_os_macos Nullable(UInt8),
        opened_os_other Nullable(UInt8),

        clicked_total Nullable(UInt8),
        clicked_dev_pc Nullable(UInt8),
        clicked_dev_mobile Nullable(UInt8),
        clicked_dev_tablet Nullable(UInt8),
        clicked_dev_other Nullable(UInt8),
        clicked_os_ios Nullable(UInt8),
        clicked_os_android Nullable(UInt8),
        clicked_os_winmobile Nullable(UInt8),
        clicked_os_windows Nullable(UInt8),
        clicked_os_linux Nullable(UInt8),
        clicked_os_macos Nullable(UInt8),
        clicked_os_other Nullable(UInt8),

        stop_total Nullable(UInt32),
        stop_invalid Nullable(UInt32),
        stop_corp Nullable(UInt32),
        stop_nomailru Nullable(UInt32),
        stop_inactive Nullable(UInt32),
        stop_nonexistent Nullable(UInt32),
        stop_spam_added Nullable(UInt32),
        stop_sendlog_added Nullable(UInt32),
        stop_unsubscr Nullable(UInt32),
        stop_letter_single_quarantine Nullable(UInt32),
        stop_template_errors Nullable(UInt32),

        bounce_total Nullable(UInt32),
        bounce_nonexistent Nullable(UInt32),
        bounce_temp_unavailable Nullable(UInt32),
        bounce_spam Nullable(UInt32),
        bounce_overflow Nullable(UInt32),
        bounce_other Nullable(UInt32)
    )
    ENGINE = MergeTree(date, (project_id, message_type, message_id, date), 8192)
""")

c.execute("""
    CREATE TABLE stats_db.stats_collapse
    (
        project_id UInt32,
        message_type FixedString(1),
        message_id UInt32,
        post_id Nullable(UInt32),

        datetime DateTime DEFAULT now(),
        date Date DEFAULT today(),
        year UInt16,
        quarter UInt8,
        month UInt8,
        hour UInt8,

        total UInt32,
        viewed UInt32,
        selected UInt32,
        sent UInt32,

        opened_total UInt8,
        clicked_total UInt8,
        
        device Nullable(FixedString(1)),
        os Nullable(FixedString(1)),

        stop_total UInt32,
        stop_invalid UInt32,
        stop_corp UInt32,
        stop_nomailru UInt32,
        stop_inactive UInt32,
        stop_nonexistent UInt32,
        stop_spam_added UInt32,
        stop_sendlog_added UInt32,
        stop_unsubscr UInt32,
        stop_letter_single_quarantine UInt32,
        stop_template_errors UInt32,

        bounce_total UInt32,
        bounce_nonexistent UInt32,
        bounce_temp_unavailable UInt32,
        bounce_spam UInt32,
        bounce_overflow UInt32,
        bounce_other UInt32
    )
    ENGINE = MergeTree(date, (project_id, message_type, message_id, date), 8192)
""")
