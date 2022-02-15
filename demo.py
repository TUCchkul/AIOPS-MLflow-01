import os 
import mlflow 
import argparse
def evaluate(param1,param2):
    metric=param1**2 +param2**2
    return metric
def main(p1,p2):
    with mlflow.start_run():
        mlflow.log_param("param1")


if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument("__param1","-p1", type=int, default=2)
    args.add_argument("__param2","-p2", type=int,default=5)
    parsed_args=args.parse_args()

    