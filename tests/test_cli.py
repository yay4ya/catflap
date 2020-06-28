from catflap.cli import create_parser, run_from_args


class TestCLI:
    def setup(self):
        self.parser = create_parser()

    def test_cli(self):
        video_url = "https://www.youtube.com/watch?v=YGRKqrEprEo"
        proxy = "stdout"
        max_requests = "1"

        args = self.parser.parse_args(
            [video_url, "--proxy", proxy, "--max-requests", max_requests])

        run_from_args(args)
