from pathlib import Path


class PATH(Path):
    def __init__(self, *args, **kwargs):
        Path.__init__(*args, **kwargs)

        if self.exists():
            return

        if not self.suffix:
            self.mkdir(parents=True)
            return

        self.touch()

        if '.json' in self.suffix:
            self.write_text("{}")


def run():
    print("WE ARE RUNNING")


def cli():
    run()
