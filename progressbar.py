import sys
import time
import datetime

class ProgressBar():
    def __init__(self, title="Progress", width=30, total=100, indicator=">"):
        self.title = title
        self.width = width

        self.total = total

        self._progress = 0
        self._start_time = time.time()
        self._the_time = self._start_time
        self.indicator = indicator

        self.update()

    def draw(self):

        sys.stdout.write(self._the_bar)
        sys.stdout.flush()

    def message(self, msg):

        nspaces = len(self._the_bar) - len(msg)

        if nspaces > 0:
            spaces = " "*nspaces
        else:
            spaces = ""

        sys.stdout.write(" %s%s\n" % (msg, spaces))
        sys.stdout.flush()

    def update(self, count=0):

        self._progress = count / (self.total-1)

        left = int(self._progress * self.width)
        right = int(self.width - left)

        left_bar = "-"*(left)
        right_bar = " "*right

        bar = left_bar + self.indicator + right_bar

        self._the_time = time.time()
        time_elapsed = self._the_time - self._start_time

        if count > 0:
            time_remaining = (self.total - count) * (time_elapsed / count)
            time_remaining = (
                str(datetime.timedelta(
                    seconds=int(time_remaining))))
        else:
            time_remaining = "unknown"

        output = (
            self.title,
            bar,
            round(self._progress*100, 3),
            str(datetime.timedelta(seconds=int(time_elapsed))),
            time_remaining,
        )

        self._the_bar = "\r%s: [%s] %.3f%%, elapsed: %s , remaining: %s" % output

    def end(self):
        sys.stdout.write(" %s\n" % b'\xe2\x9c\x93'.decode("utf-8"))
        sys.stdout.flush()
