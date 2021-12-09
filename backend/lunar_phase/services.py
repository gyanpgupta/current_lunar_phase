import datetime
import ephem
import pytz
from django.conf import settings


class Moon:
    def __init__(self, tz=None):
        self.timezone = tz if tz else settings.TIME_ZONE
        self.moon = ephem
        self.date = datetime.datetime.now(tz=pytz.timezone(tz))

    def get_moon_phase(self):
        previous_phase, next_phase = None, None
        date = datetime.datetime.now(tz=pytz.timezone(self.timezone))
        last_new_moon = ephem.localtime(ephem.previous_new_moon(date)).replace(
            tzinfo=pytz.timezone(self.timezone)
        )
        for phase in ["first_quarter", "full_moon", "last_quarter", "new_moon"]:
            last_new_moon += datetime.timedelta(days=7)
            if last_new_moon.date() == date.date():
                return phase

        previous_new_moon = ephem.localtime(ephem.previous_new_moon(date)).replace(
            tzinfo=pytz.timezone(self.timezone)
        )
        previous_first_quarter_moon = ephem.localtime(
            ephem.previous_first_quarter_moon(date)
        ).replace(tzinfo=pytz.timezone(self.timezone))
        previous_full_moon = ephem.localtime(ephem.previous_full_moon(date)).replace(
            tzinfo=pytz.timezone(self.timezone)
        )
        previous_last_quarter_moon = ephem.localtime(
            ephem.previous_last_quarter_moon(date)
        ).replace(tzinfo=pytz.timezone(self.timezone))
        next_new_moon = ephem.localtime(ephem.next_new_moon(date)).replace(
            tzinfo=pytz.timezone(self.timezone)
        )
        next_first_quarter_moon = ephem.localtime(
            ephem.next_first_quarter_moon(date)
        ).replace(tzinfo=pytz.timezone(self.timezone))
        next_full_moon = ephem.localtime(ephem.next_full_moon(date)).replace(
            tzinfo=pytz.timezone(self.timezone)
        )
        next_last_quarter_moon = ephem.localtime(
            ephem.next_last_quarter_moon(date)
        ).replace(tzinfo=pytz.timezone(self.timezone))
        moon_phases = [
            (date, "date"),
            (previous_new_moon, "previous_new_moon"),
            (previous_first_quarter_moon, "previous_first_quarter_moon"),
            (previous_full_moon, "previous_full_moon"),
            (previous_last_quarter_moon, "previous_last_quarter_moon"),
            (next_new_moon, "next_new_moon"),
            (next_first_quarter_moon, "next_first_quarter_moon"),
            (next_full_moon, "next_full_moon"),
            (next_last_quarter_moon, "next_last_quarter_moon"),
        ]
        moon_phases.sort()

        for index, phase in enumerate(moon_phases):
            if phase[1] == "date":
                previous_phase = moon_phases[index - 1][1]
                next_phase = moon_phases[index + 1][1]

        if (
            previous_phase == "previous_first_quarter_moon"
            and next_phase == "previous_full_moon"
        ):
            return "Waxing Gibbous"
        elif (
            previous_phase == "previous_full_moon"
            and next_phase == "previous_last_quarter_moon"
        ):
            return "Waning Gibbous"
        elif (
            previous_phase == "previous_last_quarter_moon"
            and next_phase == "previous_new_moon"
        ):
            return "Waning Crescent"
        elif (
            previous_phase == "previous_new_moon"
            and next_phase == "next_first_quarter_moon"
        ):
            return "Waxing Crescent"
        elif (
            previous_phase == "next_first_quarter_moon"
            and next_phase == "next_full_moon"
        ):
            return "Waxing Gibbous"
        elif (
            previous_phase == "next_full_moon"
            and next_phase == "next_last_quarter_moon"
        ):
            return "Waning Gibbous"
        elif (
            previous_phase == "next_last_quarter_moon" and next_phase == "next_new_moon"
        ):
            return "Waning Crescent"
        elif (
            previous_phase == "previous_last_quarter_moon"
            and next_phase == "next_new_moon"
        ):
            return "Waning Crescent"


if __name__ == "__main__":
    moon = Moon()
    print(moon.get_moon_phase())
