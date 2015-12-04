"""magicento.magicento: provides entry point main()."""


__version__ = "0.0.1"


import argparse


def main():
    Beanstalk()


class Arguments():
    def parse_arguments():
        parser = argparse.ArgumentParser(description='Run Magic commands.')
        parser.add_argument('service',
                            help='service to interact with')
        parser.add_argument('action',
                            help='action to perform on service')
        return parser.parse_args()


class Beanstalk():
    def __init__(self):
        args = Arguments.parse_arguments()
        if args.service == "beanstalk" and args.action == "create":
            Beanstalk.create_beanstalk()

    def create_beanstalk():
        pass
