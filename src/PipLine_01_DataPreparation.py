import os
import yaml
import argparse
import logging




if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="default")
    args.add_argument("--datasource",default=None)

    parsed_args = args.parse_args()
    print(parsed_args.datasource,parsed_args.config)