def parse_rfc3339(dt):
    import re
    broken = re.search(r'([0-9]{4})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2}):([0-9]{2})(\.([0-9]+))?(Z|([+-][0-9]{2}):([0-9]{2}))', dt)
    return datetime.datetime(
        year = int(broken.group(1)),
        month = int(broken.group(2)),
        day = int(broken.group(3)),
        hour = int(broken.group(4)),
        minute = int(broken.group(5)),
        second = int(broken.group(6)))