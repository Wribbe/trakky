import sys


from pathlib import Path


class PATH(Path):
    def __init__(self, *args, **kwargs):
        Path.__init__(self, *args, **kwargs)

        if self.exists():
            return

        if not self.suffix:
            self.mkdir(parents=True)
            return

        self.touch()

        if '.json' in self.suffix:
            self.write_text("{}")


def main(args):
    print("WE ARE RUNNING")


def cli():
    main(sys.argv[1:])
