import os
import argparse


class Controller():
    def __init__(self):
        self.arg_parsing()
        self.args_to_environments()
        # self.run_scraper_module()
        os.system('python3 scrap.py')

    def arg_parsing(self):

        parser = argparse.ArgumentParser()
        parser.add_argument("-u", "--username", required=True)
        parser.add_argument("-p", "--password", required=True)

        self.args = parser.parse_args()

    def args_to_environments(self):

        os.environ['USERNAME'] = self.args.username
        os.environ['PASSWORD'] = self.args.password



if __name__ == '__main__':
    Controller()
