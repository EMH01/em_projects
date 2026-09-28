from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo


def current_time_in_zone(
    zone_name: str,
    *,
    now: datetime | None = None,
) -> datetime:
    reference = now or datetime.now(timezone.utc)
    if reference.tzinfo is None:
        reference = reference.replace(tzinfo=timezone.utc)
    return reference.astimezone(ZoneInfo(zone_name))


def local_time_from_offset(
    offset_seconds: int,
    *,
    now: datetime | None = None,
) -> datetime:
    reference = now or datetime.now(timezone.utc)
    if reference.tzinfo is None:
        reference = reference.replace(tzinfo=timezone.utc)
    local_zone = timezone(timedelta(seconds=offset_seconds))
    return reference.astimezone(local_zone)
