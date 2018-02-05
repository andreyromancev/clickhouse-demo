import config

from clickhouse_driver import Client

c = Client(config.DB_CLICKHOUSE_HOST)
c.execute('CREATE DATABASE IF NOT EXISTS stats_db')
c.execute("""
    CREATE TABLE stats_db.stats
    (
        project_id UInt32,
        message_type FixedString(1),
        message_id UInt32,
        post_id Nullable(Int32),
        
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
        
        bounce_total UInt8,
        bounce_nonexistent UInt8,
        bounce_temp_unavailable UInt8,
        bounce_spam UInt8,
        bounce_overflow UInt8,
        bounce_other UInt8
    )
    ENGINE = MergeTree(date, (project_id, message_type, message_id, date), 8192)
""")
